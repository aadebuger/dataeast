'''
Created on 2018年2月7日

@author: aadebuger
'''
import unittest

from fdataio.gsrl import zjlxall,zjlxquery

class Test(unittest.TestCase):


    def testName(self):
         zjlxall()
    def testzjlxquery(self):
         allv= zjlxall()
         position= zjlxquery(allv,"000858")   
         print("000858 positon ",position) 
         position= zjlxquery(allv,"600050")   
         print("600050 positon",position) 
         position= zjlxquery(allv,"002439")   
         print("002439 positon",position)      
         position= zjlxquery(allv,"002439")   
         print("002439 positon",position) 
         position= zjlxquery(allv,"002038")   
         print("002038 positon",position) 

         position= zjlxquery(allv,"002594")   
         print("002594 positon",position)          
         position= zjlxquery(allv,"601878")   
         print("601878 positon",position)  
         position= zjlxquery(allv,"600679")   
         print("600679 positon",position)  
         position= zjlxquery(allv,"600958")   
         print("600958 positon",position) 
         position= zjlxquery(allv,"000681")   
         print("000681 positon",position) 

         position= zjlxquery(allv,"600876")   
         print("600876 positon",position) 
         position= zjlxquery(allv,"600125")   
         print("600125 positon",position) 
         position= zjlxquery(allv,"000400")   
         print("000400 positon",position)                   
         position= zjlxquery(allv,"000002")   
         print("000002 positon",position)  
         position= zjlxquery(allv,"600115")   
         print("600115 positon",position)  
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()