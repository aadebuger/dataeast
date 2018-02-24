'''
Created on 2018年2月24日

@author: aadebuger
'''
import unittest

from fdataio.gsrl import report
class Test(unittest.TestCase):


    def testName(self):
            report()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()