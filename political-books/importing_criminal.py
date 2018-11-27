# 2749 nodes
import networkx as nx
import csv


# f is a file object and open is a file method
FILENAME = 'NetworkAnalysis/criminal-activity/CRIMINALNETDATA.txt'


with open(FILENAME, 'r') as f:
    # read the file opened in read mode - tab delimiter - method works for parsing any text delimited files
    reader = csv.reader(f, delimiter="\t")
    # store nodes in a list
    nodes = set()
    for row in reader:
        try:
            nodes.add(row[0])
            nodes.add(row[1])
        except IndexError:
            pass
    # get the directed edges as tuples
    edges = [tuple(e) for e in reader][4:]
    # close file
    f.close()

G = nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)