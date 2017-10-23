import math, sys, os, re

#USAGE MESSAGE: check only one file was input (only one, file found)
if len(sys.argv) < 2:
    sys.exit("Usage: %s filename" % sys.argv[0])
        
filename = sys.argv[1]
    
if not os.path.exists(filename):
    sys.exit("Error: File '%s' not found" % sys.argv[1])

#PLAYER CLASS
class player:

    def  __init__(self, name, bats, hits):
        self.name = name
        self.bats = 0
        self.hits = 0
 
    def addBats(self, bats):
        self.bats += float(bats)
    
    def getAtBats(self):
        return(self.bats)
    
    def addHits(self, hits):
        self.hits += float(hits)
        
    def getHits(self):
        return(self.hits)
    
    #COMPUTE player BA rounded 
    def avg(self, bats, hits):
        if self.hits is not 0:
            return self.hits/self.bats
        else:
            return 0 
        
#READ FILE line-by-line 
player_dict = {}
player_BA = {}
with open(filename, "r") as f:
    
    for line in f:
        #PARSE name, atBats, hits
        regex = "([^.*]+) batted ([\d]+) times with ([\d]+) hits and ([\d])"
        search = re.search(regex, line)
        
        
        if (search is not None):
            name = search.group(1)
            #print(name)
            bats = search.group(2)
            hits = search.group(3)
            
            
            #Create player object 
            p = player(name, float(bats), float(hits))
            
            #If player already in dictionary
            if name in player_dict:
                player_dict[name].addHits(hits)
                player_dict[name].addBats(bats)
                
            #Otherwise make new player 
            else:
                player_dict[name] = p 

#POPULATE new dict of players and their batting averages
for name in player_dict:
    hits = player_dict[name].getHits()
    atBats = player_dict[name].getAtBats()
    
    avg = player_dict[name].avg(atBats, hits)
    avgR = round(avg, 3)
    
    player_BA[name] = avgR
    
#SORT batting averages for players 
sort_PBA = sorted(player_BA.items(), key = lambda v: v[1], reverse = True)    

#PRINT sorted, rounded, batting averages for each player 
for key, value in sort_PBA:
    print ( "%s: %s" % (key, value))


