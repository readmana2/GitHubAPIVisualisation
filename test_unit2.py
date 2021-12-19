import unittest
from timeWork2 import Githubclass,getAllContributionsOfUsers
import timeWork2
import json



class TestingLCA(unittest.TestCase):
#Testing for the correct symbolSize
    def test_timeGraph(self):
        #Main
        #Creating the github Object
        GithubWorkObject=Githubclass("","username")
        print(GithubWorkObject.user.login)


        contributionsList=[]
        contributionsList=getAllContributionsOfUsers(GithubWorkObject)
        print(contributionsList[2])

        if GithubWorkObject.errorCode == -1:
            assert(False)

        assert(True)


        


if __name__=='__main__':
    unittest.main()        
