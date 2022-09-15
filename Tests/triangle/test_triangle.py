from tkinter.tix import Tree
from typing import Type
from unittest import TestCase
from triangle import area_of_a_triangle

class TestAreaOfTriange(TestCase):
    def test_good_values(self):
        """ Test areas when values are good """
        self.assertAlmostEqual(area_of_a_triangle(3.4556, 8.3567), 14.43870626)
        self.assertEqual(area_of_a_triangle(2, 5), 5.0)
        self.assertEqual(area_of_a_triangle(0, 5), 0,0)

    def test_bad_values(self):
        """ Test that Value Error is raised for bad values """
        self.assertRaises(ValueError, area_of_a_triangle, -2, 5)
        self.assertRaises(ValueError, area_of_a_triangle, 2, -5)

    def test_bad_types(self):
        """ Test that TypeError is raised with bad types """
        self.assertRaises(TypeError, area_of_a_triangle, True, 5)
        self.assertRaises(TypeError, area_of_a_triangle, 2, True)
        self.assertRaises(TypeError, area_of_a_triangle, "base", 5)
        self.assertRaises(TypeError, area_of_a_triangle, 2, "height")