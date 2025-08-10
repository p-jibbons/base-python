"""
Mathematical functions and calculations.
"""

import math
from typing import List, Union, Tuple


def factorial(n: int) -> int:
    """
    Calculate factorial of a number.
    
    Args:
        n (int): Non-negative integer
        
    Returns:
        int: Factorial of n
        
    Example:
        >>> factorial(5)
        120
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n: int) -> int:
    """
    Calculate the nth Fibonacci number.
    
    Args:
        n (int): Position in Fibonacci sequence (0-indexed)
        
    Returns:
        int: The nth Fibonacci number
        
    Example:
        >>> fibonacci(6)
        8
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def is_prime(n: int) -> bool:
    """
    Check if a number is prime.
    
    Args:
        n (int): Number to check
        
    Returns:
        bool: True if prime, False otherwise
        
    Example:
        >>> is_prime(17)
        True
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def gcd(a: int, b: int) -> int:
    """
    Calculate Greatest Common Divisor using Euclidean algorithm.
    
    Args:
        a (int): First number
        b (int): Second number
        
    Returns:
        int: Greatest Common Divisor
        
    Example:
        >>> gcd(48, 18)
        6
    """
    while b:
        a, b = b, a % b
    return abs(a)


def lcm(a: int, b: int) -> int:
    """
    Calculate Least Common Multiple.
    
    Args:
        a (int): First number
        b (int): Second number
        
    Returns:
        int: Least Common Multiple
        
    Example:
        >>> lcm(12, 18)
        36
    """
    return abs(a * b) // gcd(a, b)


def mean(numbers: List[Union[int, float]]) -> float:
    """
    Calculate arithmetic mean of a list of numbers.
    
    Args:
        numbers (List[Union[int, float]]): List of numbers
        
    Returns:
        float: Arithmetic mean
        
    Example:
        >>> mean([1, 2, 3, 4, 5])
        3.0
    """
    if not numbers:
        raise ValueError("Cannot calculate mean of empty list")
    return sum(numbers) / len(numbers)


def median(numbers: List[Union[int, float]]) -> float:
    """
    Calculate median of a list of numbers.
    
    Args:
        numbers (List[Union[int, float]]): List of numbers
        
    Returns:
        float: Median value
        
    Example:
        >>> median([1, 2, 3, 4, 5])
        3.0
    """
    if not numbers:
        raise ValueError("Cannot calculate median of empty list")
    
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    
    if n % 2 == 0:
        return (sorted_nums[n // 2 - 1] + sorted_nums[n // 2]) / 2
    else:
        return float(sorted_nums[n // 2])


def mode(numbers: List[Union[int, float]]) -> List[Union[int, float]]:
    """
    Find mode(s) of a list of numbers.
    
    Args:
        numbers (List[Union[int, float]]): List of numbers
        
    Returns:
        List[Union[int, float]]: List of mode values
        
    Example:
        >>> mode([1, 2, 2, 3, 3, 3])
        [3]
    """
    if not numbers:
        raise ValueError("Cannot calculate mode of empty list")
    
    from collections import Counter
    counter = Counter(numbers)
    max_count = max(counter.values())
    return [num for num, count in counter.items() if count == max_count]


def standard_deviation(numbers: List[Union[int, float]]) -> float:
    """
    Calculate standard deviation of a list of numbers.
    
    Args:
        numbers (List[Union[int, float]]): List of numbers
        
    Returns:
        float: Standard deviation
        
    Example:
        >>> round(standard_deviation([1, 2, 3, 4, 5]), 2)
        1.58
    """
    if not numbers:
        raise ValueError("Cannot calculate standard deviation of empty list")
    
    avg = mean(numbers)
    variance = sum((x - avg) ** 2 for x in numbers) / len(numbers)
    return math.sqrt(variance)


def distance_2d(point1: Tuple[float, float], point2: Tuple[float, float]) -> float:
    """
    Calculate Euclidean distance between two 2D points.
    
    Args:
        point1 (Tuple[float, float]): First point (x, y)
        point2 (Tuple[float, float]): Second point (x, y)
        
    Returns:
        float: Euclidean distance
        
    Example:
        >>> distance_2d((0, 0), (3, 4))
        5.0
    """
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)


def quadratic_formula(a: float, b: float, c: float) -> Tuple[complex, complex]:
    """
    Solve quadratic equation ax² + bx + c = 0.
    
    Args:
        a (float): Coefficient of x²
        b (float): Coefficient of x
        c (float): Constant term
        
    Returns:
        Tuple[complex, complex]: Two solutions (may be complex)
        
    Example:
        >>> quadratic_formula(1, -5, 6)
        ((3+0j), (2+0j))
    """
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be zero")
    
    discriminant = b ** 2 - 4 * a * c
    sqrt_discriminant = complex(discriminant) ** 0.5
    
    x1 = (-b + sqrt_discriminant) / (2 * a)
    x2 = (-b - sqrt_discriminant) / (2 * a)
    
    return (x1, x2)
