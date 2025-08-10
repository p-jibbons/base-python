"""
General utility functions that don't fit in other categories.
"""

import time
import random
import string
from typing import Any, List, Callable, TypeVar, Optional, Dict
from functools import wraps


T = TypeVar('T')


def timer(func: Callable) -> Callable:
    """
    Decorator to measure function execution time.
    
    Args:
        func (Callable): Function to time
        
    Returns:
        Callable: Wrapped function that prints execution time
        
    Example:
        >>> @timer
        ... def slow_function():
        ...     time.sleep(1)
        >>> slow_function()
        Function 'slow_function' took 1.001 seconds to execute
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function '{func.__name__}' took {end_time - start_time:.3f} seconds to execute")
        return result
    return wrapper


def retry(max_attempts: int = 3, delay: float = 1.0):
    """
    Decorator to retry function execution on failure.
    
    Args:
        max_attempts (int): Maximum number of attempts
        delay (float): Delay between attempts in seconds
        
    Returns:
        Callable: Decorated function
        
    Example:
        >>> @retry(max_attempts=3, delay=0.5)
        ... def unreliable_function():
        ...     if random.random() < 0.7:
        ...         raise Exception("Random failure")
        ...     return "Success"
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise e
                    print(f"Attempt {attempt + 1} failed: {e}. Retrying in {delay} seconds...")
                    time.sleep(delay)
            return None
        return wrapper
    return decorator


def generate_random_string(length: int = 10, include_digits: bool = True, include_symbols: bool = False) -> str:
    """
    Generate a random string with specified parameters.
    
    Args:
        length (int): Length of the string
        include_digits (bool): Include digits in the string
        include_symbols (bool): Include symbols in the string
        
    Returns:
        str: Random string
        
    Example:
        >>> random_str = generate_random_string(8, True, False)
        >>> len(random_str)
        8
    """
    chars = string.ascii_letters
    if include_digits:
        chars += string.digits
    if include_symbols:
        chars += string.punctuation
    
    return ''.join(random.choice(chars) for _ in range(length))


def chunk_iterable(iterable: List[T], chunk_size: int) -> List[List[T]]:
    """
    Split an iterable into chunks of specified size.
    
    Args:
        iterable (List[T]): Iterable to chunk
        chunk_size (int): Size of each chunk
        
    Returns:
        List[List[T]]: List of chunks
        
    Example:
        >>> chunk_iterable([1, 2, 3, 4, 5, 6, 7], 3)
        [[1, 2, 3], [4, 5, 6], [7]]
    """
    return [iterable[i:i + chunk_size] for i in range(0, len(iterable), chunk_size)]


def memoize(func: Callable) -> Callable:
    """
    Decorator to cache function results (memoization).
    
    Args:
        func (Callable): Function to memoize
        
    Returns:
        Callable: Memoized function
        
    Example:
        >>> @memoize
        ... def expensive_calculation(n):
        ...     time.sleep(1)  # Simulate expensive operation
        ...     return n * n
    """
    cache = {}
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Create a key from args and kwargs
        key = str(args) + str(sorted(kwargs.items()))
        
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    
    return wrapper


def deep_get(data: Dict[str, Any], keys: str, default: Any = None, separator: str = '.') -> Any:
    """
    Get nested dictionary value using dot notation.
    
    Args:
        data (Dict[str, Any]): Dictionary to search
        keys (str): Dot-separated keys (e.g., 'user.address.city')
        default (Any): Default value if key not found
        separator (str): Key separator (default: '.')
        
    Returns:
        Any: Value at the key path or default
        
    Example:
        >>> data = {'user': {'address': {'city': 'New York'}}}
        >>> deep_get(data, 'user.address.city')
        'New York'
    """
    keys_list = keys.split(separator)
    current = data
    
    try:
        for key in keys_list:
            current = current[key]
        return current
    except (KeyError, TypeError):
        return default


def validate_email(email: str) -> bool:
    """
    Basic email validation.
    
    Args:
        email (str): Email address to validate
        
    Returns:
        bool: True if valid format, False otherwise
        
    Example:
        >>> validate_email('user@example.com')
        True
    """
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def clamp(value: float, min_value: float, max_value: float) -> float:
    """
    Clamp a value between min and max bounds.
    
    Args:
        value (float): Value to clamp
        min_value (float): Minimum bound
        max_value (float): Maximum bound
        
    Returns:
        float: Clamped value
        
    Example:
        >>> clamp(15, 0, 10)
        10
    """
    return max(min_value, min(value, max_value))


def safe_divide(a: float, b: float, default: float = 0.0) -> float:
    """
    Safely divide two numbers, returning default if division by zero.
    
    Args:
        a (float): Numerator
        b (float): Denominator
        default (float): Default value for division by zero
        
    Returns:
        float: Result of division or default
        
    Example:
        >>> safe_divide(10, 2)
        5.0
        >>> safe_divide(10, 0)
        0.0
    """
    try:
        return a / b
    except ZeroDivisionError:
        return default


def get_class_name(obj: Any) -> str:
    """
    Get the class name of an object.
    
    Args:
        obj (Any): Object to get class name for
        
    Returns:
        str: Class name
        
    Example:
        >>> get_class_name([1, 2, 3])
        'list'
    """
    return obj.__class__.__name__


def is_iterable(obj: Any) -> bool:
    """
    Check if an object is iterable.
    
    Args:
        obj (Any): Object to check
        
    Returns:
        bool: True if iterable, False otherwise
        
    Example:
        >>> is_iterable([1, 2, 3])
        True
        >>> is_iterable(42)
        False
    """
    try:
        iter(obj)
        return True
    except TypeError:
        return False
