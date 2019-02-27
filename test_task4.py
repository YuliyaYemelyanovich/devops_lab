from unittest import TestCase
import task4


class TestPrime(TestCase):

    def test_find_sum(self):
        self.assertEqual(task4.find_sum([-7, 5, -1, 3, 9]), 17)
        self.assertEqual(task4.find_sum([3, 14, -9, 4, -5, 1, -12, 4]), 26)
        self.assertEqual(task4.find_sum([-5, 1, 2, 3, 4, 5, 6, 7, 8, -3]), 36)

    def test_find_mult(self):
        self.assertEqual(task4.find_mult([-7, 5, -1, 3, 9]), -15)
        self.assertEqual(task4.find_mult([3, 14, -9, 4, -5, 1, -12, 4]), 180)
        self.assertEqual(task4.find_mult([-5, 1, 2, 3, 4, 5, 6, 7, 8, -3]), 5040)
