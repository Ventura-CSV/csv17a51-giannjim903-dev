from __future__ import annotations


def get_domain(mapping: dict) -> set:
    """Return the domain X (all inputs of the function)."""
    return set(mapping.keys())
   
    pass
    # === END TODO ===


def get_range(mapping: dict) -> set:
    """Return the range — the set of outputs actually mapped to."""
    return set(mapping.values())
    pass
    # === END TODO ===


def is_well_defined(mapping: dict, target: set) -> bool:
    """Return True if every output value is in the target set."""
    return get_range(mapping).issubset(target)
    pass
    # === END TODO ===


def is_injective(mapping: dict) -> bool:
    """Return True if f is one-to-one (no two inputs map to same output)."""
   return len(get_range(mapping)) == len(mapping)
    pass
    # === END TODO ===


def is_surjective(mapping: dict, target: set) -> bool:
    """Return True if f is onto (range == target)."""
   return get_range(mapping) == target
    pass
    # === END TODO ===


def is_bijective(mapping: dict, target: set) -> bool:
    """Return True if f is both injective and surjective."""
    return is_injective(mapping) and is_surjective(mapping, target)
    pass
    # === END TODO ===
python -m pytest main_test.py -v
pytest
