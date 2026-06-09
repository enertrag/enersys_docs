# Components

This section lists the available components in Enersys. Each table shows the standard PyPSA parameters and additional Enersys-specific parameters. The "Source" column indicates whether a parameter comes from PyPSA or Enersys. The "Can introduce binary variables?" column highlights parameters that can turn the optimisation into a mixed-integer problem and therefore may increase solve time.

## Bus

| Parameter | Type | Unit | Default | Description | Can introduce binary variables? | Source |
|-----------|------|------|---------|-------------|---------------------------------|--------|
| name | string |  |  | Unique name of the bus | No | PyPSA |
| v_nom | float | kV | 0 | Nominal voltage magnitude | No | PyPSA |
| type | string |  | "" | Network type (AC or DC) | No | PyPSA |
| v_mag_pu_set | float | p.u. | 1.0 | Voltage magnitude setpoint | No | PyPSA |
| v_ang_set | float | degrees | 0 | Voltage angle setpoint | No | PyPSA |
| v_mag_pu_min | float | p.u. | 0 | Minimum voltage magnitude | No | PyPSA |
| v_mag_pu_max | float | p.u. | inf | Maximum voltage magnitude | No | PyPSA |
| p_set | float | MW | 0 | Active power injection | No | PyPSA |
| q_set | float | Mvar | 0 | Reactive power injection | No | PyPSA |
| carrier | string |  | "" | Carrier of the bus | No | PyPSA |
| unit | string |  | "" | Unit of the carrier | No | PyPSA |
| sub_network | string |  | "" | Sub-network identifier | No | PyPSA |
| x | float | degrees | NaN | X-position (longitude) | No | PyPSA |
| y | float | degrees | NaN | Y-position (latitude) | No | PyPSA |
| [color](#color) | string |  | "" | Optional bus colour for visualisation (e.g. Sankey plots) | No | Enersys |

## Generator

| Parameter | Type | Unit | Default | Description | Can introduce binary variables? | Source |
|-----------|------|------|---------|-------------|---------------------------------|--------|
| bus | string |  |  | Connected bus | No | PyPSA |
| p_nom | float | MW | 0 | Nominal power | No | PyPSA |
| p_nom_extendable | bool |  | False | Allow capacity expansion | No | PyPSA |
| committable | bool |  | False | Apply unit commitment constraints; only possible with `p_nom_extendable=False` | Yes, for unit commitment | PyPSA |
| start_up_cost | float | currency | 0.0 | Cost to start up the generator; only used if `committable=True` | Only with `committable=True` | PyPSA |
| shut_down_cost | float | currency | 0.0 | Cost to shut down the generator; only used if `committable=True` | Only with `committable=True` | PyPSA |
| min_up_time | int | snapshots | 0 | Minimum number of snapshots the generator must stay online; only used if `committable=True` | Only with `committable=True` | PyPSA |
| min_down_time | int | snapshots | 0 | Minimum number of snapshots the generator must stay offline; only used if `committable=True` | Only with `committable=True` | PyPSA |
| up_time_before | int | snapshots | 1 | Number of snapshots the generator was online before the model horizon; only used with `committable=True` and `min_up_time>0` | Only with `committable=True` | PyPSA |
| down_time_before | int | snapshots | 0 | Number of snapshots the generator was offline before the model horizon; only used with `committable=True` and `min_down_time>0` | Only with `committable=True` | PyPSA |
| ramp_limit_up | float/series | p.u. | NaN | Maximum active power increase between snapshots per unit of nominal power | No | PyPSA |
| ramp_limit_down | float/series | p.u. | NaN | Maximum active power decrease between snapshots per unit of nominal power | No | PyPSA |
| ramp_limit_start_up | float | p.u. | 1.0 | Maximum active power increase at start-up per unit of nominal power; only used if `committable=True` | Only with `committable=True` | PyPSA |
| ramp_limit_shut_down | float | p.u. | 1.0 | Maximum active power decrease at shut-down per unit of nominal power; only used if `committable=True` | Only with `committable=True` | PyPSA |
| [p_nom_must_extend](#p_nom_must_extend) | bool |  | False | Like p_nom_extendable but prevents capacity fixing by `modify_by_network` | No | Enersys |
| p_nom_min | float | MW | 0 | Minimum expandable capacity | No | PyPSA |
| p_nom_max | float | MW | inf | Maximum expandable capacity | No | PyPSA |
| p_set | float | MW | 0 | Dispatch power | No | PyPSA |
| p_min_pu | float | p.u. | 0 | Minimum output per unit | No | PyPSA |
| p_max_pu | float | p.u. | 1 | Maximum output per unit | No | PyPSA |
| efficiency | float | p.u. | 1 | Conversion efficiency | No | PyPSA |
| marginal_cost | float | currency/MWh | 0 | Variable costs | No | PyPSA |
| capital_cost | float | currency/MW | 0 | Annualized capital costs | No | PyPSA |
| build_year | int | year | 0 | First year available | No | PyPSA |
| lifetime | float | years | inf | Economic lifetime | No | PyPSA |
| carrier | string |  | "" | Carrier of the generator | No | PyPSA |
| type | string |  | "" | Technology type | No | PyPSA |
| x | float | degrees | NaN | X-position (longitude) | No | PyPSA |
| y | float | degrees | NaN | Y-position (latitude) | No | PyPSA |
| [marker](#marker) | string |  | "o" | Optional plotting symbol | No | Enersys |
| [invest_cost](#invest_cost) | float | EUR/MW | NaN | Specific investment costs (CAPEX) | No | Enersys |
| [fixed_invest_cost](#fixed_invest_cost) | float | EUR | NaN | One-time fixed investment costs included in optimisation | Yes, for optional extendable components | Enersys |
| [fixed_invest_cost_post_opt](#fixed_invest_cost_post_opt) | float | EUR | NaN | One-time fixed investment costs added only during post-processing | No | Enersys |
| [fo_cost](#fo_cost) | float | EUR/(MW·a) | NaN | Specific fixed operating costs (OPEX) | No | Enersys |
| [invest_cost_scale](#invest_cost_scale) | dict | EUR/MW | NaN | Size-dependent investment cost curves | Yes, for cost segments | Enersys |
| [discount_rate](#discount_rate) | float | p.u. | NaN | Component-specific discount rate overriding network setting | No | Enersys |
| [capex_system_share](#capex_system_share) | float | p.u. | NaN | Share of system CAPEX attributed to this component | No | Enersys |
| [opex_system_share](#opex_system_share) | float | p.u. | NaN | Share of system OPEX attributed to this component | No | Enersys |
| [p_sum_min](#p_sum_min) | float | MWh | NaN | Minimum cumulative active power output | No | Enersys |
| [p_sum_max](#p_sum_max) | float | MWh | NaN | Maximum cumulative active power output | No | Enersys |
| [p_sum_annual_min](#p_sum_annual_min) | float | MWh | NaN | Minimum annual active power output | No | Enersys |
| [p_sum_annual_max](#p_sum_annual_max) | float | MWh | NaN | Maximum annual active power output | No | Enersys |
| [cf_min](#cf_min) | float | p.u. | NaN | Minimum average capacity factor | No | Enersys |
| [cf_max](#cf_max) | float | p.u. | NaN | Maximum average capacity factor | No | Enersys |
| [balancing](#balancing) | string |  | "" | Period over which output must balance (year, month, day, week, hour) | No | Enersys |
| [standby_load](#standby_load) | dict |  | False | Standby load as fraction of p_nom | No | Enersys |

## Load

| Parameter | Type | Unit | Default | Description | Can introduce binary variables? | Source |
|-----------|------|------|---------|-------------|---------------------------------|--------|
| bus | string |  |  | Connected bus | No | PyPSA |
| p_set | float | MW | 0 | Active power demand | No | PyPSA |
| q_set | float | Mvar | 0 | Reactive power demand | No | PyPSA |
| carrier | string |  | "" | Carrier of the load | No | PyPSA |
| sign | int |  | -1 | Sign convention | No | PyPSA |
| type | string |  | "" | Technology type | No | PyPSA |
| [x](#x) | float | degrees | NaN | X-position (longitude) | No | Enersys |
| [y](#y) | float | degrees | NaN | Y-position (latitude) | No | Enersys |
| [marker](#marker) | string |  | "o" | Optional plotting symbol | No | Enersys |

## Link

| Parameter | Type | Unit | Default | Description | Can introduce binary variables? | Source |
|-----------|------|------|---------|-------------|---------------------------------|--------|
| bus0 | string |  |  | Input bus | No | PyPSA |
| bus1 | string |  |  | Output bus | No | PyPSA |
| p_nom | float | MW | 0 | Nominal power | No | PyPSA |
| p_nom_extendable | bool |  | False | Allow capacity expansion | No | PyPSA |
| committable | bool |  | False | Apply unit commitment constraints; only possible with `p_nom_extendable=False` | Yes, for unit commitment | PyPSA |
| start_up_cost | float | currency | 0.0 | Cost to start up the link; only used if `committable=True` | Only with `committable=True` | PyPSA |
| shut_down_cost | float | currency | 0.0 | Cost to shut down the link; only used if `committable=True` | Only with `committable=True` | PyPSA |
| min_up_time | int | snapshots | 0 | Minimum number of snapshots the link must stay online; only used if `committable=True` | Only with `committable=True` | PyPSA |
| min_down_time | int | snapshots | 0 | Minimum number of snapshots the link must stay offline; only used if `committable=True` | Only with `committable=True` | PyPSA |
| up_time_before | int | snapshots | 1 | Number of snapshots the link was online before the model horizon; only used with `committable=True` and `min_up_time>0` | Only with `committable=True` | PyPSA |
| down_time_before | int | snapshots | 0 | Number of snapshots the link was offline before the model horizon; only used with `committable=True` and `min_down_time>0` | Only with `committable=True` | PyPSA |
| ramp_limit_up | float/series | p.u. | NaN | Maximum power increase between snapshots per unit of nominal power | No | PyPSA |
| ramp_limit_down | float/series | p.u. | NaN | Maximum power decrease between snapshots per unit of nominal power | No | PyPSA |
| ramp_limit_start_up | float | p.u. | 1.0 | Maximum power increase at start-up per unit of nominal power; only used if `committable=True` | Only with `committable=True` | PyPSA |
| ramp_limit_shut_down | float | p.u. | 1.0 | Maximum power decrease at shut-down per unit of nominal power; only used if `committable=True` | Only with `committable=True` | PyPSA |
| [p_nom_must_extend](#p_nom_must_extend) | bool |  | False | Like p_nom_extendable but prevents capacity fixing by `modify_by_network` | No | Enersys |
| p_nom_min | float | MW | 0 | Minimum expandable capacity | No | PyPSA |
| p_nom_max | float | MW | inf | Maximum expandable capacity | No | PyPSA |
| p_min_pu | float | p.u. | -inf | Minimum dispatch per unit | No | PyPSA |
| p_max_pu | float | p.u. | inf | Maximum dispatch per unit | No | PyPSA |
| efficiency | float | p.u. | 1 | Efficiency from bus0 to bus1 | No | PyPSA |
| efficiency2 | float | p.u. | 1 | Efficiency from bus1 to bus0 | No | PyPSA |
| marginal_cost | float | currency/MWh | 0 | Variable costs | No | PyPSA |
| capital_cost | float | currency/MW | 0 | Annualized capital costs | No | PyPSA |
| length | float | km | 0 | Physical length of the link | No | PyPSA |
| carrier | string |  | "" | Carrier of the link | No | PyPSA |
| type | string |  | "" | Technology type | No | PyPSA |
| [x](#x) | float | degrees | NaN | X-position (longitude) | No | Enersys |
| [y](#y) | float | degrees | NaN | Y-position (latitude) | No | Enersys |
| [marker](#marker) | string |  | "o" | Optional plotting symbol | No | Enersys |
| [invest_cost](#invest_cost) | float | EUR/MW | NaN | Specific investment costs (CAPEX) | No | Enersys |
| [fixed_invest_cost](#fixed_invest_cost) | float | EUR | NaN | One-time fixed investment costs included in optimisation | Yes, for optional extendable components | Enersys |
| [fixed_invest_cost_post_opt](#fixed_invest_cost_post_opt) | float | EUR | NaN | One-time fixed investment costs added only during post-processing | No | Enersys |
| [fo_cost](#fo_cost) | float | EUR/(MW·a) | NaN | Specific fixed operating costs (OPEX) | No | Enersys |
| [invest_cost_scale](#invest_cost_scale) | dict | EUR/MW | NaN | Size-dependent investment cost curves | Yes, for cost segments | Enersys |
| [discount_rate](#discount_rate) | float | p.u. | NaN | Component-specific discount rate overriding network setting | No | Enersys |
| [capex_system_share](#capex_system_share) | float | p.u. | NaN | Share of system CAPEX attributed to this component | No | Enersys |
| [opex_system_share](#opex_system_share) | float | p.u. | NaN | Share of system OPEX attributed to this component | No | Enersys |
| [p_sum_min](#p_sum_min) | float | MWh | NaN | Minimum cumulative active power output | No | Enersys |
| [p_sum_max](#p_sum_max) | float | MWh | NaN | Maximum cumulative active power output | No | Enersys |
| [p_sum_annual_min](#p_sum_annual_min) | float | MWh | NaN | Minimum annual active power output | No | Enersys |
| [p_sum_annual_max](#p_sum_annual_max) | float | MWh | NaN | Maximum annual active power output | No | Enersys |
| [cf_min](#cf_min) | float | p.u. | NaN | Minimum average capacity factor | No | Enersys |
| [cf_max](#cf_max) | float | p.u. | NaN | Maximum average capacity factor | No | Enersys |
| [balancing](#balancing) | string |  | "" | Period over which flows must balance (year, month, day, week, hour) | No | Enersys |
| [ref_output_bus1](#ref_output_bus1) | bool |  | False | Use output bus power for sizing and costs | No | Enersys |
| [standby_load](#standby_load) | dict |  | False | Standby load as fraction of p_nom | No | Enersys |

## StorageUnit

| Parameter | Type | Unit | Default | Description | Can introduce binary variables? | Source |
|-----------|------|------|---------|-------------|---------------------------------|--------|
| bus | string |  |  | Connected bus | No | PyPSA |
| [bus](#bus) | list |  |  | multi-bus connection | No | enersys |
| p_nom | float | MW | 0 | Nominal power | No | PyPSA |
| p_nom_extendable | bool |  | False | Allow capacity expansion | No | PyPSA |
| [p_nom_must_extend](#p_nom_must_extend) | bool |  | False | Like p_nom_extendable but prevents capacity fixing by `modify_by_network` | No | Enersys |
| p_nom_min | float | MW | 0 | Minimum expandable capacity | No | PyPSA |
| p_nom_max | float | MW | inf | Maximum expandable capacity | No | PyPSA |
| p_min_pu | float | p.u. | -inf | Minimum dispatch per unit | No | PyPSA |
| p_max_pu | float | p.u. | inf | Maximum dispatch per unit | No | PyPSA |
| max_hours | float | h | 1 | Storage capacity relative to power | No | PyPSA |
| efficiency_store | float | p.u. | 1 | Charging efficiency | No | PyPSA |
| efficiency_dispatch | float | p.u. | 1 | Discharging efficiency | No | PyPSA |
| standing_loss | float | p.u./h | 0 | Hourly standing loss | No | PyPSA |
| inflow | series | MW | 0 | Inflow profile | No | PyPSA |
| state_of_charge_initial | float | MWh | 0 | Initial state of charge | No | PyPSA |
| state_of_charge_set | float | MWh | NaN | Fixed state of charge | No | PyPSA |
| cyclic_state_of_charge | bool |  | False | Enforce cyclical state of charge | No | PyPSA |
| marginal_cost | float | currency/MWh | 0 | Variable costs | No | PyPSA |
| capital_cost | float | currency/MW | 0 | Annualized capital costs | No | PyPSA |
| build_year | int | year | 0 | First year available | No | PyPSA |
| lifetime | float | years | inf | Economic lifetime | No | PyPSA |
| carrier | string |  | "" | Carrier of the unit | No | PyPSA |
| [x](#x) | float | degrees | NaN | X-position (longitude) | No | Enersys |
| [y](#y) | float | degrees | NaN | Y-position (latitude) | No | Enersys |
| [marker](#marker) | string |  | "o" | Optional plotting symbol | No | Enersys |
| [invest_cost](#invest_cost) | float | EUR/MW | NaN | Specific investment costs (CAPEX) | No | Enersys |
| [fixed_invest_cost](#fixed_invest_cost) | float | EUR | NaN | One-time fixed investment costs included in optimisation | Yes, for optional extendable components | Enersys |
| [fixed_invest_cost_post_opt](#fixed_invest_cost_post_opt) | float | EUR | NaN | One-time fixed investment costs added only during post-processing | No | Enersys |
| [fo_cost](#fo_cost) | float | EUR/(MW·a) | NaN | Specific fixed operating costs (OPEX) | No | Enersys |
| [invest_cost_scale](#invest_cost_scale) | dict | EUR/MW | NaN | Size-dependent investment cost curves | Yes, for cost segments | Enersys |
| [discount_rate](#discount_rate) | float | p.u. | NaN | Component-specific discount rate overriding network setting | No | Enersys |
| [capex_system_share](#capex_system_share) | float | p.u. | NaN | Share of system CAPEX attributed to this component | No | Enersys |
| [opex_system_share](#opex_system_share) | float | p.u. | NaN | Share of system OPEX attributed to this component | No | Enersys |
| [p_sum_min](#p_sum_min) | float | MWh | NaN | Minimum cumulative active power output | No | Enersys |
| [p_sum_max](#p_sum_max) | float | MWh | NaN | Maximum cumulative active power output | No | Enersys |
| [p_sum_annual_min](#p_sum_annual_min) | float | MWh | NaN | Minimum annual active power output | No | Enersys |
| [p_sum_annual_max](#p_sum_annual_max) | float | MWh | NaN | Maximum annual active power output | No | Enersys |
| [cf_min](#cf_min) | float | p.u. | NaN | Minimum average capacity factor | No | Enersys |
| [cf_max](#cf_max) | float | p.u. | NaN | Maximum average capacity factor | No | Enersys |
| [share_usable_capacity](#share_usable_capacity) | float/series | p.u. | NaN | Share of storage energy capacity that may be used | No | Enersys |
| [standby_load](#standby_load) | dict |  | False | Standby load as fraction of p_nom | No | Enersys |


## Enersys-specific parameter examples

(bus)=
### bus

Multi-bus option for storage units will connect one storage to multiple buses. Energy charged on one bus can only be
discharged to the same bus. Internally, one storage unit is created for each bus, multiple buses will appear in the
output files.

```python
network.add("StorageUnit", "storage_multibus", bus=["b_electricity_green", "b_electricity_grey", ...)
```

(color)=
### color

Defines an optional colour for buses that is used by visualisation tools such as Sankey plots.

```python
network.add("Bus", "example_bus", color="#4477AA")
```

(marker)=
### marker

Defines the plotting symbol used when visualising network components, allowing custom markers on maps and diagrams.

```python
network.add("Generator", "example_gen", bus="bus0", marker="s")
```

(p_nom_must_extend)=
### p_nom_must_extend

Keeps a component expandable even when a reference network is later applied with `Network.modify_by_network`. Use it for
capacities that must remain optimisation variables in follow-up scenarios. It is available on `Generator`, `Link`, and
`StorageUnit` components.

```python
network.add(
    "Generator",
    "wind park",
    bus="bus0",
    p_nom_extendable=True,
    p_nom_must_extend=True,
)
```

(invest_cost)=
### invest_cost

Specifies the specific investment costs (CAPEX) per unit of nominal power. These costs are used in optimisation to value
new capacity [EUR/MW].

```python
network.add("Generator", "example_gen", bus="bus0", invest_cost=750000)
```

(fixed_invest_cost)=
### fixed_invest_cost

Specifies a one-time fixed investment cost in EUR for a component. Unlike `invest_cost`, this cost is independent of the
chosen capacity size and applies when the installed capacity is greater than zero. For extendable components, Enersys adds
the corresponding optimisation constraint so the fixed CAPEX is only charged when the component is built. This can
introduce a binary build variable for each optional extendable component using `fixed_invest_cost`. Binary variables turn
the optimisation into a mixed-integer problem; using `fixed_invest_cost` on many components can slow simulations down
massively. For fixed non-extendable components with `p_nom > 0`, the cost is converted into the component's annualized
`capital_cost`.

`discount_rate` and `lifetime` must be available either on the network or on the component so Enersys can annualize the
fixed amount.

```python
network.add(
    "Generator",
    "backup boiler",
    bus="heat bus",
    p_nom_extendable=True,
    p_nom_max=20,
    fixed_invest_cost=100_000,
    lifetime=20,
    discount_rate=0.06,
)
```

(fixed_invest_cost_post_opt)=
### fixed_invest_cost_post_opt

Adds a one-time fixed investment cost in EUR only after the optimisation has finished. This is useful for reporting costs
that should appear in CAPEX and OPEX outputs but should not influence the investment or dispatch decision. The cost is
applied during post-processing when the optimized capacity is greater than zero and also requires `discount_rate` and
`lifetime` for annualization.

```python
network.add(
    "Generator",
    "optional reporting item",
    bus="bus0",
    p_nom_extendable=True,
    fixed_invest_cost_post_opt=50_000,
    lifetime=20,
    discount_rate=0.06,
)
```

(fo_cost)=
### fo_cost

Defines the specific fixed operating costs (OPEX) per unit of nominal power and year, representing annual operation and
maintenance expenses [EUR/(MW*a)].

```python
network.add("Generator", "example_gen", bus="bus0", fo_cost=5000)
```

(invest_cost_scale)=
### invest_cost_scale

Provides a size-dependent investment cost curve. The parameter is a dictionary, where the keys are
the lower capacity boundary of a cost interval, and the value are the specific costs of that interval.

E.g. the parameter dictionary `invest_cost_scale={0: 200, 10: 150, 30: 100}` means that the costs for the first interval
0 - 10 MW are 200 EUR/MW. Then for the second interval 10 - 30 MW the costs are 150 EUR/MW. And for every MW installed
above 30 MW the costs are 100 EUR/MW.

In this example if e.g. a component of size 50 MW would be build, the actual specific costs would be
for interval 1 the full 10 MW at 200 EUR/MW -> 2000 EUR, for interval 2 the full 20 MW at  150 EUR/MW -> 3000 EUR and
then for the last interval 20 MW at 100 EUR/MW -> 2000 EUR.

This results in (2000 EUR + 3000 EUR + 2000 EUR) / 50 MW --> 140 EUR/MW

```python
network.add("Generator", "example_gen", bus="bus0", invest_cost_scale={0: 200, 10: 150, 30: 100})
```

(discount_rate)=
### discount_rate

Sets a component-specific discount rate. If set, this value overrides the network-wide `discount_rate` for CAPEX/OPEX
annuity calculations of that component.

```python
network.add("Generator", "example_gen", bus="bus0", discount_rate=0.06)
```

(capex_system_share)=
### capex_system_share

Adds a fraction of `invest_cost` as system costs for this component (e.g. 0.2 -> 20 % of invest cost as EUR).

```python
network.add("Generator", "example_gen", bus="bus0", capex_system_share=0.2)
```

(opex_system_share)=
### opex_system_share

Specifies the fraction of `invest_cost` that will be attributed as system OPEX for this component (e.g. 0.02 -> 2 %
of invest cost as EUR/a)

```python
network.add("Generator", "example_gen", bus="bus0", opex_system_share=0.02)
```

(p_sum_min)=
### p_sum_min

Enforces a minimum cumulative energy production over the entire simulation horizon.

```python
network.add("Generator", "example_gen", bus="bus0", p_sum_min=10)
```

(p_sum_max)=
### p_sum_max

Sets a maximum limit on the cumulative energy production over the whole simulation period.

```python
network.add("Generator", "example_gen", bus="bus0", p_sum_max=100)
```

(p_sum_annual_min)=
### p_sum_annual_min

Requires a minimum amount of annual energy to be produced.

```python
network.add("Generator", "example_gen", bus="bus0", p_sum_annual_min=500)
```

(p_sum_annual_max)=
### p_sum_annual_max

Restricts the annual energy production to not exceed a specified value.

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


(share_usable_capacity)=
### share_usable_capacity

Limits the usable energy capacity of a `StorageUnit` without changing its charge or discharge power capacity. The limit
is applied to the state of charge as a share of `p_nom * max_hours`; for example, `0.5` means only half of the
storage energy capacity can be filled. Values must be between 0 and 1.

The parameter can be set as a static value or as a time series to model availability changes over time.

```python
network.add(
    "StorageUnit",
    "battery",
    bus="bus0",
    p_nom=10,
    max_hours=4,
    share_usable_capacity=0.8,
)

network.add(
    "StorageUnit",
    "seasonal_storage",
    bus="bus0",
    p_nom=10,
    max_hours=100,
    share_usable_capacity=pd.Series([0.5, 0.6, 0.8], index=network.snapshots[:3]),
)
```

(standby_load)=
### standby_load

Represents a constant standby consumption as a fraction of nominal power-

```python
network.add("Generator", "example_gen", bus="bus0", standby_load={"bus_electricity": 0.05})
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

Defines the period over which inflows and outflows on a link must balance (such as year, month, week or hour) to model
multi-period constraints.

```python
network.add("Link", "example_link", bus0="b0", bus1="b1", balancing="year")
```

(ref_output_bus1)=
### ref_output_bus1

When set to ``True``, Enersys internally rewrites the link so that sizing and costs reference the original ``bus1``
power instead of the original ``bus0`` power.

This means:

- ``bus0`` and ``bus1`` are swapped internally.
- ``p_min_pu`` and ``p_max_pu`` are swapped and sign-inverted.
- Main efficiency ``efficiency`` is inverted (``1 / efficiency``), so the physical conversion relation stays
  consistent after swapping.
- Additional outputs (``bus2``, ``bus3``, ...) are converted to efficiencies relative to the new reference
  (``-efficiencyN / efficiency``).
- Cost and sizing-related parameters that are tied to link power (e.g. ``p_nom``, ``p_nom_extendable``,
  ``capital_cost``, ``marginal_cost``) are then evaluated on the transformed orientation, which is exactly why they
  effectively reference the original ``bus1`` side when ``ref_output_bus1=True``.
- Because ``standby_load`` is defined as a share of link ``p_nom``, and ``p_nom`` is referenced to the original
  ``bus1`` side when ``ref_output_bus1=True``, the absolute standby-load magnitude is also effectively scaled from
  original ``bus1``-referenced capacity.

As a result, optimized ``p_nom`` and link costs follow the original output side (``bus1``), while conversion
constraints remain physically equivalent.

```python
network.add("Link", "example_link", bus0="b0", bus1="b1", ref_output_bus1=True)
```
