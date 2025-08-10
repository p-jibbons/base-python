"""
Tests for math functions.
"""

import unittest
import sys
import os

# Add src directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from math_functions import (
    factorial, fibonacci, is_prime, gcd, lcm, mean, median, mode,
    standard_deviation, distance_2d, quadratic_formula
)


class TestMathFunctions(unittest.TestCase):
    
    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
        
        with self.assertRaises(ValueError):
            factorial(-1)
    
    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(6), 8)
        
        with self.assertRaises(ValueError):
            fibonacci(-1)
    
    def test_is_prime(self):
        self.assertTrue(is_prime(17))
        self.assertTrue(is_prime(2))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
    
    def test_gcd(self):
        self.assertEqual(gcd(48, 18), 6)
        self.assertEqual(gcd(17, 13), 1)
    
    def test_lcm(self):
        self.assertEqual(lcm(12, 18), 36)
    
    def test_mean(self):
        self.assertEqual(mean([1, 2, 3, 4, 5]), 3.0)
        
        with self.assertRaises(ValueError):
            mean([])
    
    def test_median(self):
        self.assertEqual(median([1, 2, 3, 4, 5]), 3.0)
        self.assertEqual(median([1, 2, 3, 4]), 2.5)
        
        with self.assertRaises(ValueError):
            median([])
    
    def test_mode(self):
        self.assertEqual(mode([1, 2, 2, 3, 3, 3]), [3])
        
        with self.assertRaises(ValueError):
            mode([])
    
    def test_distance_2d(self):
        self.assertEqual(distance_2d((0, 0), (3, 4)), 5.0)
    
    def test_quadratic_formula(self):
        result = quadratic_formula(1, -5, 6)
        # Should be (3+0j) and (2+0j)
        self.assertAlmostEqual(result[0].real, 3, places=5)
        self.assertAlmostEqual(result[1].real, 2, places=5)
        
        with self.assertRaises(ValueError):
            quadratic_formula(0, 1, 1)


if __name__ == '__main__':
    unittest.main()
