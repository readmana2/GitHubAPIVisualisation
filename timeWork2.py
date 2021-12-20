from github import Github
import json
import requests
import pprint
import math
import re




#The node class
class Githubclass:
    
    errorCode=None
    stringTest=None
    g=None
    repos = None
    user = None
    

    saveReposInOrder=[]#The Repos

    def __init__(self, token, userName):
 
        self.g=Github(token);#(" ");
        
        if self.g is None:
            self.errorCode=-1

        self.username=userName#"""
        self.user=self.g.get_user(self.username)

        if self.user is None:
            self.errorCode=-1

        #Stuff testing
        self.repos=self.g.get_user(self.username).get_repos()
        if self.repos is None:
            self.errorCode=-1

        print("Is This Working?")
        self.stringTest="successfullyInstantiated"




def getAllContributionsOfUsers(GithubWorkObject):

    idOfRepo = 0
    allcommits=[]

    for repo in GithubWorkObject.repos:
        commits =repo.get_commits()
        number=0
        for commit in commits:

            number+=1
            #allcommits.append(repo.get_commit(commit.sha).commit.author.date)
            dateexact=repo.get_commit(commit.sha).commit.author.date

            # print(dateexact)
            stringdate = str(dateexact)
 
            # re.sub("-", ",", stringdate.strip())
            # re.sub(":", ",", stringdate.strip())
            # re.sub(" ", ",", stringdate.strip())

            strippedString= re.sub("[,]", ",", stringdate)
            strippedString=strippedString[:13]


            #print(strippedString)

            allcommits.append(strippedString)
    
    return allcommits



            


# #Main
# #Creating the github Object
# GithubWorkObject=Githubclass("","")
# print(GithubWorkObject.user.login)

# contributionsList=[]
# contributionsList=getAllContributionsOfUsers(GithubWorkObject)
# print(contributionsList[2])

# my_dict = {i:contributionsList.count(i) for i in contributionsList}
# print(my_dict)

# print("JSON of time")
# jsonStringList =json.dumps(my_dict)
#      #print(jsonStringList)


# with open("time1.json", "w") as outfile:
#     outfile.write(jsonStringList)



#Get date of account creation and use that as the base