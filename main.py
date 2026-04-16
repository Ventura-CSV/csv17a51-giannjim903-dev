from __future__ import annotations


def get_domain(mapping: dict) -> set:
    """Return the domain X (all inputs of the function)."""
    return set(mapping.keys())
   

    # === END TODO ===


def get_range(mapping: dict) -> set:
    """Return the range — the set of outputs actually mapped to."""
    return set(mapping.values())
    
    # === END TODO ===


def is_well_defined(mapping: dict, target: set) -> bool:
    """Return True if every output value is in the target set."""
    return all(value in target for value in mapping.values())
    # === END TODO ===


def is_injective(mapping: dict) -> bool:
    """Return True if f is one-to-one (no two inputs map to same output)."""
   return len(mapping.values()) == len(set(mapping.values()))
    # === END TODO ===


def is_surjective(mapping: dict, target: set) -> bool:
    """Return True if f is onto (range == target)."""
   return set(mapping.values()) == target
    # === END TODO ===


def is_bijective(mapping: dict, target: set) -> bool:
    """Return True if f is both injective and surjective."""
    return is_inejective(mapping) and is_surjective(mapping, target)
