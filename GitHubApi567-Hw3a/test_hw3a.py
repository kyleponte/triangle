import unittest
import hw3a
from unittest.mock import patch


class FakeResponse:
    def __init__(self, status_code=200, json_data=None):
        self.status_code = status_code
        self._json = json_data if json_data is not None else []

    def json(self):
        return self._json

class TestHW3AMock(unittest.TestCase):
    @patch("hw3a.requests.get")
    def test_user_not_found(self, mock_get):
        """ValueError should be raised."""
        mock_get.return_value = FakeResponse(status_code=404, json_data=[])
        with self.assertRaises(ValueError):
            hw3a.list_repos("kyleponte10122371238")

    @patch("hw3a.requests.get")
    def test_repo_with_commits(self, mock_get):
        """Repo with two commits should return commit_count=2."""
        mock_get.side_effect = [
            FakeResponse(200, [{"name": "RepoA"}]),                 
            FakeResponse(200, [{"test": "1"}, {"test": "2"}])      
        ]
        out = hw3a.list_repos("Kyle")
        self.assertEqual(out, [{"repo": "RepoA", "commits": 2}])

    @patch("hw3a.requests.get")
    def test_repo_with_no_commits(self, mock_get):
        """Repo with no commits should return commit_count=0."""
        mock_get.side_effect = [
            FakeResponse(200, [{"name": "RepoB"}]),  
            FakeResponse(200, [])                    
        ]
        out = hw3a.list_repos("John")
        self.assertEqual(out, [{"repo": "RepoB", "commits": 0}])


if __name__ == "__main__":
    unittest.main()
