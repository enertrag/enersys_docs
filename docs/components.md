# Components

This section lists the available components in Enersys. Each table shows the standard PyPSA parameters and additional Enersys-specific parameters. The "Source" column indicates whether a parameter comes from PyPSA or Enersys.

## Bus

| Parameter | Type | Unit | Default | Description | Source |
|-----------|------|------|---------|-------------|--------|
| name | string | | | Unique name of the bus | PyPSA |
| v_nom | float | kV | 0 | Nominal voltage magnitude | PyPSA |
| type | string | | "" | Network type (AC or DC) | PyPSA |
| v_mag_pu_set | float | p.u. | 1.0 | Voltage magnitude setpoint | PyPSA |
| v_ang_set | float | degrees | 0 | Voltage angle setpoint | PyPSA |
| v_mag_pu_min | float | p.u. | 0 | Minimum voltage magnitude | PyPSA |
| v_mag_pu_max | float | p.u. | inf | Maximum voltage magnitude | PyPSA |
| p_set | float | MW | 0 | Active power injection | PyPSA |
| q_set | float | Mvar | 0 | Reactive power injection | PyPSA |
| carrier | string | | "" | Carrier of the bus | PyPSA |
| unit | string | | "" | Unit of the carrier | PyPSA |
| sub_network | string | | "" | Sub-network identifier | PyPSA |
| x | float | degrees | NaN | X-position (longitude) | PyPSA |
| y | float | degrees | NaN | Y-position (latitude) | PyPSA |

_No Enersys-specific parameters are currently defined for buses._

## Generator

