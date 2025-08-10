"""
Data processing utilities for cleaning and transforming data.
"""

import re
from typing import List, Dict, Any, Union, Optional, Callable
from collections import Counter


def clean_text(text: str) -> str:
    """
    Clean text by removing extra whitespace and special characters.
    
    Args:
        text (str): Text to clean
        
    Returns:
        str: Cleaned text
        
    Example:
        >>> clean_text("  Hello,   World!  \\n\\t")
        'Hello, World!'
    """
    # Remove extra whitespace and newlines
    cleaned = re.sub(r'\s+', ' ', text.strip())
    return cleaned


def extract_numbers(text: str) -> List[float]:
    """
    Extract all numbers from a text string.
    
    Args:
        text (str): Text to extract numbers from
        
    Returns:
        List[float]: List of extracted numbers
        
    Example:
        >>> extract_numbers("Price: $29.99, Quantity: 5, Tax: 2.5%")
        [29.99, 5, 2.5]
    """
    pattern = r'-?\d+\.?\d*'
    matches = re.findall(pattern, text)
    return [float(match) for match in matches if match]


def extract_emails(text: str) -> List[str]:
    """
    Extract email addresses from text.
    
    Args:
        text (str): Text to extract emails from
        
    Returns:
        List[str]: List of extracted email addresses
        
    Example:
        >>> extract_emails("Contact us at info@example.com or support@test.org")
        ['info@example.com', 'support@test.org']
    """
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.findall(pattern, text)


def normalize_phone_number(phone: str) -> str:
    """
    Normalize phone number format.
    
    Args:
        phone (str): Phone number to normalize
        
    Returns:
        str: Normalized phone number
        
    Example:
        >>> normalize_phone_number("(555) 123-4567")
        '5551234567'
    """
    # Remove all non-digit characters
    digits_only = re.sub(r'\D', '', phone)
    
    # Remove leading 1 if present (US country code)
    if len(digits_only) == 11 and digits_only.startswith('1'):
        digits_only = digits_only[1:]
    
    return digits_only


