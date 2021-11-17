import unittest
import scriptGather5TestNodes4
import json
import pymongo


class TestingGithubVisualisation(unittest.TestCase):
   

 #Test if the entire thing works while building.   
    def test_BuildDataObject(self):

        GithubWorkObject=Githubclass("token","username")#
        if GithubWorkObject.errorCode == -1:
            assert(False)

        assert(True)

#Testing if categories given are correct. Do this by evaluating the size of the categories from a known address
#According to the Visualisation library I looked at and some basic messing around with tutorials,I will need categories which should correspond to repos
    def test_Cateogories(self):

        # ###################################
        #Creating the github Object with the specific Token  and username
        GithubWorkObject=Githubclass("token","username")#
        ##################################
        # # Create the required Categories
        createCategoriesArray(GithubWorkObject.categories,GithubWorkObject.repos)#Github Object should have this stuff

        size=len(GithubWorkObject.categories)#Using a user address with only two categories
        self.assertEqual(size,2)
        
#Testing if repos given are correct. Do this by evaluating the size of the repos from a known address
    def test_Repos(self):
        assert(False)

#Testing if the id returned is correct to ensure the correct amount of Nodes were added to the nodes/links array
    def test_addNodes(self):
        assert(False)
    
#Test if the entire thing works once it has ran    
    def test_runWholeThingWithoutErrors(self):
        assert(False)


#Test if the entire thing works once it has ran    
    def test_runWholeThingWithErrors(self):
        assert(False)

 
#Test if the entire thing works once it has ran    
    def test_DataReceived(self):
        assert(False)       



        
        

 
 


if __name__=='__main__':
    unittest.main()        
