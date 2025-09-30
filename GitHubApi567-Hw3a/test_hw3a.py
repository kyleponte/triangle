import unittest
from unittest.mock import patch
import hw3a


# Fake response object that behaves like requests.get() output
class FakeResponse:
    def __init__(self, status_code=200, json_data=None):
        self.status_code = status_code
        self._json = json_data if json_data is not None else []

    def json(self):
        return self._json


class TestHW4A(unittest.TestCase):
    @patch("hw3a.requests.get")
    def test_user_not_found(self, mock_get):
        """If GitHub returns 404 for the user, our code should raise ValueError."""
        mock_get.return_value = FakeResponse(status_code=404, json_data=[])
        with self.assertRaises(ValueError):
            hw3a.list_repos("no_such_user")

    @patch("hw3a.requests.get")
    def test_repo_with_commits(self, mock_get):
        """Repo with two commits should return commit_count=2."""
        mock_get.side_effect = [
            FakeResponse(200, [{"name": "RepoA"}]),                 # first call: repos
            FakeResponse(200, [{"sha": "1"}, {"sha": "2"}])        # second call: commits
        ]
        out = hw3a.list_repos("alice")
        self.assertEqual(out, [{"repo": "RepoA", "commits": 2}])

    @patch("hw3a.requests.get")
    def test_repo_with_no_commits(self, mock_get):
        """Repo with no commits should return commit_count=0."""
        mock_get.side_effect = [
            FakeResponse(200, [{"name": "RepoB"}]),  # repos
            FakeResponse(200, [])                    # commits
        ]
        out = hw3a.list_repos("bob")
        self.assertEqual(out, [{"repo": "RepoB", "commits": 0}])


if __name__ == "__main__":
    unittest.main()
