from github import Github
import json
import requests
import pprint
import math



#The node class
class Githubclass:
    
    errorCode=None
    stringTest=None
    g=None
    username=None
    user=None
    repos=None
    dictContributorListAllRepos =[]#The nodes
    linksStuff=[]#The links of the Node
    categories=[]
    t=0#The id of the node
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


#Functions
########################################
def determineSybmbolSize(contributions):
        # if x.contributions < 50:
        #     symbolSize=1+5
        # elif x.contributions < 100:
        #     symbolSize=1+10
        # elif x.contributions < 200:
        #     symbolSize=1+20
        # elif x.contributions < 400:
        #     symbolSize=1+40
        # else:
        #     symbolSize=1+80

    symbolSize=1+math.log(contributions)*10
    return symbolSize
        

def createCategoriesArray(categories,repos):
    # Create the required Categories
    
    for repo in repos:#[0:4:1]:
        
        idStuff={'name': repo.name}
        categories.append(idStuff)



    return None
#Returns the next ID available
def addRepositoryNodes(t,dictContributorListAllRepos,saveReposInOrder,repos):
    # #Get all the repos
    for repo in repos:  
    #Adding repo Nodes
    #contributions=value

        idStuff={'id':t,'name': repo.name,'login': repo.name,'value':200,'category':repo.name,"symbolSize": 50,"symbol": "diamond"}
        
        dictContributorListAllRepos.append(idStuff)
        saveReposInOrder.append(repo.name)
        t+=1

#First 12 have an id of 0-11
    return t

#
def addNodes(repos,t,dictContributorListAllRepos,saveReposInOrder,linksStuff):
    i=1

    for repo in repos:#[0:4:1]:
        print("Repo: "+str(i)+" of "+str(repos.totalCount))
        
        
        contribList=list(repo.get_contributors())
        print(len(contribList))

        for x in contribList:#[0:4:1]:
        
            valueIs="ContributionsMade"+str(x.contributions)#Could do a unit test here for a function
            symbolSize=determineSybmbolSize(x.contributions)

            contrib ={'id':t,'name':x.login,'login':x.login,'value':valueIs,'category':repo.name,"symbolSize": symbolSize}
            print("contributor: "+x.login)
            dictContributorListAllRepos.append(contrib)  
            #saveReposInOrde
            #Create Link
            for x in saveReposInOrder:
                if x==repo.name:
                    index=saveReposInOrder.index(x);
                    #Create a link here
                    link={
                    "source":t,
                    "target":index #We might be getting the wrong index here so watch out
                    }
                    linksStuff.append(link)
                    break



            t+=1
        i+=1
    return t

#############################################


###################################
#Creating the github Object
#GithubWorkObject=Githubclass("token","user")
GithubWorkObject=Githubclass("token","user")

print("Testing"+GithubWorkObject.stringTest)

###################################
#Add Repo Nodes
nextIndex=addRepositoryNodes(GithubWorkObject.t,GithubWorkObject.dictContributorListAllRepos,GithubWorkObject.saveReposInOrder,GithubWorkObject.repos)
GithubWorkObject.t=nextIndex

####################################
#Adding User Nodes and Links between those Nodes and Repos
nextIndex=addNodes(GithubWorkObject.repos,GithubWorkObject.t,GithubWorkObject.dictContributorListAllRepos,GithubWorkObject.saveReposInOrder,GithubWorkObject.linksStuff)
GithubWorkObject.t=nextIndex
##################################
# # Create the required Categories
createCategoriesArray(GithubWorkObject.categories,GithubWorkObject.repos)

data={'nodes':GithubWorkObject.dictContributorListAllRepos,'links':GithubWorkObject.linksStuff,'categories':GithubWorkObject.categories}


print("JSON of contributors")
jsonStringList =json.dumps(data)
#print(jsonStringList)


with open("sample4.json", "w") as outfile:
    outfile.write(jsonStringList)



