import unittest

from HW04567 import get_commits_numbers


class TestHW04(unittest.TestCase):
    def test_user_repositories(self):
        self.assertDictEqual(get_commits_numbers("ZYZMarshall"),
                             {'GitHubAPI567': 18, 'Triangle567': 24, 'Hello-world-': 5})
