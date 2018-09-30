#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tuesday 9/25 2018
author: yuzhen zhang
"""

import unittest

from HW04567 import get_info


class TestGetInfo(unittest.TestCase):
    
    def testValidUser(self):
        self.assertEqual(get_info('ZYZMarshall'), [('hello-world', 2), ('GitHubApi567', 25), ('Triangle567', 24)])
        
    def testInvalidUser(self):
        self.assertEqual(get_info('jsbfjejknejk'), 'Invalid GitHub Username')
        self.assertEqual(get_info(' '), 'Invalid GitHub Username')


if __name__ == '__main__':
    unittest.main()
