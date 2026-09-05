# Commercial Walk-In Box-Load Sizer (Educational)

Python **stdlib-only** CLI that estimates walk-in **cooler / freezer** refrigeration load and suggests a **rough BTU/hr equipment band**.

> **Educational only — not for stamped bids or final equipment selection.**  
> Use manufacturer selection software and ASHRAE methods for real design work.  
> All heat-gain factors here are approximate practice values.

## What it calculates

| Component | Method (simplified) |
|-----------|---------------------|
| **Transmission** | Steady \(Q = U \times A \times \Delta T\) on walls, ceiling, floor (\(U = 1/R\)) |
| **Infiltration** | Volume × air changes/day → average CFM × \(1.08 \times \Delta T\), plus a rough door-opening bonus |
| **Product** | Sensible pull-down (+ freeze latent / respiration presets where applicable) |
| **Misc** | Lights, people, evaporator fans, electric defrost average |
| **Safety** | User-selectable **10–20%** on subtotal |

## Out of scope (v1)

Glass display cases, blast chillers, CO₂ racks, humidity design, multi-evaporator balance, full psychrometric infiltration.

## Requirements

- Python 3.9+
- No third-party packages

## Quick start

```bash
cd commercial-box-load-sizer
python3 box_load.py --help
python3 box_load.py -i          # interactive
```

### Example — medium-traffic cooler

```bash
python3 box_load.py \
  --length 10 --width 8 --height 8 \
  --box-type cooler \
  --ambient-f 95 \
  --insulation cooler-4in-foam \
  --floor insulated \
  --usage medium \
  --product packaged-meat \
  --product-enter-f 50 \
  --product-lbs-day 500 \
  --lights-w 120 \
  --fans-w 200 \
  --defrost none \
  --safety-pct 15
```

### Example — freezer with electric defrost

```bash
python3 box_load.py \
  --length 12 --width 10 --height 8 \
  --box-type freezer \
  --ambient-f 95 \
  --insulation freezer-5in-foam \
  --floor insulated \
  --usage heavy \
  --product frozen-food \
  --product-enter-f 0 \
  --product-lbs-day 800 \
  --defrost electric \
  --defrost-kw 4 \
  --defrost-hours-day 1.5 \
  --safety-pct 20
```

### Turnover instead of lbs/day

```bash
python3 box_load.py \
  --length 10 --width 8 --height 8 \
  --box-type cooler \
  --product produce \
  --product-enter-f 55 \
  --turnover-pct 10 \
  --safety-pct 15
```

(`turnover-pct` approximates lb/day as `volume_ft³ × 25 × pct/100`.)

## Presets

**Box types:** `cooler` (~35°F), `freezer` (~−10°F), `custom` (pass `--target-f`)

**Insulation:** `cooler-4in-foam`, `freezer-5in-foam`, `freezer-6in-foam`, `thin-2in` (override with `--wall-r` / `--ceiling-r`)

**Floor:** `insulated`, `on-grade`, `none`

**Usage:** `light` / `medium` / `heavy` (sets openings/day + air changes/day; overridable)

**Product:** `packaged-meat`, `produce`, `dairy`, `frozen-food`, `beverage`, `custom`

## Outputs

- BTU/hr by component (transmission, infiltration, product, misc)
- Subtotal, safety factor, **total**
- Rough unit suggestion band (not a model number)
- Hard educational disclaimer on every report
