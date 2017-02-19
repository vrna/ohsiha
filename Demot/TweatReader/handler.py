import json
import networkx as nx
G=nx.Graph()
results = "{}"
with open('results.json') as json_data:
    results = json.load(json_data)
    json_data.close()
 
for status in results["statuses"]:
	tweeter = status["user"]["screen_name"]
	print "tweet by " + tweeter
	
	if tweeter not in G.nodes():
		G.add_node(tweeter)
		print "added " + tweeter + " to the graph"
	
	for mention in status["entities"]["user_mentions"]:
		target = mention["screen_name"]
		print tweeter + " mentioned " + target
		if target not in G.nodes():
			G.add_node(target)
			print "added " + target + " to the graph"
		
		ed = (tweeter,target)
		
		if ed not in G.edges():
			G.add_edge(tweeter,target,weight=1)
			print "added edge " + str(ed)
		else:
			G.edges(ed).weight += 1
		
nx.write_graphml(G, "test.graphml")
	