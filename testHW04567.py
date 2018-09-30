import unittest

from HW04567 import get_commits_numbers


class TestHW04(unittest.TestCase):
    def test_user_repositories(self):
        self.assertDictEqual(get_commits_numbers("ZYZMarshall"),
                             {{'GitHubApi567': 21,'GitHubApi567-1': 5,'GitHubApi567-2': 4,'Hello-world-': 5, 'SSW567-HW05': 5,'Triangle567': 24,'hello-world': 2, 'triangle': 5}})

if __name__ == '__main__':
    unittest.main(verbosity=2, exit=False)
