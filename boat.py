import unittest

Left = 'Left'
Right = 'Right'

def calculate_direction(angles):
    return Right if sum(angles) > 0 else Left

class BoatTestCase(unittest.TestCase):
    def test_givenOnePositiveAngle_returnsRight(self):
        givenAngles = [1]

        direction = calculate_direction(givenAngles)

        self.assertEqual(direction, Right)

    def test_givenNothing_returnsLeft(self):
        givenAngles = []

        direction = calculate_direction(givenAngles)

        self.assertEqual(direction, Left)

    def test_givenOneNegativeAngle_returnsLeft(self):
        givenAngles = [-1]

        direction = calculate_direction(givenAngles)

        self.assertEqual(direction, Left)

    def test_givenTwoAnglesWithTotalPositive_returnsRight(self):
        givenAngles = [-1, 2]

        direction = calculate_direction(givenAngles)

        self.assertEqual(direction, Right)

    def test_givenTwoAnglesWithTotalNegative_returnsLeft(self):
        givenAngles = [-2, 1]

        direction = calculate_direction(givenAngles)

        self.assertEqual(direction, Left)

if __name__ == '__main__':
    unittest.main()
