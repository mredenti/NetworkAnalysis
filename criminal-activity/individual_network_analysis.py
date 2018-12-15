import networkx as nx
import matplotlib.pyplot as plt
import collections


# path to cleaned file
GRAPH = "NetworkAnalysis/criminal-activity/datasets/graph/individual.gml"
# column names - surname will be useful later when we'd like to group them by family
FULLNAME = "fullname"
#FORENAME =  "forename"
SURNAME = "surname"
EVENT_ID = "event"
# number of events
NUMB_EVENTS = 47
# number of individuals
NUMB_INDIVIDUALS = 156


G = nx.read_gml(GRAPH)
# get edges and respective weight to pass as width attribute
weights = [G[u][v]['weight'] for u, v in G.edges]
# get nodes attributes to pass as size
nodes = G.nodes
# number of events attended
numb_events = [G.nodes[v]['eventscount'] for v in nodes]
edge_color = [G[u][v]['color'] for u, v in G.edges]
# plotting the graph
nx.draw(G, node_size=numb_events, with_labels=False,
        width=weights, edge_color=edge_color)
plt.show(G)
plt.close("all")
# density histogram of degree distribution - numb events attended by individuals
numb_events = collections.Counter(numb_events)
deg, cnt = zip(*numb_events.items())
rel_cnt = list(map(lambda i: i/NUMB_INDIVIDUALS, cnt))
plt.bar(deg, rel_cnt, width=0.80, color='b')
plt.title("Summits Attendance Histogram - 156 individuals, 47 summits", pad=20)
plt.ylabel("Relative node frequency")
plt.xlabel("Number Of Summits")
plt.xlim(left=0.4)
plt.ylim(top=0.5)
plt.xticks(deg)
plt.tight_layout()
plt.grid(axis='y', alpha=0.75)
plt.savefig(
    'NetworkAnalysis/criminal-activity/images/individual_events_distribution.png')
plt.close("all")
# diameter - a measure of the connectedness/familiarità of the members
print("Diameter:", nx.diameter(G), nx.info(G))
print(nx.average_shortest_path_length(G))
