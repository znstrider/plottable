from typing import Any, Dict


def replace_lw_key(d) -> Dict[str, Any]:
    """Replaces the "lw" key in a Dictionary with "linewidth"."""
    if "lw" in d:
        d["linewidth"] = d.pop("lw")
    return d
