# test_sunrise.py
"""
Tests for SunRise module.
"""

import unittest
from sunrise import SunRise

class TestSunRise(unittest.TestCase):
    """Test cases for SunRise class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SunRise()
        self.assertIsInstance(instance, SunRise)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SunRise()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
