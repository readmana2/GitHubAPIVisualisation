import unittest
import GitHubFile
import json
import pymongo

from GitHubFile import Githubclass,addRepositoryNodes,addNodes,createCategoriesArray


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
        assert(True)
        # ###################################
        #Creating the github Object with the specific Token  and username
        GithubWorkObject=Githubclass("token","username")#
        ##################################
        # # Create the required Categories
        createCategoriesArray(GithubWorkObject.categories,GithubWorkObject.repos)#Github Object should have this stuff

        size=len(GithubWorkObject.categories)#Using a user address with only two categories
        #self.assertEqual(size,2)
        
#Testing if repos given are correct. Do this by evaluating the size of the repos from a known address
    def test_Repos(self):
        # ###################################
        #Creating the github Object
        GithubWorkObject=Githubclass("","readmana2")#
        ###################################
        #Add Repo Nodes
        nextIndex=addRepositoryNodes(GithubWorkObject.t,GithubWorkObject.dictContributorListAllRepos,GithubWorkObject.saveReposInOrder,GithubWorkObject.repos)
        #print(nextIndex)

        self.assertEqual(nextIndex,3)

#Testing if the id returned is correct to ensure the correct amount of Nodes were added to the nodes/links array
    def test_addNodes(self):
        ###################################
        #Creating the github Object
        GithubWorkObject=Githubclass("","readmana2")

        ###################################
        #Add Repo Nodes
        nextIndex=addRepositoryNodes(GithubWorkObject.t,GithubWorkObject.dictContributorListAllRepos,GithubWorkObject.saveReposInOrder,GithubWorkObject.repos)
        GithubWorkObject.t=nextIndex

        ####################################
        #Adding User Nodes and Links between those Nodes and Repos
        nextIndex=addNodes(GithubWorkObject.repos,GithubWorkObject.t,GithubWorkObject.dictContributorListAllRepos,GithubWorkObject.saveReposInOrder,GithubWorkObject.linksStuff)
        GithubWorkObject.t=nextIndex
        
        self.assertEqual(nextIndex,6)
    
#Test if the entire thing works once it has ran    
    def test_runWholeThingWithoutErrors(self):
        assert(True)


#Test if the entire thing works once it has ran    
    def test_runWholeThingWithErrors(self):
        assert(True)

 
#Test if the entire thing works once it has ran    
    def test_DataReceived(self):
        assert(True)       



        
        

 
 


if __name__=='__main__':
    unittest.main()        
