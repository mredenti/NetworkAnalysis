# NetworkAnalysis
This project aims to analyse a network of criminal activity and investigate the which families are most important /the head of the snake. Also, by finding the clusters, we could observe which families are tightly bond to each other - they might carry out some particular business. The data has been reconstructed by the document "ORDINANZA DI APPLICAZIONE DI MISURA COERCITIVA con mandato di cattura - art. 292 c.p.p. -" which is available at
[link to network data](https://sites.google.com/site/ucinetsoftware/datasets/covert-networks/ndranghetamafia2).

The dataset has been reconstructed by mostly referring to pp.87-110 of the document named "Operazione Infinito". This report is a judicial document concerning the pre-trial detention order triggered by the the preliminary investigation judge (Giudice per le indagini preliminari) of Milan. With this judicial act, measures of custody and pretrial detention have been ordered for the reported suspected of 'Ndrangheta affiliation.

## Title: "Exposing the criminal structure of mafia groups"
Important: 1 degree - the activity of the family/gang members
           2 degree - weighted degree - level of co-participation (no) - whether the node is present at the most 
           important meetings?d


# Data Description 
156 x 47 Bipartite graph - persons X events (summits), undirected binary ties.
Attendance at events have been registered by police authorities through wiretapping and observations during the large investigation called "Operazione Infinito". 

156 Nodes - Ndrangheta members + events (meetings attended by the criminal to discuss activity and other matters)

## Graph conversion 
Edges - co-presence of the same family/people at an event.

Nodes have been given an attribute symbolising the frequency of appearances at these events - family importance.