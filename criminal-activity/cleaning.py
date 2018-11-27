"""This script cleans the csv file 
   containing the network data. The main issue
   is the header row which the name of the restaurant
   comma separated by the date. 
   Just convert the header to integers identifiers preseving
   the chronological order of the events.
"""
import csv


EVENTS_ATTENDANCE_ORIGINAL = "criminal-activity/datasets/original/NDRANGHETAMAFIA_2M.csv"
# save cleaned file to a new file
EVENTS_ATTENDANCE_CLEANED = "criminal-activity/datasets/cleaned/mafia_bipartite.csv"
