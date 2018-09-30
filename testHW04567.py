import unittest

from HW04567 import  getCommits, getRepos

class TestGitHubApi(unittest.TestCase):

    def testGetCommits(self):
        self.assertEqual(getCommits('ZYZMarshall', ['Triangle567']), [24], 'There are 24 commits in this repo')

    def testGetRepos(self):
        self.assertEqual(getRepos('ZYZMarshall'), ['GitHubApi567', 'hello-world','Hello-world-', 'triangle','Triangle567','SS2567-HW05'])

if __name__ == '__main__':
    unittest.main()
