#!/usr/bin/env python3
""" unitest try"""

import unittest
from utils import access_nested_map
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """unit tests for utils.access_nested_map"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_value):
        """FIRST TEST CASE"""
        self.assertEqual(access_nested_map(nested_map, path), expected_value)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """seconde test """
        expected_message = f"'{path[-1]}'"
        with self.assertRaises(KeyError) as testing:
            access_nested_map(nested_map, path)

        self.assertEqual(str(testing.exception), expected_message)


if __name__ == "__main__":
    unittest.main()
