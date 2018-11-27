import networkx as nx 
import pandas as pd
import matplotlib.pyplot as plt

# path to cleaned file
EVENTS_ATTENDANCE_CLEANED = "NetworkAnalysis/criminal-activity/datasets/cleaned/mafia_bipartite.csv"
# column names - surname will be useful later when we'd like to group them by family
FULLNAME = "fullname"
FORENAME =  "forename"
SURNAME = "surname" 
EVENT_ID = "event"


# import cleaned data in pandas dataframe
data = pd.read_csv(EVENTS_ATTENDANCE_CLEANED)
# create graph object from pd dataframe
G = nx.from_pandas_edgelist(df = data, source = FULLNAME, target = EVENT_ID)
# get the two bipartite sets
x,y = nx.bipartite.sets(G)
pos = dict()
# for each person name and event obtain a unique position index
pos.update( (n, (1, i)) for i, n in enumerate(x) ) # put nodes from X at x=1
pos.update( (n, (2, i)) for i, n in enumerate(y) ) # put nodes from Y at x=2
nx.draw(G, pos=pos, node_size = 10)
plt.show()
plt.close("all")
# get the degree distribution for the degree of bipartite set x - the criminals - do it for the families too
degree_sequence = G.degree(x) 
# who are the nodes who participate more often to this meetings - are they the key nodes
# who are the key families?

