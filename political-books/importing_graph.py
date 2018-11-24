import networkx as nx
import matplotlib.pyplot as plt


G = nx.read_gml("NetworkAnalysis/polbooks.gml")
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
