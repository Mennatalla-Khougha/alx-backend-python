#!/usr/bin/env python3
"""Unit test for clients"""
import unittest
from unittest.mock import patch, PropertyMock
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

    def test_public_repos_url(self):
        """Unit test for clients"""
        with patch(
            'client.GithubOrgClient.org',
            new_callable=PropertyMock
            )\
                as mock_org:
            mock_org.return_value = {'repos_url': 'expected_url'}
            client = GithubOrgClient('org_name')
            self.assertEqual(client._public_repos_url, 'expected_url')
