"""This script cleans the csv file 
   containing the network data. The main issue
   is the header row which the name of the restaurant
   comma separated by the date. 
   Just convert the header to integers identifiers preseving
   the chronological order of the events.
"""
import csv


EVENTS_ATTENDANCE_ORIGINAL = "NetworkAnalysis/criminal-activity/datasets/original/NDRANGHETAMAFIA_2M.csv"
# save cleaned file to a new file
EVENTS_ATTENDANCE_CLEANED = "NetworkAnalysis/criminal-activity/datasets/cleaned/mafia_bipartite.csv"


with open(EVENTS_ATTENDANCE_ORIGINAL, 'r') as f, open(EVENTS_ATTENDANCE_CLEANED, 'w') as w:
   # reader - eyes
   reader = csv.reader(f)
   # skip header row
   header = next(reader)
   # set new header - 
   new_header = ["surname", "forename", "fullname", "event"] 
   # write new header, join takes a list and joins the items in this case separating them with a comma
   w.write("{}\n".format(','.join(new_header)))
   # go to second line
   row = next(reader)
   # while roe is non-empty
   while row:
      # get the full name of the person
      fullname = row[0]
      if fullname.split(' ')[0] == "DE":
         surname = fullname.split(' ')[1].title()
      else:
         surname = fullname.split(' ')[0].title()
      # split the name into surname and forename - ignore middle name
      forename = fullname.split(' ')[-1]
      # now count the numb of events attended
      booleans = [int(boolean) for boolean in row[1:]] 
      # which events did he participate to - the 1's
      events = [event for event,boolean in enumerate(booleans) if boolean == 1]
      for i in range(len(events)):
         # set a new row
         new_row = [forename, surname, fullname, str(events[i])]
         # write new row to the file
         w.write("{}\n".format(','.join(new_row)))
      # move onto new row
      try:
         row = next(reader)
      # if line is empty python raises an error
      except StopIteration:
         # in this case set the row to None - this way "while row" will give False
         row = None