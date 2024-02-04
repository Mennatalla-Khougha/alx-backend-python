#!/usr/bin/env python3
"""Unit test for clients"""
import unittest
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


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

    @patch('client.get_json', return_value=[
        {"name": "rep1"}, {"name": "rep2"}
        ])
    def test_public_repos(self, mock_get_json):
        """Unit test for clients"""
        with patch(
            'client.GithubOrgClient._public_repos_url',
            new_callable=PropertyMock)\
                as mock_repos_url:
            mock_repos_url.return_value = 'http://github.com/repos'
            client = GithubOrgClient('org_name')
            repos = client.public_repos()
            self.assertEqual(repos, ['rep1', 'rep2'])
            mock_get_json.assert_called_once_with(
                'http://github.com/repos')
            mock_repos_url.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True,),
        ({"license": {"key": "other_license"}}, "my_license", False,),
    ])
    def test_has_license(self, repo, key, excepted_res):
        """Unit test for clients"""
        client = GithubOrgClient('org_name')
        res = client.has_license(repo, key)
        self.assertEqual(res, excepted_res)


# org_payload, repos_payload, expected_repos, apache2_repos = TEST_PAYLOAD[0]

@parameterized_class((
    'org_payload', 'repos_payload',
    'expected_repos', 'apache2_repos'
    ), TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test for clients"""
    @classmethod
    def setUpClass(cls) -> None:
        """Class setUp method"""
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        def side_effect(url):
            """Side effect of url"""
            if url == GithubOrgClient.ORG_URL.format(org='org_name'):
                return Mock(
                    json=lambda: {
                        "repos_url":
                            "https://api.github.com/orgs/org_name/repos"
                        }
                    )
            elif url == 'https://api.github.com/orgs/org_name/repos':
                return Mock(json=lambda: cls.repos_payload)
            return Mock(json=lambda: {})

        cls.mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls) -> None:
        """Class teardown method"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Integration test for clients"""
        client = GithubOrgClient('org_name')
        repos = client.public_repos()
        self.assertEqual(repos, self.expected_repos)

    def test_public_repos_with_license(self):
        """Integration test for clients with license filter"""
        client = GithubOrgClient('org_name')
        repos = client.public_repos(license="apache-2.0")
        self.assertEqual(repos, self.apache2_repos)