def remove_outliers(data: List[Union[int, float]], method: str = 'iqr') -> List[Union[int, float]]:
    """
    Remove outliers from a list of numbers.
    
    Args:
        data (List[Union[int, float]]): List of numbers
        method (str): Method to use ('iqr' or 'zscore')
        
    Returns:
        List[Union[int, float]]: List with outliers removed
        
    Example:
        >>> remove_outliers([1, 2, 3, 4, 5, 100])
        [1, 2, 3, 4, 5]
    """
    if method == 'iqr':
        sorted_data = sorted(data)
        n = len(sorted_data)
        
        q1 = sorted_data[n // 4]
        q3 = sorted_data[3 * n // 4]
        iqr = q3 - q1
        
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        
        return [x for x in data if lower_bound <= x <= upper_bound]
    
    elif method == 'zscore':
        mean = sum(data) / len(data)
        variance = sum((x - mean) ** 2 for x in data) / len(data)
        std_dev = variance ** 0.5
        
        return [x for x in data if abs((x - mean) / std_dev) < 3]
    
    else:
        raise ValueError("Method must be 'iqr' or 'zscore'")


def fill_missing_values(data: List[Optional[Union[int, float]]], strategy: str = 'mean') -> List[Union[int, float]]:
    """
    Fill missing values in a list using specified strategy.
    
    Args:
        data (List[Optional[Union[int, float]]]): List with potential None values
        strategy (str): Strategy to use ('mean', 'median', 'mode', 'zero')
        
    Returns:
        List[Union[int, float]]: List with missing values filled
        
    Example:
        >>> fill_missing_values([1, 2, None, 4, None], 'mean')
        [1, 2, 2.33, 4, 2.33]
    """
    # Remove None values for calculation
    valid_values = [x for x in data if x is not None]
    
    if not valid_values:
        return [0] * len(data)
    
    if strategy == 'mean':
        fill_value = sum(valid_values) / len(valid_values)
    elif strategy == 'median':
        sorted_values = sorted(valid_values)
        n = len(sorted_values)
        if n % 2 == 0:
            fill_value = (sorted_values[n//2-1] + sorted_values[n//2]) / 2
        else:
            fill_value = sorted_values[n//2]
    elif strategy == 'mode':
        counter = Counter(valid_values)
        fill_value = counter.most_common(1)[0][0]
    elif strategy == 'zero':
        fill_value = 0
    else:
        raise ValueError("Strategy must be 'mean', 'median', 'mode', or 'zero'")
    
    return [fill_value if x is None else x for x in data]


def normalize_data(data: List[Union[int, float]], method: str = 'min_max') -> List[float]:
    """
    Normalize data using specified method.
    
    Args:
        data (List[Union[int, float]]): Data to normalize
        method (str): Normalization method ('min_max', 'z_score')
        
    Returns:
        List[float]: Normalized data
        
    Example:
        >>> normalize_data([1, 2, 3, 4, 5])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if method == 'min_max':
        min_val = min(data)
        max_val = max(data)
        if max_val == min_val:
            return [0.0] * len(data)
        return [(x - min_val) / (max_val - min_val) for x in data]
    
    elif method == 'z_score':
        mean = sum(data) / len(data)
        variance = sum((x - mean) ** 2 for x in data) / len(data)
        std_dev = variance ** 0.5
        if std_dev == 0:
            return [0.0] * len(data)
        return [(x - mean) / std_dev for x in data]
    
    else:
        raise ValueError("Method must be 'min_max' or 'z_score'")


def group_data(data: List[Dict[str, Any]], key: str) -> Dict[Any, List[Dict[str, Any]]]:
    """
    Group list of dictionaries by a key.
    
    Args:
        data (List[Dict[str, Any]]): Data to group
        key (str): Key to group by
        
    Returns:
        Dict[Any, List[Dict[str, Any]]]: Grouped data
        
    Example:
        >>> data = [{'name': 'Alice', 'dept': 'IT'}, {'name': 'Bob', 'dept': 'IT'}]
        >>> group_data(data, 'dept')
        {'IT': [{'name': 'Alice', 'dept': 'IT'}, {'name': 'Bob', 'dept': 'IT'}]}
    """
    grouped = {}
    for item in data:
        group_key = item.get(key)
        if group_key not in grouped:
            grouped[group_key] = []
        grouped[group_key].append(item)
    return grouped


def filter_data(data: List[Dict[str, Any]], condition: Callable[[Dict[str, Any]], bool]) -> List[Dict[str, Any]]:
    """
    Filter list of dictionaries based on a condition function.
    
    Args:
        data (List[Dict[str, Any]]): Data to filter
        condition (Callable): Function that takes a dict and returns bool
        
    Returns:
        List[Dict[str, Any]]: Filtered data
        
    Example:
        >>> data = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]
        >>> filter_data(data, lambda x: x['age'] > 27)
        [{'name': 'Alice', 'age': 30}]
    """
    return [item for item in data if condition(item)]


def sort_data(data: List[Dict[str, Any]], key: str, reverse: bool = False) -> List[Dict[str, Any]]:
    """
    Sort list of dictionaries by a key.
    
    Args:
        data (List[Dict[str, Any]]): Data to sort
        key (str): Key to sort by
        reverse (bool): Sort in descending order if True
        
    Returns:
        List[Dict[str, Any]]: Sorted data
        
    Example:
        >>> data = [{'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}]
        >>> sort_data(data, 'age')
        [{'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}]
    """
    return sorted(data, key=lambda x: x.get(key, 0), reverse=reverse)


def calculate_statistics(data: List[Union[int, float]]) -> Dict[str, float]:
    """
    Calculate basic statistics for a list of numbers.
    
    Args:
        data (List[Union[int, float]]): List of numbers
        
    Returns:
        Dict[str, float]: Dictionary with statistics
        
    Example:
        >>> calculate_statistics([1, 2, 3, 4, 5])
        {'mean': 3.0, 'median': 3.0, 'std': 1.58, 'min': 1, 'max': 5}
    """
    if not data:
        return {}
    
    sorted_data = sorted(data)
    n = len(sorted_data)
    
    # Mean
    mean = sum(data) / n
    
    # Median
    if n % 2 == 0:
        median = (sorted_data[n//2-1] + sorted_data[n//2]) / 2
    else:
        median = sorted_data[n//2]
    
    # Standard deviation
    variance = sum((x - mean) ** 2 for x in data) / n
    std_dev = variance ** 0.5
    
    return {
        'mean': round(mean, 2),
        'median': median,
        'std': round(std_dev, 2),
        'min': min(data),
        'max': max(data),
        'count': n
    }
