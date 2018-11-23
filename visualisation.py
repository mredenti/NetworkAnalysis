import networkx as nx 
import matplotlib.pyplot as plt


# read graph modeling language file format as network
G = nx.read_gml("NetworkAnalysis/polbooks.gml")
# define a function that assigns a color to each book's attribute
def coloring_books(book):
    # book is liberal
    if book[1]['value'] == 'l':
        book = 'blue'
    # conservative
    elif book[1]['value'] == 'c':
        book = 'red'
    else:
        # 
        book = 'green'
    return book
# color each node depending on if book is conservative, liberal, ...
color_node = list(map(coloring_books, G.nodes(data=True)))
# plot graph - which is the best layout to communicate results?
nx.draw_circular(G, node_size=30, with_labels=False, node_color = color_node)
# add title - not working
plt.title("Amazon Co-Purchased Books") 
plt.show()
plt.close()
# main result: audience of a certain political orientation do not co-purchase books of opposite political opinion