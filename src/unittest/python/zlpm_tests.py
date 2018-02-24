'''
Created on 2018年2月23日

@author: aadebuger
'''
import unittest
from fdataio.gsrl import zlpm,zlpmall

class Test(unittest.TestCase):


    def testZlpm(self):
            zlpm()
    def testZlpmall(self):
            zlpmall(10)
            

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()