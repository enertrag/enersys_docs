# Enersys Overview

Enersys is an energy system modelling toolkit built on top of [PyPSA](https://pypsa.org/). It reuses PyPSA's `Network` structure and solvers while adding opinionated defaults and utilities that streamline typical studies at Enertrag.

## Getting started

When beginning a new analysis, copy the provided `project_template` folder into your working directory. The template contains minimal, working examples that can be adapted to your use case. After copying, open the scripts in your preferred editor and adjust them to match the scenario you want to investigate.

## Repository structure

- `project_template/` – starting point for new studies with a minimal runnable scenario and configuration helpers.
- `enersys/` – Python package that extends PyPSA with scenario management and data utilities.
- `docs/` – Sphinx documentation sources.
- `tests/` – unit tests ensuring the core functionality remains stable.

## Managing scenarios

Running many model variants manually can be tedious. The `Scenarios` helper
automates this process by varying parameters and executing the model for each
combination. Provide a function that assembles and returns a `Network` for a
given set of parameters. If the returned network has not been solved yet,
`Scenarios` will call `network.optimize()` automatically.

Two optional hooks allow further customisation:

- `modify_network` is executed **before** optimisation and only if the
  scenario function returned an unsolved network. It can be either a callable
  that tweaks the network or a `Network` instance. When a `Network` instance is
  supplied, the new `Network.modify_by_network` method is used to apply the
  component capacities from that network to the scenario network.
- `post_optimize` runs **after** optimisation and can trigger post-processing
  steps such as `Network.create_txt`.

Both hooks may optionally include any subset of the scenario parameters in
their function signature, but they do not have to.

Parameters can be divided into groups. Same groups are varied together. For different group permutations are created.
E.g. the parameters p1 = Parameter(values=[50, 100], group=1), p2 = Parameter(values=[8, 9], group=1) and
p3 = Parameter(values=[1000, 2000], group=2), the following four permutations would be evaluated:

| Scenario | p1  | p2 | p3   |
|----------|-----|----|------|
| 1        | 50  | 8  | 1000 |
| 2        | 50  | 8  | 2000 |
| 3        | 100 | 9  | 1000 |
| 4        | 100 | 9  | 2000 |

```python
from enersys.scenarios import Scenarios, Parameter

def scenario(co2_price, demand):
    # assemble a PyPSA network and return it unsolved
    network = ...
    return network

def post_optimize(network, co2_price):
    network.create_txt("result")

def modify_network(network, demand):
    # optional pre-optimisation adjustments
    return network

param_co2_price = Parameter(values=[50, 100], group=1)
param_demand = Parameter(values=[1.0, 1.2], group=2)

s = Scenarios(
    scenario,
    post_optimize=post_optimize,
    modify_network=modify_network,  # or pass an optimised Network instance
    co2_price=param_co2_price,
    demand=param_demand,
)
s.run(n_parallel=2)
```

Each parameter combination is solved and stored, allowing straightforward
comparison of results.

### Saving and reusing results

`Scenarios` can persist the outcome of a run for later inspection. Calling
`store_results_to_folder("path")` writes a `results.csv` with the evaluated
parameters and, if the result objects are networks, corresponding NetCDF
files. An existing `Scenarios` instance may later populate itself with these
values via `load_results_from_folder("path")`.

To rebuild a `Scenarios` object from disk there are two class methods:

- `Scenarios.restore_results_from_folder(folder, scenario)` creates the
  instance and loads the stored results directly.
- `Scenarios.create_from_results_folder(folder, scenario)` only restores the
  parameters. Because the parameters originate from `results.csv`, group
  information is lost and the already permuted values are provided as plain
  lists. If parameters need adjustment afterwards they can be overwritten with
  either a scalar, e.g. `s.parameter["param"] = 1`, or with a list matching the
  number of scenarios to compute.

### Modifying networks

The `Network` class offers `modify_by_network` to freeze the capacities from one
network onto another. This is particularly useful together with the
`modify_network` hook:

```python
n_ref = Network(...)
n_ref.optimize()

n_scenario = Network(...)
n_scenario.modify_by_network(n_ref)
```

Components that should remain expandable can set the new
`p_nom_must_extend` parameter. It behaves like `p_nom_extendable` but prevents
`modify_by_network` from fixing the capacity when another network is applied.

### Running scenario batches with Fabric uploads

`Scenarios` can create Fabric-ready upload folders automatically after each
successful scenario run. Enable this with `create_fabric_upload=True` and pass
project and scenario metadata either as explicit constructor arguments or via
`fabric_upload_kwargs`. Scenario rows are used to create stable `run_id` values
and, by default, each scenario is written to its own subfolder.

```python
s = Scenarios(
    scenario,
    create_fabric_upload=True,
    fabric_upload_folder_path="fabric_upload",
    project_id="project-42",
    project_name="Example project",
    scenario_name="base case",
    scenario_version="v1",
    scenario_subversion="sub-a",
    demand=[1.0, 1.2],
)
s.run()
```

When `Network.create_txt()` is called from a scenario run, Enersys also records
the scenario input parameters as output rows with categories named
`parameter <name>`. Numeric values are written to the `value` column; non-numeric
values are written to the `info` column. The same scenario-parameter KPI rows are
included in Fabric `output_kpi.csv` files.

## Post-processing and result exports

### Text output and custom KPIs

`Network.create_txt()` writes the standard KPI text file. Use
`additional_parameters` with `ResultValue` objects for project-specific KPIs or
metadata. Custom categories are preserved in the output and appended after the
standard Enersys categories.

```python
from enersys.post_processing.create_csv import ResultValue

network.create_txt(
    "results/output.txt",
    deprecated_layout=False,
    additional_parameters=[
        ResultValue(
            category="parameter comment",
            info="sensitivity run with constrained grid connection",
        ),
        ResultValue(
            category="custom KPI curtailed energy",
            unit="MWh/a",
            value=123.4,
        ),
    ],
)
```

The output includes run metadata such as snapshot start/end, snapshot count,
snapshot timestep width, objective value, runtime rows, and annualized cost KPIs.
Recent KPI categories include annual import/export costs, annual variable costs,
average variable costs, CAPEX/OPEX system share totals, storage charge cycles,
circular storage energy flow, and burned storage energy.

### Fabric upload package

`Network.create_fabric_upload()` creates a self-contained folder for Microsoft
Fabric ingestion without changing the local text-output format. It writes:

- `output_kpi.csv` – KPI rows with project, scenario, run, schema, visibility,
  status, and layout metadata.
- `output_runtime.csv` – tracked runtime rows.
- `timeseries_values.csv` and `timeseries_stats.csv` – selected model and input
  time series plus summary statistics.
- `input_timeseries_metadata.csv` – metadata for time series originally supplied
  through `Network.add` or through the `input_ts` argument.
- `input_model_init.csv`, `input_model_add.csv`, and
  `input_custom_constraints.csv` – model reconstruction metadata.
- `manifest.json` – schema version, run metadata, and file inventory.

```python
network.create_fabric_upload(
    folder_path="fabric_upload/base_case",
    project_id="project-42",
    project_name="Example project",
    scenario_name="base case",
    scenario_version="v1",
    scenario_subversion="sub-a",
    run_status="draft",
    visibility="private",
)
```

The Fabric ingestion notebook in `notebooks/fabric_ingestion_notebook.py` loads
these files into bronze, silver, and gold tables. It also creates optional Data
Agent helper tables with project, scenario, KPI, variant, model-parameter, and
time-series search views so Power BI, Fabric Data Agent, and Copilot Studio can
use the same curated semantics.

## Working with time series

### Prognos forecasts

Forecast electricity prices from the Prognos study can be loaded with `get_prognos_ts`:

```python
from enersys.data.electricity_price import get_prognos_ts

ts = get_prognos_ts(year=2030, azw=75, energy_type="wind")
```

If you already have a time index, pass it via `snapshots`:

```python
import pandas as pd
from enersys.data.electricity_price import get_prognos_ts

snapshots = pd.date_range("2030-01-01", periods=24, freq="h")
ts = get_prognos_ts(snapshots=snapshots, azw=75, energy_type="wind")
```

### Day-ahead and intraday prices

Historical market prices can be downloaded with `get_price_ts`:

```python
from enersys.data.electricity_price.get_day_ahead_ts import get_price_ts

day_ahead = get_price_ts(year=2021, price_type="day_ahead")
intraday = get_price_ts(year=2021, price_type="intraday_continous")
```

The downloaded data are cached locally so subsequent runs are fast.

### Aurora forecasts

Aurora electricity-price forecasts can be loaded with `get_aurora_ts`. The
helper supports the bundled `central` and `low` price levels and can return
hourly or 15-minute data. If `snapshots` are provided, Enersys infers whether
hourly or 15-minute values are needed and aligns the returned series to the
requested index.

```python
from enersys.data.electricity_price import get_aurora_ts, AuroraPriceLevel

prices = get_aurora_ts(year=2030, price_level=AuroraPriceLevel.central)
prices_15min = get_aurora_ts(
    snapshots=network.snapshots,
    price_level=AuroraPriceLevel.low,
)
```

### Multi-year helper indexes

Use `multiyear_snapshots` to build a concatenated `DatetimeIndex` for several
representative years and `multiyear_timeseries` to copy a one-year input profile
to multiple target years.

```python
from enersys.utils import multiyear_snapshots, multiyear_timeseries

snapshots = multiyear_snapshots([2030, 2035])
demand = multiyear_timeseries(demand_2030_profile, years=[2030, 2035])
```

### Renewable overbuild and wind quality helpers

`enersys.data.renewables.re_overbuild` contains helpers for overbuild-based wind
and solar time series. The wind quality helper module provides AZW correction
functions and bundled reference-yield lookup data for turbine types.

```python
from enersys.helpers.wind_quality_factor import get_azw_correction_factor

correction = get_azw_correction_factor(
    annual_turbine_yield=20_000_000,
    annual_reference_yield=26_347_424.8,
)
```

## Optimization helpers

### Rolling horizon optimization

For long time horizons, call `network.optimize.optimize_with_rolling_horizon()`
to solve consecutive windows instead of the full horizon at once. `horizon` and
`overlap` are measured in snapshots. Capacity expansion is intentionally
restricted: components with `p_nom_extendable=True` must also set
`p_nom_must_extend=True`, otherwise the rolling-horizon helper raises an error
before solving.

```python
network.optimize.optimize_with_rolling_horizon(
    horizon=168,
    overlap=24,
)
```

Optional per-component `rolling_horizon_update_fun` callbacks can update model
state after each completed non-overlap window.

## Typical workflow

1. Copy the project template and adjust the provided examples.
2. Build or adapt a PyPSA network using the template scripts.
3. Use `Scenarios` to sweep over key parameters.
4. Generate necessary time series such as Prognos forecasts or day-ahead prices.
5. Analyse and communicate results with your preferred plotting tools.

## Differences from PyPSA

PyPSA focuses on generic power system modelling. Enersys builds on this foundation with opinionated defaults, ready-made helpers and a project template that cater to typical Enertrag studies while remaining compatible with the PyPSA ecosystem.

## Further information

- See the [components](components.md) page for additional component parameters.
- The repository README covers installation and contribution guidelines.
- `project_template/scenario_variation.py` contains a minimal runnable scenario script.
