#!/usr/bin/env python3
"""Unit test for utils"""
from utils import access_nested_map
import unittest
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """Unit test for utils.access_nested_map"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, result):
        """Unit test for utils.access_nested_map"""
        res = access_nested_map(nested_map, path)
        self.assertEqual(result, res)

    @parameterized.expand([
        ({}, ("a",), "'a'"),
        ({"a": 1}, ("a", "b"), "'b'"),
    ])
    def test_access_nested_map_exception(self, nested_map, path, result):
        """Unit test for utils.access_nested_map"""
        with self.assertRaises(KeyError) as key:
            access_nested_map(nested_map, path)
        self.assertEqual(str(key.exception), result)
