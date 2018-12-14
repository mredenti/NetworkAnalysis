import networkx as nx 
import pandas as pd
import matplotlib.pyplot as plt
import collections


# path to cleaned file
EVENTS_ATTENDANCE_CLEANED = "NetworkAnalysis/criminal-activity/datasets/cleaned/mafia_bipartite.csv"
# column names - surname will be useful later when we'd like to group them by family
FULLNAME = "fullname"
#FORENAME =  "forename"
SURNAME = "surname" 
EVENT_ID = "event"
# number of events
NUMB_EVENTS = 47


# import cleaned df_events_attendance in pandas df_events_attendanceframe
df_events_attendance = pd.read_csv(EVENTS_ATTENDANCE_CLEANED)
# counting the number events attended per individual - degree - attribute
df_degree = df_events_attendance.groupby([SURNAME, FULLNAME], as_index = False).count()
# change name of column header
df_degree.rename(columns = {EVENT_ID: "eventscount"}, inplace = True)
""" here below we extract the indivuals which are part of a family
"""
# set the number of events participated to as zero
#df_family = df_degree[[SURNAME, FULLNAME]].groupby(SURNAME, as_index = False).count()
# color - family size
#df_family.rename(columns = {FULLNAME: "color"}, inplace = True)
#df_family[df_family["color"] > 1]
#df_degree = df_degree.merge(df_family, on = ["surname"])
#df_family["events count"] = 0

# create graph object from pd df_events_attendanceframe
B = nx.from_pandas_edgelist(df = df_events_attendance, source = FULLNAME, target = EVENT_ID)
# get the two bipartite sets - X will be the indivuals, Y the events
X,Y = nx.bipartite.sets(B)
# convert the bipartite graph to a weighted graph of common participation to an event
G = nx.algorithms.bipartite.weighted_projected_graph(B, X)
# set number of events attended as node attribute
df_degree.set_index(FULLNAME, inplace = True)
nx.set_node_attributes(G, pd.Series(df_degree["eventscount"], index=df_degree.index).to_dict(), "eventscount")
# set surname as attribute
nx.set_node_attributes(G, pd.Series(df_degree[SURNAME], index=df_degree.index).to_dict(), SURNAME)
# edges color
for u,v in G.edges:
    if G.nodes[u][SURNAME] == G.nodes[v][SURNAME]:
        G.edges[u,v]["color"] = "blue"
    else:
        G.edges[u,v]["color"] = "black"
# node color
for v in G.nodes:
    G.nodes[v]["color"] = "red"
# color black "Pino" - the clan boss
G.nodes["Pino"]["color"] = "yellow"
nx.write_gml(G, "NetworkAnalysis/criminal-activity/datasets/graph/individual.gml")
"""
# create graph object from pd df_events_attendanceframe
G = nx.from_pandas_edgelist(df = df_events_attendance, source = FULLNAME, target = EVENT_ID)
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
# put an attribute to the df_events_attendanceframe as number of events the person participated too
# his importance in the clan - size of the node."""