# test_immutablex.py
"""
Tests for ImmutableX module.
"""

import unittest
from immutablex import ImmutableX

class TestImmutableX(unittest.TestCase):
    """Test cases for ImmutableX class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ImmutableX()
        self.assertIsInstance(instance, ImmutableX)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ImmutableX()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
