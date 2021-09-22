import sys
import os
import unittest

from source.libs.Request import Request


class Test(unittest.TestCase):

    # Mongo db module and database on cloud testing
    
    database="WebScrapper"
    table="Links"
    interface=Interface(database,table)
    test_url="https://realpython.github.io/fake-jobs"
    def test_CreateUpdateItem(self):

        data={"links":["first entry"]}
        self.assertTrue(self.interface.UpdateItem(self.table,"links",data),"Cannot connect to mongo database")
        data={"links":["second entry"]}
        self.assertTrue(self.interface.UpdateItem(self.table,"links",data),"Cannot update data")
        self.assertEqual(type(self.interface.GetItem(self.table,"links")),dict,"This method must return a dictionary")
        self.assertEqual(type(self.interface.GetItems(self.table)),list,"This method must return a list")
        self.assertTrue(type(self.interface.DeleteItem(self.table,id="")),"Must return True if item is deleted or doesnt exist")
        self.assertTrue(self.interface.ExploreUrl(self.test_url),"Method must return true if the feching process finishes")
        self.assertEqual(type(self.interface.GetLinks()),list,"Method must returns a list of links")

    #http requests module
    test_url="https://realpython.github.io/fake-jobs"
    req=Request()

        
    def test_Ping(self):

        self.assertTrue(self.req.Ping(self.test_url),"Cannot connect to url, this urls exists")
        self.assertFalse(self.req.Ping(""),"No url added, method fail, raise exeption and returns False")
        

    def test_Get(self):

        self.assertTrue(self.req.Get(self.test_url),"Cannot connect to url, this url eixist")
        self.assertFalse(self.req.Get(""),"No url added, must return False")
        temp="https://realpython.github.io/jfjjgj-jobsiyoweoh"
        self.assertFalse(self.req.Get(temp),"Url doesnt exist, must return false")


    def test_ParseResponseBody(self):
   
        self.assertTrue(self.req.Get(self.test_url),"Cannot connect to url, this urls exists")
        self.assertEqual(type(self.req.ParseResponseBodyToList()),list,"Method must return a list")

    
    #main process module
    process=SearchProcess.Proccess()
    test_url="https://realpython.github.io/fake-jobs"

    def test_explore_urls(self):

        self.assertEqual(type(self.process.ExploreUrl(self.test_url)),list,"Cannot explore/fetche urls")
        self.assertFalse(self.process.ExploreUrl("https://realpyt.io/ddfake-jobssasdasdasdsasd"),"this is a wrong url, the process must return False")


    # app inner path system module
    path="/home/robin/Python/WebScrapper"
    explorer=DirectoryTreeGenerator_lite.TreeExplorer()
    

    def test_directory_tree_explorer(self):

        self.explorer.ExploreDirectories(path=self.path)
        dir_list=self.explorer.Dir_List
        file_list=self.explorer.Files_List
        self.assertGreater(len(dir_list),0,"Class cannot fetch directories")
        self.assertGreater(len(file_list),0,"Class cannot fetch files")
        self.explorer.ExploreDirectories(path=self.path,ignore=["static","__pycache__","__init__.py"])
        dir_list2=self.explorer.Dir_List
        file_list2=self.explorer.Files_List
        self.assertTrue(len(dir_list) > len(dir_list2),"Directory filter is not working")
        self.assertTrue(len(file_list) > len(file_list2),"Files filter is not working")

if __name__=="__main__":

    unittest.main()