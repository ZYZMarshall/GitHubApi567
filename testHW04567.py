import unittest

from HW04567 import  getCommits, getRepos

class TestGitHubApi(unittest.TestCase):

    def testGetCommits(self):
        self.assertEqual(getCommits('ZYZMarshall', ['Triangle567']), [2], 'There are 2 commits in this repo')

    def testGetRepos(self):
        self.assertEqual(getRepos('ZYZMarshall'), ['hello-world', 'triangle', 'SSW567HW05','GitHubApi567', 'Hello-world-', 'Triangle567'])

if __name__ == '__main__':
    unittest.main()
