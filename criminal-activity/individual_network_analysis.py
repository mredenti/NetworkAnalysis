import networkx as nx 
import matplotlib.pyplot as plt


# path to cleaned file
GRAPH = "NetworkAnalysis/criminal-activity/datasets/graph/individual.gml"
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
nodes = G.nodes
# number of events attended
numb_events = [G.nodes[v]['eventscount']*10 for v in nodes]
edge_color = [G[u][v]['color'] for u,v in G.edges]
# plotting the graph
nx.draw(G, node_size = numb_events , with_labels = False, width = weights, edge_color = edge_color)
plt.show(G)
plt.close("all")