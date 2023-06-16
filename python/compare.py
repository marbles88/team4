import pandas as pd
import csv

blacklist = pd.read_csv("MMSI.csv", header = None)
ais2021 = pd.read_csv("output2021.csv", header = None)

blacklist.columns = ['id']
ais2021.columns = ['id']

intersect = pd.merge(blacklist,ais2021, on = 'id')

csv_file = 'Intersection2021.csv'
intersect.to_csv(csv_file, index=False)
    