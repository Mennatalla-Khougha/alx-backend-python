#!/usr/bin/env python3
"""Unit test for clients"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Unit test for clients"""
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json', return_value={"organization_info": "dummy"})
    def test_org(self, org_name, mock_get_json):
        """Unit test for clients"""
        client = GithubOrgClient(org_name)
        org_info = client.org
        mock_get_json.assert_called_once_with(
            GithubOrgClient.ORG_URL.format(org=org_name)
            )
        self.assertEqual(org_info, {"organization_info": "dummy"})
