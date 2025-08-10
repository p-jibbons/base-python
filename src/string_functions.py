"""
String manipulation functions for common operations.
"""


def reverse_string(text: str) -> str:
    """
    Reverse a string.
    
    Args:
        text (str): The string to reverse
        
    Returns:
        str: The reversed string
        
    Example:
        >>> reverse_string("hello")
        'olleh'
    """
    return text[::-1]


def count_vowels(text: str) -> int:
    """
    Count the number of vowels in a string.
    
    Args:
        text (str): The string to count vowels in
        
    Returns:
        int: Number of vowels found
        
    Example:
        >>> count_vowels("hello world")
        3
    """
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)


def is_palindrome(text: str) -> bool:
    """
    Check if a string is a palindrome (reads the same forwards and backwards).
    
    Args:
        text (str): The string to check
        
    Returns:
        bool: True if palindrome, False otherwise
        
    Example:
        >>> is_palindrome("racecar")
        True
    """
    cleaned = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]


def capitalize_words(text: str) -> str:
    """
    Capitalize the first letter of each word in a string.
    
    Args:
        text (str): The string to capitalize
        
    Returns:
        str: String with capitalized words
        
    Example:
        >>> capitalize_words("hello world")
        'Hello World'
    """
    return ' '.join(word.capitalize() for word in text.split())


def remove_duplicates_preserve_order(text: str) -> str:
    """
    Remove duplicate characters from string while preserving order.
    
    Args:
        text (str): The string to process
        
    Returns:
        str: String with duplicates removed
        
    Example:
        >>> remove_duplicates_preserve_order("hello")
        'helo'
    """
    seen = set()
    result = []
    for char in text:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)


def word_count(text: str) -> dict:
    """
    Count occurrences of each word in a string.
    
    Args:
        text (str): The string to analyze
        
    Returns:
        dict: Dictionary with words as keys and counts as values
        
    Example:
        >>> word_count("hello world hello")
        {'hello': 2, 'world': 1}
    """
    words = text.lower().split()
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts


def snake_to_camel(snake_str: str) -> str:
    """
    Convert snake_case to camelCase.
    
    Args:
        snake_str (str): String in snake_case format
        
    Returns:
        str: String in camelCase format
        
    Example:
        >>> snake_to_camel("hello_world_example")
        'helloWorldExample'
    """
    components = snake_str.split('_')
    return components[0] + ''.join(word.capitalize() for word in components[1:])


def camel_to_snake(camel_str: str) -> str:
    """
    Convert camelCase to snake_case.
    
    Args:
        camel_str (str): String in camelCase format
        
    Returns:
        str: String in snake_case format
        
    Example:
        >>> camel_to_snake("helloWorldExample")
        'hello_world_example'
    """
    import re
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', camel_str).lower()
