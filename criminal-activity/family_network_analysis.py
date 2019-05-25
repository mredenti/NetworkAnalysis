import networkx as nx 
import matplotlib.pyplot as plt
import collections


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
numb_events = [G.nodes[v]['eventscount'] for v in G.nodes]
family_size = [G.nodes[v]['familysize'] for v in G.nodes]
# plotting the graph
nx.draw(G, node_size = numb_events , with_labels = False, alpha=0.7, width = weights, node_color = family_size)
plt.legend()
plt.show(G)
plt.close("all")
# denisity histogram of degree distribution - numb events attended by individuals
numb_families = 109
numb_events = collections.Counter(numb_events)
deg, cnt = zip(*numb_events.items())
rel_cnt = list(map(lambda i: i/numb_families, cnt))
plt.bar(deg,rel_cnt, width=0.80, color='b')
plt.title("Summits Attendance Histogram - 156 families/individuals, 47 summits", pad = 20)
plt.ylabel("Relative frequency")
plt.xlabel("Number Of Summits")
plt.xlim(left = 0.4)
plt.ylim(top = 0.5)
plt.xticks(deg)
plt.tight_layout()
plt.grid(axis='y', alpha=0.75)
plt.savefig('NetworkAnalysis/criminal-activity/images/family_events_distribution.png')
plt.close("all")
print("Diameter:", nx.diameter(G))
print(nx.average_shortest_path_length(G))