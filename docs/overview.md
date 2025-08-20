# Enersys Overview

Enersys is an energy system modelling toolkit built on top of [PyPSA](https://pypsa.org/). It reuses PyPSA's `Network` structure and solvers while adding opinionated defaults and utilities that streamline typical studies at Enertrag.

## Getting started

When beginning a new analysis, copy the provided `project_template` folder into your working directory. The template contains minimal, working examples that can be adapted to your use case. After copying, open the scripts in your preferred editor and adjust them to match the scenario you want to investigate.

## Repository structure

- `project_template/` – starting point for new studies with example scripts and configuration helpers.
- `enersys/` – Python package that extends PyPSA with scenario management and data utilities.
- `examples/` – small demonstrations of how to build and run networks.
- `docs/` – Sphinx documentation sources.
- `tests/` – unit tests ensuring the core functionality remains stable.

## Managing scenarios

Running many model variants manually can be tedious. The `Scenarios` helper automates this process by varying parameters 
and executing the model for each combination. Provide a function that assembles, optimizes, and returns a `Network` for 
a given set of parameters.

Parmameters can be divided into groups. Same groups are varied together. For different group permutations are created. 
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
    # assemble a PyPSA network, solve it and return the result
    network = ...
    network.optimize()
    return network

param_co2_price = Parameter(values=[50, 100], group=1)
param_demand = Param(values=[1.0, 1.2], group=2)
s = Scenarios(scenario, co2_price=param_co2_price, demand=param_demand)
s.run(n_parallel=2)
```

Each parameter combination is solved and stored, allowing straightforward comparison of results.

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
- The `examples` directory contains small demonstration scripts.
