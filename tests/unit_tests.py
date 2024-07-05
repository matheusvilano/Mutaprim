import unittest

from mutaprim import *


class MutaprimTests(unittest.TestCase):

    def test_types(self):
        self.assertIsInstance(MutableBool().value, bool)
        self.assertIsInstance(MutableInt().value, int)
        self.assertIsInstance(MutableFloat().value, float)
        self.assertIsInstance(MutableStr().value, str)
        self.assertIsInstance(MutableBytes().value, bytes)

    def test_value(self):
        number = MutableInt(10)
        self.assertEqual(number.get(), 10)
        self.assertEqual(number.value, 10)
        number.value = 20
        self.assertEqual(number.get(), 20)
        self.assertEqual(number.value, 20)
        number.set(30)
        self.assertEqual(number.get(), 30)
        self.assertEqual(number.value, 30)


if __name__ == '__main__':
    unittest.main()
