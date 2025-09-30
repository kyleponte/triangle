import unittest
import hw3a


class TestHW3ALive(unittest.TestCase):
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
