# Creating and debugging enersys models with Codex

This page explains how to use Codex from VS Code when the actual model project
is outside the enersys repository. It is written for a VS Code multi-root
workspace where one folder is the model project and another folder is a local
checkout of this repository.

## Recommended VS Code workspace layout

Open both folders in the same VS Code window:

```text
enersys-modeling.code-workspace
├── customer-or-study-model/
└── enersys/
```

The model project remains the place where Codex should create or edit model
files. The `enersys/` folder is reference material that Codex can inspect for
package code, component documentation, tests, and templates.

## Make the instructions automatic

The most reliable way to avoid repeating setup prompts is to keep an `AGENTS.md`
file in the model project itself. Codex reads AGENTS instructions from the
workspace tree it is editing, so instructions in the model project are available
automatically when Codex works on those model files.

The `project_template/` folder includes an `AGENTS.md` with the enersys modeling
rules. When starting a new model project, copy the whole template folder,
including `project_template/AGENTS.md`. Then Codex can pick up the rules from the
model project without being reminded at the beginning of every VS Code session.

For existing model projects, copy `project_template/AGENTS.md` into the model
project root or copy the reusable snippet at the bottom of this page. If many
model projects live below one common parent directory, you can place an
`AGENTS.md` in that parent directory so the same instructions apply to all child
projects.

Keeping the instructions in `AGENTS.md` is preferred over relying on VS Code
user settings or Codex extension settings for project-specific behavior. Global
settings are easy to forget, hard to review, and may affect unrelated projects.
Use global settings only for personal defaults; keep enersys modeling rules in
version-controlled `AGENTS.md` files.

When the model project is generated from the template and the enersys repository
is also open as a second VS Code workspace folder, Codex has two useful sources
of context:

- the copied model-project `AGENTS.md`, which applies automatically to model
  files;
- the `enersys/` repository folder, which Codex can inspect for implementation,
  docs, tests, and examples when needed.

## Prompt starter for model creation

Use a prompt like this when asking Codex to create a new model:

```text
We are creating an enersys model in the model project folder of this multi-root
VS Code workspace. Use the enersys repository folder as reference material.

The model project already contains an AGENTS.md copied from the enersys project
template. Follow it. If you need reference material from the enersys repo, use:
- enersys/AGENTS.md
- enersys/docs/components.md
- enersys/project_template/scenario_variation.py
- enersys/docs/codex_modeling.md

Modeling rules:
- Use enersys.Network.
- Use only Bus, Generator, Load, Link, and StorageUnit as physical components.
- Do not add Carrier components or carrier= metadata unless I explicitly ask.
- Do not use Line, Store, Storage, Transformer, ShuntImpedance, or
  GlobalConstraint unless I explicitly ask.
- Prefer a small runnable model script with clear snapshots, units, component
  names, and comments.
- Use human-readable component and carrier names with spaces, for example
  `wind park high voltage` or `wind park hv`, not `wind_park_hv`.
- If I ask for specific KPIs, add them to the standard output txt via
  additional_parameters by default; only create another output file format if I
  explicitly ask.
- After writing the model, run it or run the narrowest available smoke test.
```

## Supported physical component types

When generating enersys models, use the component types documented in
`components.md`:

| Component | Typical use |
|-----------|-------------|
| `Bus` | Location or commodity balance node. |
| `Generator` | Supply, market import/export with signed bounds, fixed time series, or expandable production. |
| `Load` | Fixed demand on a bus. |
| `Link` | Conversion, transport, electrolysis, heat pumps, curtailment sinks, and other directed flows between buses. |
| `StorageUnit` | Batteries, hydrogen storage, and other storage with power and energy capacity coupled through `max_hours`. |

Do not substitute generic PyPSA components such as `Line`, `Store`, `Storage`,
or `Transformer` unless a user explicitly asks for them. For most enersys
studies, use `Link` for transport/conversion and `StorageUnit` for storage.

## Minimal model checklist

A generated model should usually include:

1. Imports for `pandas` and `enersys`.
2. A clear `snapshots = pd.date_range(...)` definition.
3. `n = enersys.Network(snapshots=snapshots, name="...")`.
4. Buses with meaningful names and units. Do not add `Carrier` components or
   `carrier=` metadata unless the user explicitly requests them.
5. Generators, loads, links, and storage units using only supported component
   types.
6. Human-readable component and carrier names with spaces, for example
   `wind park high voltage` or `wind park hv`, not `wind_park_hv`.
7. Time-series data indexed by `snapshots` when a parameter varies over time.
8. A direct runnable entry point guarded by `if __name__ == "__main__":` when
   the file is intended to be executed.
9. A validation action such as `n.optimize()` plus a small result printout or a
   call to `create_txt`/scenario result storage when appropriate.
10. Requested model-specific KPIs written to the standard txt output through
   `additional_parameters`, unless the user explicitly asks for a separate
   output file or export format.

For scenario sweeps, follow the pattern in `project_template/scenario_variation.py`:
write a scenario function that returns an `enersys.Network`, then pass it to
`Scenarios` with `Parameter` definitions.

## Model-specific KPI output

