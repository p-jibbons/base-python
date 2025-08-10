"""
Dictionary manipulation functions for common operations.
"""

from typing import Dict, Any, List, Union


def merge_dicts(*dicts: Dict[Any, Any]) -> Dict[Any, Any]:
    """
    Merge multiple dictionaries into one.
    
    Args:
        *dicts: Variable number of dictionaries to merge
        
    Returns:
        Dict[Any, Any]: Merged dictionary
        
    Example:
        >>> merge_dicts({'a': 1}, {'b': 2}, {'c': 3})
        {'a': 1, 'b': 2, 'c': 3}
    """
    result = {}
    for d in dicts:
        result.update(d)
    return result


def invert_dict(d: Dict[Any, Any]) -> Dict[Any, Any]:
    """
    Invert a dictionary (keys become values, values become keys).
    
    Args:
        d (Dict[Any, Any]): Dictionary to invert
        
    Returns:
        Dict[Any, Any]: Inverted dictionary
        
    Example:
        >>> invert_dict({'a': 1, 'b': 2})
        {1: 'a', 2: 'b'}
    """
    return {value: key for key, value in d.items()}


def filter_dict_by_value(d: Dict[Any, Any], condition) -> Dict[Any, Any]:
    """
    Filter dictionary by values using a condition function.
    
    Args:
        d (Dict[Any, Any]): Dictionary to filter
        condition: Function that takes a value and returns bool
        
    Returns:
        Dict[Any, Any]: Filtered dictionary
        
    Example:
        >>> filter_dict_by_value({'a': 1, 'b': 2, 'c': 3}, lambda x: x > 1)
        {'b': 2, 'c': 3}
    """
    return {key: value for key, value in d.items() if condition(value)}


def get_nested_value(d: Dict[Any, Any], keys: List[Any], default=None) -> Any:
    """
    Get value from nested dictionary using a list of keys.
    
    Args:
        d (Dict[Any, Any]): The dictionary to search
        keys (List[Any]): List of keys representing the path
        default: Default value if key path doesn't exist
        
    Returns:
        Any: The value at the key path or default
        
    Example:
        >>> get_nested_value({'a': {'b': {'c': 1}}}, ['a', 'b', 'c'])
        1
    """
    current = d
    try:
        for key in keys:
            current = current[key]
        return current
    except (KeyError, TypeError):
        return default


def set_nested_value(d: Dict[Any, Any], keys: List[Any], value: Any) -> None:
    """
    Set value in nested dictionary using a list of keys.
    
    Args:
        d (Dict[Any, Any]): The dictionary to modify
        keys (List[Any]): List of keys representing the path
        value (Any): Value to set
        
    Example:
        >>> d = {}
        >>> set_nested_value(d, ['a', 'b', 'c'], 1)
        >>> d
        {'a': {'b': {'c': 1}}}
    """
    current = d
    for key in keys[:-1]:
        if key not in current or not isinstance(current[key], dict):
            current[key] = {}
        current = current[key]
    current[keys[-1]] = value


def flatten_dict(d: Dict[Any, Any], separator: str = '.') -> Dict[str, Any]:
    """
    Flatten a nested dictionary.
    
    Args:
        d (Dict[Any, Any]): Dictionary to flatten
        separator (str): Separator for nested keys
        
    Returns:
        Dict[str, Any]: Flattened dictionary
        
    Example:
        >>> flatten_dict({'a': {'b': {'c': 1}, 'd': 2}})
        {'a.b.c': 1, 'a.d': 2}
    """
    def _flatten(obj, parent_key=''):
        items = []
        if isinstance(obj, dict):
            for key, value in obj.items():
                new_key = f"{parent_key}{separator}{key}" if parent_key else key
                items.extend(_flatten(value, new_key).items())
        else:
            return {parent_key: obj}
        return dict(items)
    
    return _flatten(d)


def group_by_key(items: List[Dict[Any, Any]], key: Any) -> Dict[Any, List[Dict[Any, Any]]]:
    """
    Group list of dictionaries by a specific key.
    
    Args:
        items (List[Dict[Any, Any]]): List of dictionaries
        key (Any): Key to group by
        
    Returns:
        Dict[Any, List[Dict[Any, Any]]]: Grouped dictionaries
        
    Example:
        >>> items = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 25}]
        >>> group_by_key(items, 'age')
        {25: [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 25}]}
    """
    grouped = {}
    for item in items:
        group_key = item.get(key)
        if group_key not in grouped:
            grouped[group_key] = []
        grouped[group_key].append(item)
    return grouped


def dict_diff(dict1: Dict[Any, Any], dict2: Dict[Any, Any]) -> Dict[str, Dict[Any, Any]]:
    """
    Find differences between two dictionaries.
    
    Args:
        dict1 (Dict[Any, Any]): First dictionary
        dict2 (Dict[Any, Any]): Second dictionary
        
    Returns:
        Dict[str, Dict[Any, Any]]: Dictionary with 'added', 'removed', 'changed' keys
        
    Example:
        >>> dict_diff({'a': 1, 'b': 2}, {'a': 1, 'c': 3})
        {'added': {'c': 3}, 'removed': {'b': 2}, 'changed': {}}
    """
    added = {k: v for k, v in dict2.items() if k not in dict1}
    removed = {k: v for k, v in dict1.items() if k not in dict2}
    changed = {k: {'old': dict1[k], 'new': dict2[k]} 
               for k in dict1 if k in dict2 and dict1[k] != dict2[k]}
    
    return {'added': added, 'removed': removed, 'changed': changed}
