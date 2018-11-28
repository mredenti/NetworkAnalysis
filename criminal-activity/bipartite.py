import networkx as nx 
import pandas as pd
import matplotlib.pyplot as plt
import collections

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
member_degree = G.degree(x) 
# who are the nodes who participate more often to this meetings - are they the key nodes
# who are the key families?
def hub(member_degree):
    # iter creates an object which can be iterated one element at a time
    iter_member_degree = iter(member_degree)
    maximum = next(iter_member_degree)
    for _ in range(len(member_degree)):
        try:
            trial = next(iter_member_degree)
            if trial[1] > maximum[1]:
                maximum = trial
            else: 
                pass
        except StopIteration:
            break
    return maximum

maximum = hub(member_degree)


# degree distribution: few nodes participate to many of the events, but no one person participates to all
# events - but maybe one family participates to all events
degree_sequence = sorted([degree for name, degree in G.degree(x)], reverse=True)  # degree sequence
# now count the frequency of each degree 
degree_count = collections.Counter(degree_sequence)
degree, frequency = zip(*degree_count.items())
# plot graph 
plt.bar(degree, frequency, color = 'b')
plt.title("Degree Distribution")
plt.xlabel("Degree - Number of events attended")
plt.ylabel("Frequency")
plt.show()
plt.close("all")
# put an attribute to the dataframe as number of events the person participated too
# his importance in the clan - size of the node.