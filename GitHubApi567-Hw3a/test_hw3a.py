import unittest
import hw3a


class FakeResponse:
    def __init__(self, status_code=200, json_data=None):
        self.status_code = status_code
        self._json = json_data if json_data is not None else []

    def json(self):
        return self._json

class TestHW3AMock(unittest.TestCase):
    def test_known_user_has_repos(self):
        """Check that a known public user has at least one repo."""
        data = hw3a.list_repos("kyleponte")
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)
        for repo in data:
            self.assertIn("repo", repo)
            self.assertIn("commits", repo)

    def test_fake_user_raises(self):
        """Check that an obviously fake user raises ValueError."""
        with self.assertRaises(ValueError):
            hw3a.list_repos("kyleponte12736172301923")


if __name__ == "__main__":
    unittest.main()
