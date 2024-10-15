import data
import lab4
import unittest

from data import Point


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_first_element_1(self):
        input = [[1,2], [3,4]]
        result = lab4.first_element(input)
        expected = [1, 3]
        self.assertEqual(expected, result)


    def test_first_element_2(self):
        input = [[0],[1, 2, 3, 4, 5],[64,3], [-1]]
        result = lab4.first_element(input)
        expected = [0, 1, 64, -1]
        self.assertEqual(expected, result)

    # Part 2
    from data import Point

    def test_x_coordinates_1(self):
        input = [Point(3, 4), Point(-0.5, 20) ]
        result = lab4.x_coordinates(input)
        expected = [3, -0.5]
        self.assertEqual(expected, result)


    def test_x_coordinates_2(self):
        input = [Point(0,3), Point(-33, 87), Point(1, 0)]
        result = lab4.x_coordinates(input)
        expected = [0,-33, 1]
        self.assertEqual(expected, result)

    # Part 3

    def test_are_in_positive_quadrant_1(self):
        input = [Point(3, 4), Point(-0.5, 20) ]
        result = lab4.are_in_positive_quadrant(input)
        expected = [Point(3, 4)]
        self.assertEqual(expected, result)


    def test_are_in_positive_quadrant_2(self):
        input = [Point(1,3), Point(-33, 87), Point(1, 0),Point(0.1,0.01)]
        result = lab4.are_in_positive_quadrant(input)
        expected = [Point(1,3), Point(0.1, 0.01)]
        self.assertEqual(expected, result)

    # Part 4

    def test_distance_1(self):
        input1 = Point(1,2)
        input2 = Point(4,6)
        result = lab4.distance(input1, input2)
        expected = 5
        self.assertEqual(expected, result)


    def test_distance_2(self):
        input1 = Point(-1, 2)
        input2 = Point(-2, 3)
        result = lab4.distance(input1,input2)
        expected = pow(2,0.5)
        self.assertEqual(expected, result)
    # Part 5
    def test_manhattan_distance_1(self):
        input1 = Point(-1,2)
        input2 = Point(4,-6)
        result = lab4.manhattan_distance(input1, input2)
        expected = 13
        self.assertEqual(expected, result)


    def test_manhattan_distance_2(self):
        input1 = Point(-1, -2)
        input2 = Point(-2, -3)
        result = lab4.manhattan_distance(input1,input2)
        expected = 2
        self.assertEqual(expected, result)

    # Part 6

    def test_distance_all_1(self):
        input = [Point(0,1), Point(5,0), Point(-7,0), Point(0,-1), Point(0,0)]
        result = lab4.distance_all(input)
        expected = [1, 5, 7, 1, 0]
        self.assertEqual(expected, result)


    def test_distance_all_2(self):
        input = [Point(3, 4), Point(5, 1), Point(-3, -4), Point(4, -3), Point(5, 12)]
        result = lab4.distance_all(input)
        expected = [5, pow(26, 0.5), 5, 5, 13]
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
