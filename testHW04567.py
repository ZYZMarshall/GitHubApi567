import unittest
from HW04567 import getUserRepos, getCommitnum

class TestHW04567(unittest.TestCase):
    
    def testHW0456701(self):
        self.assertIn("hello-world", getUserRepos("ZYZMarshall"))
                    
    def testHW0456701b(self):
        self.assertNotIn("ddddddd", getUserRepos("ZYZMarshall"))

    def testHW0456701c(self):
        self.assertEqual(24, getCommitnum("ZYZMarshall", "Triangle567"))
                         
    def testHW0456702A(self):
        self.assertIn("Triangle567", getUserRepos("ZYZMarshall"))
                    
    def testHW0456702b(self):
        self.assertNotIn("HelloUnivrse", getUserRepos("ZYZMarshall"))

    def testHW0456702c(self):
        self.assertNotEqual(3, getCommitnum("ZYZMarshall", "Hello-world-"))

    def testHW0456703A(self):
        self.assertEqual([], getUserRepos("Notexisit12343213"))

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
