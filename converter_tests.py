import unittest
from converter import c_to_f, f_to_c

class CToFTestCase(unittest.TestCase):
    def test_given1Returns33_8(self):
        f = c_to_f(1)

        self.assertEqual(f, 33.8)

    def test_given0Returns(self):
        f = c_to_f(0)

        self.assertEqual(f, 32)

    def test_given100Returns212(self):
        f = c_to_f(100)

        self.assertEqual(f, 212)

class FToCTestCase(unittest.TestCase):
    def test_given0Returns_17_7(self):
        c = f_to_c(0)

        self.assertEqual(c, -32*5/9)

    def test_given32Returns0(self):
        c = f_to_c(32)

        self.assertEqual(c, 0)

    def test_given212Returns100(self):
        c = f_to_c(212)

        self.assertEqual(c, 100)

if __name__ == '__main__':
    unittest.main()
