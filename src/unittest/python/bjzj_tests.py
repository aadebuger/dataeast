'''
Created on 2018年2月23日

@author: aadebuger
'''
import unittest

from fdataio.gsrl import bkzj,bkzj_gn
class Test(unittest.TestCase):


    def testName(self):
            bkzj(1)

    def testBkzjgn(self):
            bkzj_gn(1)
            
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()