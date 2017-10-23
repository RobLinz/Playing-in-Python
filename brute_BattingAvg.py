import sys, os, re

player_atBat = {}
player_hits = {}
player_avgR = {}

#USAGE MESSAGE: check only one file was input (only one, file found)
if len(sys.argv) < 2:
    sys.exit("Usage: %s filename" % sys.argv[0])

filename = sys.argv[1]

if not os.path.exists(filename):
    sys.exit("Error: File '%s' not found" % sys.argv[1])

#READ FILE line-by-line
#PARSE and STORE information name, bats, hits 
with open(filename, "r") as f:

    for line in f:
        regex = "([^.*]+) batted ([\d]+) times with ([\d]+) hits and ([\d])"
        search = re.search(regex, line)
        
        
        if (search is not None):
            name = search.group(1)
            bats = search.group(2)
            hits = search.group(3)
            runs = search.group(4)
        
            #player exists, bat 
            if name in player_atBat:
                b = player_atBat[name]
                player_atBat[name] = float(b) + float(bats)
            #create player, bat
            else:
                player_atBat[name] = float(bats)
                
            #player exists, hits
            if name in player_hits:
                h = player_hits[name]
                player_hits[name] = float(h)+float(hits)
            #create player, hits 
            else:
                player_hits[name] = float(hits)

#COMPUTE batting averages for each player
for name in player_atBat:
    for name in player_hits:
        atBats = player_atBat[name]
        totHits = player_hits[name]
        player_avgR[name]= round((totHits/atBats),3)


#SORT batting averages for players 
sort_PBA = sorted(player_avgR.items(), key = lambda v: v[1], reverse = True)

#PRINT sorted, rounded, batting averages for each player 
for key, value in sort_PBA:
    print ( "%s: %s" % (key, value))
