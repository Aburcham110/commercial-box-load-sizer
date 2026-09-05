"""Approximate educational presets for walk-in box-load sizing."""

from __future__ import annotations

from typing import Any, Dict

DISCLAIMER = (
    "EDUCATIONAL ONLY — not for stamped bids or equipment selection.\n"
    "Use manufacturer software and ASHRAE methods for real design work.\n"
    "All factors are approximate practice values, not certified data."
)

BOX_TYPES: Dict[str, Dict[str, Any]] = {
    "cooler": {"target_f": 35.0, "label": "Cooler (~35°F)"},
    "freezer": {"target_f": -10.0, "label": "Freezer (~−10°F)"},
    "custom": {"target_f": None, "label": "Custom target °F"},
}

INSULATION_PRESETS: Dict[str, Dict[str, Any]] = {
    "cooler-4in-foam": {"r": 28.0, "label": "4\" foam cooler panel (~R-28)"},
    "freezer-5in-foam": {"r": 35.0, "label": "5\" foam freezer panel (~R-35)"},
    "freezer-6in-foam": {"r": 42.0, "label": "6\" foam freezer panel (~R-42)"},
    "thin-2in": {"r": 14.0, "label": "2\" foam (~R-14)"},
}

FLOOR_PRESETS: Dict[str, Dict[str, Any]] = {
    "insulated": {"r": 28.0, "label": "Insulated floor (same class as walls)"},
    "on-grade": {"r": 8.0, "label": "On-grade / lightly insulated (~R-8 effective)"},
    "none": {"r": 9999.0, "label": "Ignore floor transmission"},
}

USAGE_PRESETS: Dict[str, Dict[str, Any]] = {
    "light": {"openings_day": 20, "acpd": 4.0, "label": "Light traffic"},
    "medium": {"openings_day": 50, "acpd": 8.0, "label": "Medium traffic"},
    "heavy": {"openings_day": 100, "acpd": 14.0, "label": "Heavy traffic"},
}

PRODUCT_PRESETS: Dict[str, Dict[str, Any]] = {
    "packaged-meat": {"cp": 0.75, "latent": 0.0, "resp_day": 0.0, "label": "Packaged meat"},
    "produce": {"cp": 0.90, "latent": 0.0, "resp_day": 40.0, "label": "Produce (higher respiration)"},
    "dairy": {"cp": 0.90, "latent": 0.0, "resp_day": 5.0, "label": "Dairy"},
    "frozen-food": {"cp": 0.45, "latent": 144.0, "resp_day": 0.0, "label": "Frozen food"},
    "beverage": {"cp": 1.00, "latent": 0.0, "resp_day": 0.0, "label": "Beverage"},
    "custom": {"cp": 0.80, "latent": 0.0, "resp_day": 0.0, "label": "Custom (default cp)"},
}

DEFROST_TYPES = ("electric", "hot-gas", "none")
W_TO_BTU_HR = 3.412
