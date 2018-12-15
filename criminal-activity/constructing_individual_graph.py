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
# create graph object from pd df_events_attendanceframe
B = nx.from_pandas_edgelist(df = df_events_attendance, source = FULLNAME, target = EVENT_ID)
# get the two bipartite sets: x will be the indivuals, y the events
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
