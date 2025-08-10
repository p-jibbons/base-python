"""
Python Functions Reference Package

A comprehensive collection of utility functions for common programming tasks.
"""

__version__ = "1.0.0"
__author__ = "Your Name"
__description__ = "A reference collection of basic Python functions"

# Import commonly used functions for easy access
from .string_functions import reverse_string, count_vowels, is_palindrome
from .list_functions import find_duplicates, remove_duplicates, flatten_list
from .math_functions import factorial, fibonacci, is_prime, mean, median
from .utility_functions import timer, generate_random_string, memoize

__all__ = [
    # String functions
    'reverse_string', 'count_vowels', 'is_palindrome',
    # List functions  
    'find_duplicates', 'remove_duplicates', 'flatten_list',
    # Math functions
    'factorial', 'fibonacci', 'is_prime', 'mean', 'median',
    # Utility functions
    'timer', 'generate_random_string', 'memoize',
]
