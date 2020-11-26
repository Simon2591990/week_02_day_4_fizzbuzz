import unittest
from src.fizzbuzz import fizzbuzz

class TestFizzBuzz(unittest.TestCase):
    def test_fizzbuzz__3_returns_fizz(self):
        self.assertEqual("Fizz", fizzbuzz(3))

    def test_fizzbuzz__5_returns_buzz(self):
        self.assertEqual("Buzz", fizzbuzz(5))

    def test_fizzbuzz__15_returns_fizzbuzz(self):
        self.assertEqual("Fizz Buzz", fizzbuzz(15))
    
    def test_fizzbuzz__7_returns_7(self):
        self.assertEqual("7", fizzbuzz(7))

    def test_fizzbuzz__6_returns_fizz(self):
        self.assertEqual("Fizz", fizzbuzz(6))
    
    def test_fizzbuzz__10_returns_buzz(self):
        self.assertEqual("Buzz", fizzbuzz(10))
    
    def test_fizzbuzz__30_returns_fizzbuzz(self):
        self.assertEqual("Fizz Buzz", fizzbuzz(30))



