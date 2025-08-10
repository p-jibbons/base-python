"""
Tests for string functions.
"""

import unittest
import sys
import os

# Add src directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from string_functions import (
    reverse_string, count_vowels, is_palindrome, capitalize_words,
    remove_duplicates_preserve_order, word_count, snake_to_camel, camel_to_snake
)


class TestStringFunctions(unittest.TestCase):
    
    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string(""), "")
        self.assertEqual(reverse_string("a"), "a")
    
    def test_count_vowels(self):
        self.assertEqual(count_vowels("hello world"), 3)
        self.assertEqual(count_vowels(""), 0)
        self.assertEqual(count_vowels("AEIOU"), 5)
        self.assertEqual(count_vowels("bcdfg"), 0)
    
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
        self.assertFalse(is_palindrome("hello"))
    
    def test_capitalize_words(self):
        self.assertEqual(capitalize_words("hello world"), "Hello World")
        self.assertEqual(capitalize_words(""), "")
    
    def test_remove_duplicates_preserve_order(self):
        self.assertEqual(remove_duplicates_preserve_order("hello"), "helo")
        self.assertEqual(remove_duplicates_preserve_order(""), "")
    
    def test_word_count(self):
        result = word_count("hello world hello")
        expected = {"hello": 2, "world": 1}
        self.assertEqual(result, expected)
    
    def test_snake_to_camel(self):
        self.assertEqual(snake_to_camel("hello_world"), "helloWorld")
        self.assertEqual(snake_to_camel("hello"), "hello")
    
    def test_camel_to_snake(self):
        self.assertEqual(camel_to_snake("helloWorld"), "hello_world")
        self.assertEqual(camel_to_snake("hello"), "hello")


if __name__ == '__main__':
    unittest.main()
