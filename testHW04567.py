
import json
import unittest
# import unittest.mock
# from unittest.mock import patch
from unittest import mock
from unittest.mock import Mock
from HW04567 import getCommitnum, getUserRepos

class DummyObject(object):
    def __init__(self, content):
        self.content = content

class TestHw04a(unittest.TestCase):
        
    @mock.patch('requests.get')
    def testValidInput1(self, mocked_reqs):
        """ this mocks GitHub returning JSON with two repositories.  The second and third are the JSON details about the number of commits """
        mocked_reqs.side_effect = [
            # Each nested dictionary below is like an individual repo - 
            # the first response emulates the github request to get all repos
            # the subsequent responses emulate the details associated with each of the repos in mockedResponses[0]
            (b'[{"id" : "146485002", "name" : "hello-world"}, {"id" : "147696620", "name" : "Triangle567"}]'),
            (b'[{"commit": "You want a commit?"}, {"commit": "Leave me alone."}, {"commit": "Alright,what you want?"}]'),
            (b'[{"comit": "No, not again."}, {"commit": "You wanna fight?"}]')]


        self.assertEqual(getCommitnum("", "hello-world"), 2)  #YOUR TEST HERE
        self.assertEqual(getCommitnum("", "Triangle567"), 3)  #YOUR TEST HERE
        
       


        
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False)
