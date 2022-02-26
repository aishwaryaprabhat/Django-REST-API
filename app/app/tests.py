from django.test import TestCase
from app.calc import add 

class CalcTests(TestCase):

    def test_add_numbers(self):
        """Test that two numbers are added together"""
        self.assertEqual(add(3,8),11)
    
    def test_subtract_numbers(self):
        """Test that subtract b from a"""
        self.assertEqual(subtract(8,3),5)