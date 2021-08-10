#!/bin/python3

import pandas as pd
'''
Collects data of the csv file we 
just downloaded from wireshark 
'''
data = pd.read_csv("packets.csv")

'''
Assigns Source and Destination to a variable
'''

source_ip = data["Source"].unique()
destination_ip = data["Destination"].unique()

d= {}
for i in source_ip:
  file = open("source", "a")
  file.write(f"{i}\n")

for n in destination_ip:
  file2 = open("destination", "a")
  file2.write(f"{n}\n")

'''
Append txt files to a new dictionary
'''
with open("source", "r") as f, open("destination", "r") as x:
  h = {line1.strip():line2.strip() for line1, line2 in zip(f,x)}
with open("Source&Destination", "w") as out:
  for k,v in h.items():
      out.write("{} =====> {}\n".format(k,v))







