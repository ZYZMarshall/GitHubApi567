import unittest

from HW04567 import  getCommits, getRepos

class TestGitHubApi(unittest.TestCase):

    def testGetCommits(self):
        self.assertEqual(getCommits('ZYZMarshall', ['Triangle567']), [24], 'There are 24 commits in this repo')

    def testGetRepos(self):
        self.assertEqual(getRepos('ZYZMarshall'), ['GitHubApi567', 'Hello-world-', 'Triangle567'], 'GitHubApi567, Hello-world-, and Triangle567 are the repos')

if __name__ == '__main__':
    unittest.main()