| Parameter | Type | Unit | Default | Description | Source |
|-----------|------|------|---------|-------------|--------|
| bus | string | | | Connected bus | PyPSA |
| p_nom | float | MW | 0 | Nominal power | PyPSA |
| p_nom_extendable | bool | | False | Allow capacity expansion | PyPSA |
| p_nom_min | float | MW | 0 | Minimum expandable capacity | PyPSA |
| p_nom_max | float | MW | inf | Maximum expandable capacity | PyPSA |
| p_set | float | MW | 0 | Dispatch power | PyPSA |
| p_min_pu | float | p.u. | 0 | Minimum output per unit | PyPSA |
| p_max_pu | float | p.u. | 1 | Maximum output per unit | PyPSA |
| efficiency | float | p.u. | 1 | Conversion efficiency | PyPSA |
| marginal_cost | float | currency/MWh | 0 | Variable costs | PyPSA |
| capital_cost | float | currency/MW | 0 | Annualized capital costs | PyPSA |
| build_year | int | year | 0 | First year available | PyPSA |
| lifetime | float | years | inf | Economic lifetime | PyPSA |
| carrier | string | | "" | Carrier of the generator | PyPSA |
| type | string | | "" | Technology type | PyPSA |
| x | float | degrees | NaN | X-position (longitude) | PyPSA |
| y | float | degrees | NaN | Y-position (latitude) | PyPSA |
| [marker](#marker) | string | | "o" | Optional plotting symbol | Enersys |
| [invest_cost](#invest_cost) | float | EUR/MW | NaN | Specific investment costs (CAPEX) | Enersys |
| [fo_cost](#fo_cost) | float | EUR/(MW·a) | NaN | Specific fixed operating costs (OPEX) | Enersys |
| [invest_cost_scale](#invest_cost_scale) | dict | EUR/MW | NaN | Size-dependent investment cost curves | Enersys |
| [p_sum_min](#p_sum_min) | float | MWh | NaN | Minimum cumulative active power output | Enersys |
| [p_sum_max](#p_sum_max) | float | MWh | NaN | Maximum cumulative active power output | Enersys |
| [p_sum_annual_min](#p_sum_annual_min) | float | MWh | NaN | Minimum annual active power output | Enersys |
| [p_sum_annual_max](#p_sum_annual_max) | float | MWh | NaN | Maximum annual active power output | Enersys |
| [cf_min](#cf_min) | float | p.u. | NaN | Minimum average capacity factor | Enersys |
| [cf_max](#cf_max) | float | p.u. | NaN | Maximum average capacity factor | Enersys |
| [standby_load](#standby_load) | dict | | False | Standby load as fraction of p_nom | Enersys |

## Load

| Parameter | Type | Unit | Default | Description | Source |
|-----------|------|------|---------|-------------|--------|
| bus | string | | | Connected bus | PyPSA |
| p_set | float | MW | 0 | Active power demand | PyPSA |
| q_set | float | Mvar | 0 | Reactive power demand | PyPSA |
| carrier | string | | "" | Carrier of the load | PyPSA |
| sign | int | | -1 | Sign convention | PyPSA |
| type | string | | "" | Technology type | PyPSA |
| [x](#x) | float | degrees | NaN | X-position (longitude) | Enersys |
| [y](#y) | float | degrees | NaN | Y-position (latitude) | Enersys |
| [marker](#marker) | string | | "o" | Optional plotting symbol | Enersys |

## Link

| Parameter | Type | Unit | Default | Description | Source |
|-----------|------|------|---------|-------------|--------|
| bus0 | string | | | Input bus | PyPSA |
| bus1 | string | | | Output bus | PyPSA |
| p_nom | float | MW | 0 | Nominal power | PyPSA |
| p_nom_extendable | bool | | False | Allow capacity expansion | PyPSA |
| p_nom_min | float | MW | 0 | Minimum expandable capacity | PyPSA |
| p_nom_max | float | MW | inf | Maximum expandable capacity | PyPSA |
| p_min_pu | float | p.u. | -inf | Minimum dispatch per unit | PyPSA |
| p_max_pu | float | p.u. | inf | Maximum dispatch per unit | PyPSA |
| efficiency | float | p.u. | 1 | Efficiency from bus0 to bus1 | PyPSA |
| efficiency2 | float | p.u. | 1 | Efficiency from bus1 to bus0 | PyPSA |
| marginal_cost | float | currency/MWh | 0 | Variable costs | PyPSA |
| capital_cost | float | currency/MW | 0 | Annualized capital costs | PyPSA |
| length | float | km | 0 | Physical length of the link | PyPSA |
| carrier | string | | "" | Carrier of the link | PyPSA |
| type | string | | "" | Technology type | PyPSA |
| [x](#x) | float | degrees | NaN | X-position (longitude) | Enersys |
| [y](#y) | float | degrees | NaN | Y-position (latitude) | Enersys |
| [marker](#marker) | string | | "o" | Optional plotting symbol | Enersys |
| [invest_cost](#invest_cost) | float | EUR/MW | NaN | Specific investment costs (CAPEX) | Enersys |
| [fo_cost](#fo_cost) | float | EUR/(MW·a) | NaN | Specific fixed operating costs (OPEX) | Enersys |
| [invest_cost_scale](#invest_cost_scale) | dict | EUR/MW | NaN | Size-dependent investment cost curves | Enersys |
| [p_sum_min](#p_sum_min) | float | MWh | NaN | Minimum cumulative active power output | Enersys |
| [p_sum_max](#p_sum_max) | float | MWh | NaN | Maximum cumulative active power output | Enersys |
| [p_sum_annual_min](#p_sum_annual_min) | float | MWh | NaN | Minimum annual active power output | Enersys |
| [p_sum_annual_max](#p_sum_annual_max) | float | MWh | NaN | Maximum annual active power output | Enersys |
| [cf_min](#cf_min) | float | p.u. | NaN | Minimum average capacity factor | Enersys |
| [cf_max](#cf_max) | float | p.u. | NaN | Maximum average capacity factor | Enersys |
| [balancing](#balancing) | string | | "" | Period over which flows must balance (year, month, day, week, hour) | Enersys |
| [ref_output_bus1](#ref_output_bus1) | bool | | False | Use output bus power for sizing and costs | Enersys |
| [standby_load](#standby_load) | dict | | False | Standby load as fraction of p_nom | Enersys |

## StorageUnit

| Parameter | Type | Unit | Default | Description | Source |
|-----------|------|------|---------|-------------|--------|
| bus | string | | | Connected bus | PyPSA |
| [bus](#bus) | list | | | multi-bus connection | enersys |
| p_nom | float | MW | 0 | Nominal power | PyPSA |
| p_nom_extendable | bool | | False | Allow capacity expansion | PyPSA |
| p_nom_min | float | MW | 0 | Minimum expandable capacity | PyPSA |
| p_nom_max | float | MW | inf | Maximum expandable capacity | PyPSA |
| p_min_pu | float | p.u. | -inf | Minimum dispatch per unit | PyPSA |
| p_max_pu | float | p.u. | inf | Maximum dispatch per unit | PyPSA |
| max_hours | float | h | inf | Storage capacity relative to power | PyPSA |
| efficiency_store | float | p.u. | 1 | Charging efficiency | PyPSA |
| efficiency_dispatch | float | p.u. | 1 | Discharging efficiency | PyPSA |
| standing_loss | float | p.u./h | 0 | Hourly standing loss | PyPSA |
| inflow | series | MW | 0 | Inflow profile | PyPSA |
| state_of_charge_initial | float | MWh | 0 | Initial state of charge | PyPSA |
| state_of_charge_set | float | MWh | NaN | Fixed state of charge | PyPSA |
| cyclic_state_of_charge | bool | | False | Enforce cyclical state of charge | PyPSA |
| marginal_cost | float | currency/MWh | 0 | Variable costs | PyPSA |
| capital_cost | float | currency/MW | 0 | Annualized capital costs | PyPSA |
| build_year | int | year | 0 | First year available | PyPSA |
| lifetime | float | years | inf | Economic lifetime | PyPSA |
| carrier | string | | "" | Carrier of the unit | PyPSA |
| [x](#x) | float | degrees | NaN | X-position (longitude) | Enersys |
| [y](#y) | float | degrees | NaN | Y-position (latitude) | Enersys |
| [marker](#marker) | string | | "o" | Optional plotting symbol | Enersys |
| [invest_cost](#invest_cost) | float | EUR/MW | NaN | Specific investment costs (CAPEX) | Enersys |
| [fo_cost](#fo_cost) | float | EUR/(MW·a) | NaN | Specific fixed operating costs (OPEX) | Enersys |
| [invest_cost_scale](#invest_cost_scale) | dict | EUR/MW | NaN | Size-dependent investment cost curves | Enersys |
| [p_sum_min](#p_sum_min) | float | MWh | NaN | Minimum cumulative active power output | Enersys |
| [p_sum_max](#p_sum_max) | float | MWh | NaN | Maximum cumulative active power output | Enersys |
| [p_sum_annual_min](#p_sum_annual_min) | float | MWh | NaN | Minimum annual active power output | Enersys |
| [p_sum_annual_max](#p_sum_annual_max) | float | MWh | NaN | Maximum annual active power output | Enersys |
| [cf_min](#cf_min) | float | p.u. | NaN | Minimum average capacity factor | Enersys |
| [cf_max](#cf_max) | float | p.u. | NaN | Maximum average capacity factor | Enersys |
| [standby_load](#standby_load) | dict | | False | Standby load as fraction of p_nom | Enersys |


## Enersys-specific parameter examples

(bus)=
### bus

Multi-bus option for storage units will connect one storage to multiple buses. Energy charged on one bus can only be
discharged to the same bus. Internally, one storage unit is created for each bus, multiple buses will appear in the 
output files.

```python
network.add("StorageUnit", "storage_multibus", bus=["b_electricity_green", "b_electricity_grey", ...)
```

(marker)=
### marker

Defines the plotting symbol used when visualising network components, allowing custom markers on maps and diagrams.

```python
network.add("Generator", "example_gen", bus="bus0", marker="s")
```

(invest_cost)=
### invest_cost

Specifies the specific investment costs (CAPEX) per unit of nominal power. These costs are used in optimisation to value new capacity.

```python
network.add("Generator", "example_gen", bus="bus0", invest_cost=750000)
```

(fo_cost)=
### fo_cost

Defines the specific fixed operating costs (OPEX) per unit of nominal power and year, representing annual operation and maintenance expenses.

```python
network.add("Generator", "example_gen", bus="bus0", fo_cost=5000)
```

(invest_cost_scale)=
### invest_cost_scale

Provides a size-dependent investment cost curve. Keys denote capacity breakpoints and values give the corresponding specific investment costs, enabling modelling of economies of scale.

```python
network.add("Generator", "example_gen", bus="bus0", invest_cost_scale={100: 900000})
```

(p_sum_min)=
### p_sum_min

Enforces a minimum cumulative active power production over the entire simulation horizon.

```python
network.add("Generator", "example_gen", bus="bus0", p_sum_min=10)
```

(p_sum_max)=
### p_sum_max

Sets a maximum limit on the cumulative active power production over the whole simulation period.

```python
network.add("Generator", "example_gen", bus="bus0", p_sum_max=100)
```

(p_sum_annual_min)=
### p_sum_annual_min

Requires a minimum amount of active power to be produced in each modelled year.

```python
network.add("Generator", "example_gen", bus="bus0", p_sum_annual_min=500)
```

(p_sum_annual_max)=
### p_sum_annual_max

Restricts the annual active power production to not exceed a specified value in each year.

```python
network.add("Generator", "example_gen", bus="bus0", p_sum_annual_max=1000)
```

(cf_min)=
### cf_min

Defines a lower bound on the average capacity factor over the modelling horizon.

```python
network.add("Generator", "example_gen", bus="bus0", cf_min=0.2)
```

(cf_max)=
### cf_max

Specifies an upper bound on the average capacity factor across the simulation period.

```python
network.add("Generator", "example_gen", bus="bus0", cf_max=0.8)
```

(standby_load)=
### standby_load

Represents standby consumption as a fraction of nominal power, modelling electricity use while the component is idle.

```python
network.add("Generator", "example_gen", bus="bus0", standby_load={"p": 0.05})
```

(x)=
### x

Stores the x‑coordinate (for example, longitude) of a component for plotting and geographical analyses.

```python
network.add("Load", "example_load", bus="bus0", x=10)
```

(y)=
### y

Stores the y‑coordinate (for example, latitude) of a component for plotting and geographical analyses.

```python
network.add("Load", "example_load", bus="bus0", y=50)
```

(balancing)=
### balancing

Defines the period over which flows on a link must balance (such as year, month, week or hour) to model multi-period constraints.

```python
network.add("Link", "example_link", bus0="b0", bus1="b1", balancing="year")
```

(ref_output_bus1)=
### ref_output_bus1

When set to ``True``, sizes and costs the link based on power at the output bus instead of the input bus, useful for asymmetric efficiencies.

```python
network.add("Link", "example_link", bus0="b0", bus1="b1", ref_output_bus1=True)
```