When a user asks Codex to calculate specific KPIs for a model, the default is to
append those KPI values to the normal output txt file. Use
`enersys.post_processing.create_csv.ResultValue` objects and pass them through
`additional_parameters`. For each `ResultValue`, fill either `value` or `info`:
use `value` for numeric KPI values and `info` for non-numeric text. Do not fill
both for the same KPI unless there is an explicit reason.

```python
from enersys.post_processing.create_csv import ResultValue

custom_kpis = [
    ResultValue(
        category="battery full-load hours",
        comp_type="StorageUnit",
        comp_name="battery",
        unit="h/a",
        value=battery_full_load_hours,
    ),
]

n.create_txt(
    file_path="results/1_output.txt",
    additional_parameters=custom_kpis,
    deprecated_layout=False,
)
```

For `Scenarios.create_txt(...)`, pass `additional_parameters` when the same KPI
rows apply to every scenario output. If KPI values must be calculated separately
for each optimized scenario, compute the `ResultValue` list from that scenario's
network before calling `n.create_txt(...)`, for example in a scenario-specific
post-processing step.

Only create new output files, custom CSV/Excel exports, database uploads, or new
post-processing modules when the user explicitly asks for a different output
format, destination, or schema. Otherwise keep custom KPIs in the standard txt
output so downstream tooling sees them together with the normal enersys results.

## Debugging checklist for existing models

When Codex debugs a model, ask it to proceed in this order:

1. Reproduce the failure with the exact command used by the model project.
2. Identify whether the failure happens during import, network construction,
   optimization, post-processing, or result storage.
3. Print or inspect the relevant component tables:
   - `n.buses`
   - `n.generators`
   - `n.loads`
   - `n.links`
   - `n.storage_units`
4. Inspect time-series tables that match the failing component type, for example
   `n.generators_t`, `n.loads_t`, `n.links_t`, and `n.storage_units_t`.
5. Check that all component bus references point to existing buses.
6. Check that all time-series objects use the same index as `n.snapshots`.
7. Check signs and bounds for market exchange, curtailment, and bidirectional
   flows.
8. Check extendable capacity settings (`p_nom_extendable`, `p_nom_min`,
   `p_nom_max`, `p_nom_must_extend`) and cost inputs (`invest_cost`, `fo_cost`,
   `capital_cost`, `marginal_cost`).
9. Make the smallest safe change and rerun the original failing command.
10. Report the command, solver status, and any remaining warnings.

## Useful inspection snippets

These snippets are safe to paste into a temporary debugging cell or script after
`n` has been built:

```python
print("snapshots", n.snapshots[:3], "...", n.snapshots[-3:], len(n.snapshots))
print("buses", n.buses.index.to_list())
print("generators", n.generators[["bus", "p_nom", "p_nom_extendable"]])
print("loads", n.loads[["bus"]])
print("links", n.links[["bus0", "bus1", "p_nom", "p_nom_extendable"]])
print("storage_units", n.storage_units[["bus", "p_nom", "max_hours"]])
```

For bus-reference checks:

```python
bus_names = set(n.buses.index)
for component_name, table, columns in [
    ("Generator", n.generators, ["bus"]),
    ("Load", n.loads, ["bus"]),
    ("Link", n.links, ["bus0", "bus1"]),
    ("StorageUnit", n.storage_units, ["bus"]),
]:
    for column in columns:
        missing = sorted(set(table[column].dropna()) - bus_names)
        if missing:
            print(component_name, column, "missing buses:", missing)
```

## Reusable AGENTS.md snippet for model projects

New projects created from `project_template/` already include these instructions.
Copy this snippet into older model projects that live outside this repository:

```md
# AGENTS.md

## Enersys modeling rules

This project contains enersys model files. When creating, editing, debugging, or
running models:

- Use `enersys.Network`, not raw `pypsa.Network`, unless explicitly requested.
- Use only these physical component types: `Bus`, `Generator`, `Load`, `Link`,
  and `StorageUnit`.
- Do not use PyPSA `Line`, `Store`, `Storage`, `Transformer`, `ShuntImpedance`,
  `GlobalConstraint`, or other physical component types unless explicitly
  requested.
- Do not add `Carrier` components or `carrier=` metadata automatically. Only add
  carriers when explicitly requested.
- Use `Link` for transport/conversion flows and `StorageUnit` for storage.
- Use human-readable component and carrier names with spaces, for example
  `wind park high voltage` or `wind park hv`, not `wind_park_hv`.
- Add requested model-specific KPIs to the standard output txt via
  `additional_parameters` by default. For each `ResultValue`, use `value` for
  numeric KPI values and `info` for non-numeric text; do not fill both unless
  explicitly needed. Create separate output files only when explicitly requested.
- Keep time-series indexes aligned with `n.snapshots`.
- Reproduce failures with the original command before changing code, then rerun
  that command after the fix.
- If an `enersys/` repo folder is open in the same VS Code workspace, consult
  `enersys/AGENTS.md`, `enersys/docs/components.md`,
  `enersys/project_template/scenario_variation.py`, and
  `enersys/docs/codex_modeling.md` before writing model code.
```
