from github import Github

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


def addRepositoryNodes(t,dictContributorListAllRepos,saveReposInOrder,repos):
    # #Get all the repos
    for repo in repos:  
    #Adding repo Nodes
    #contributions=value

        idStuff={'id':t,'name': repo.name,'login': repo.name,'value':200,'category':repo.name,"symbolSize": 50,"symbol": "diamond"}
        
        dictContributorListAllRepos.append(idStuff)
        saveReposInOrder.append(repo.name)
        t+=1

#E.g First 12 have an id of 0-11
    return t



