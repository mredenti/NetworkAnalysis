import networkx as nx
import matplotlib.pyplot as plt
import collections


G = nx.read_gml("NetworkAnalysis/political-books/polbooks.gml")
# general network information
info = nx.info(G)
# adjacency matrix
adj_matrix = nx.adjacency_matrix(G)
# nodes' names - book titles
book_titles = G.nodes
# density of graph - nb of edges/potential nb of edges
density = nx.density(G)
# finding the shortest path between two nodes - !undirected graph!
# nx.shortest_path(G, source=id_name, target=id_name_string)
# diameter - not relevant in this case - raises error if graph is disconnected -> find diameter on largest component
diameter = nx.diameter(G)
# check if graph is connected
connected_or_not = nx.is_connected(G)
# get list of components of graph
components = nx.connected_components(G)
# find largest component - other heys/filter are possible
largest_component = max(components, key=len)
# Create a "subgraph" of just the largest component
subgraph = G.subgraph(largest_component)
# clustering coefficient for entire graph
graph_clustering_coeffcien = nx.transitivity(G)
# get degree distribution - G.degree is a dictionary of key,values pairs
#for n,d in G.degree():
    #print("title:", n, ",", "degree:" d)
# or nx.degree_histogram(G)
degree_sequence = sorted([degree for name, degree in G.degree()], reverse=True)  # degree sequence
# now count the frequency of each degree 
degree_count = collections.Counter(degree_sequence)
degree, frequency = zip(*degree_count.items())
# plot graph 
plt.bar(degree, frequency, color = 'b')
plt.title("Degree Distribution")
plt.xlabel("Degree")
plt.ylabel("Frequency")
plt.show()
plt.close("all")
# Comment: from the degree distribution we can observe that there are few books
#  ("main resource of a political party") (a small variety) which are co-purchased with
#  many other books (maily purchased)-
# so perhaps they are the leading books. On the other hand a great variety of books as small number 
# of co-purchases, meaning that they might be preferred at the discretion of the reader. 
# Try the degree distribution for each bubble (conservative, liberal) - different behaviour?
# bubble within the bubble? - separating set 

# maximum degree
max_degree = max(degree_sequence)
# which book was mostly purchased? - assuming same frequency (weight 1)
book_most_purchased = filter(lambda d: d[1]==25, G.degree()) # wrong; do it for each type of book - conservative/liberal.
