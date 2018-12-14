import networkx as nx 
import matplotlib.pyplot as plt


# path to cleaned file
GRAPH = "NetworkAnalysis/criminal-activity/datasets/graph/family.gml"
# column names - surname will be useful later when we'd like to group them by family
FULLNAME = "fullname"
#FORENAME =  "forename"
SURNAME = "surname" 
EVENT_ID = "event"
# number of events
NUMB_EVENTS = 47


G = nx.read_gml(GRAPH)
# get edges and respective weight to pass as width attribute
weights = [G[u][v]['weight'] for u,v in G.edges]
# get nodes attributes to pass as size
# number of events attended
numb_events = [G.nodes[v]['eventscount']*10 for v in G.nodes]
family_size = [G.nodes[v]['familysize'] for v in G.nodes]
# plotting the graph
nx.draw(G, node_size = numb_events , with_labels = False, alpha=0.7, width = weights, node_color = family_size)
plt.legend()
plt.show(G)
plt.close("all")