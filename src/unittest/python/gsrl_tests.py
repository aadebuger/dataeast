'''
Created on 2018年2月7日

@author: aadebuger
'''
import unittest

from fdataio.gsrl import gsrl,gsrl2
class Test(unittest.TestCase):


    def testName(self):
        pass

    def testGsrl(self):
         itemv = gsrl()
         for item  in itemv:
             print(item)
    def testGsrl2(self):
         gsrl2()    
         
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()