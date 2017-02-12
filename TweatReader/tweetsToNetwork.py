import tweepy
from tweepy import OAuthHandler
import json
import sys
# initaliaze the twitter API call and execute the search
searchquery = sys.argv[1]
d = "{}"
with open('appsettings.json') as json_data:
    d = json.load(json_data)
    json_data.close()
    
consumer_key = d["consumer_key"]
consumer_secret = d["consumer_secret"]
access_token = d["access_token"]
access_secret = d["access_secret"]

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth,parser=tweepy.parsers.JSONParser())

results = api.search(searchquery,rpp=100)
# api.search(searchquery,rpp=100, page=i) would allow for more results
# loop through results, gather the grpah
import networkx as nx
G=nx.Graph()
for status in results["statuses"]:
	tweeter = status["user"]["screen_name"]
	print "tweet by " + tweeter
	
	# check the tweeter
	if tweeter not in G.nodes():
		G.add_node(tweeter)
		print "added " + tweeter + " to the graph"
	
	# check the persons mentioned by tweeter
	for mention in status["entities"]["user_mentions"]:
		target = mention["screen_name"]
		print tweeter + " mentioned " + target
		
		if target not in G.nodes():
			G.add_node(target)
			print "added " + target + " to the graph"
		
		# twiiter + mentioned persons form an edge
		# if edge already exists, just increase its weight
		ed = (tweeter,target)
		
		if ed not in G.edges():
			G.add_edge(tweeter,target,weight=1)
			print "added edge " + str(ed)
		else:
			G.edges(ed).weight += 1
			print "increased weight for edge " + str(ed)

# export to CSV and graphml
nx.write_weighted_edgelist(G, 'test.weighted.edgelist',delimiter=";")
nx.write_graphml(G, "test.graphml")
	