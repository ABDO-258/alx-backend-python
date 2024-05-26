#!/usr/bin/env python3
""" unitest try"""

import unittest
from unittest.mock import patch
from utils import access_nested_map, get_json

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


class TestGetJson(unittest.TestCase):
    """unit tests for get_json"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        with patch('utils.requests.get') as mock_get:
            mock_get.return_value.json.return_value = test_payload

            # Call get_json with the test URL
            result = get_json(test_url)

            # Assertions
            self.assertEqual(result, test_payload)
            mock_get.assert_called_once_with(test_url)


if __name__ == "__main__":
    unittest.main()
