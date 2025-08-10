"""
Example usage of various Python utility functions.
"""

import sys
import os

# Add src directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from string_functions import reverse_string, count_vowels, is_palindrome
from list_functions import find_duplicates, remove_duplicates, flatten_list
from math_functions import factorial, fibonacci, is_prime
from utility_functions import timer, generate_random_string


def main():
    print("=== Python Functions Reference Examples ===\\n")
    
    # String functions
    print("STRING FUNCTIONS:")
    text = "Hello World"
    print(f"Original: '{text}'")
    print(f"Reversed: '{reverse_string(text)}'")
    print(f"Vowel count: {count_vowels(text)}")
    print(f"Is palindrome: {is_palindrome('racecar')}")
    print()
    
    # List functions
    print("LIST FUNCTIONS:")
    numbers = [1, 2, 3, 2, 4, 3, 5]
    print(f"Original list: {numbers}")
    print(f"Duplicates: {find_duplicates(numbers)}")
    print(f"Without duplicates: {remove_duplicates(numbers)}")
    
    nested = [[1, 2], [3, 4], [5, 6]]
    print(f"Nested list: {nested}")
    print(f"Flattened: {flatten_list(nested)}")
    print()
    
    # Math functions
    print("MATH FUNCTIONS:")
    n = 5
    print(f"Factorial of {n}: {factorial(n)}")
    print(f"6th Fibonacci number: {fibonacci(6)}")
    print(f"Is 17 prime? {is_prime(17)}")
    print()
    
    # Utility functions
    print("UTILITY FUNCTIONS:")
    
    @timer
    def sample_function():
        """Sample function to demonstrate timer decorator."""
        import time
        time.sleep(0.1)  # Simulate work
        return "Task completed"
    
    result = sample_function()
    print(f"Function result: {result}")
    
    # Generate random string
    random_str = generate_random_string(10, include_digits=True, include_symbols=False)
    print(f"Random string: {random_str}")


if __name__ == "__main__":
    main()
