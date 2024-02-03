#!/usr/bin/env python3
"""Unit test for utils"""
from utils import *
import unittest
from unittest.mock import patch, Mock
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


class TestGetJson(unittest.TestCase):
    """Unit test for utils.get_json"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """Unit test for utils.get_json"""
        res = Mock()
        res.json.return_value = test_payload
        mock_get.return_value = res
        result = get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """Unit test for the utils.memoize"""
    def test_memoize(self):
        """Unit test for the utils.memoize"""
        class TestClass:
            """Class for testing"""
            def a_method(self):
                """a_method for testing"""
                return 42

            @memoize
            def a_property(self):
                """decorator a_property for testing"""
                return self.a_method()

        test_method = TestClass()
        with patch.object(test_method, "a_method") as mock_method:
            mock_method.return_value = 42
            res1 = test_method.a_property
            res2 = test_method.a_property
            mock_method.assert_called_once()
            self.assertEqual(res1, 42)
            self.assertEqual(res2, 42)
