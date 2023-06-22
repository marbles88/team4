import pandas
import sqlite3
import os
import csv

# Connect to the SQL file
conn = sqlite3.connect('../AISVesselTracks2021.gpkg')

# Create a cursor object to interact with the database
cursor = conn.cursor()

bl_vessel_ids_2021 = [319133800, 248233000, 374811000, 574004860]
bl_vessel_dates_2021 = [None] * len(bl_vessel_ids_2021)
for index, vessel_id in enumerate(bl_vessel_ids_2021):

    query = '''
        SELECT
            date(TrackStartTime),
            time(TrackStartTime)
        FROM AISVesselTracks2021
        WHERE MMSI = '{}';
    '''.format(vessel_id)

    cursor.execute(query)
    bl_vessel_dates_2021[index] = [vessel_id, cursor.fetchall()]

print(bl_vessel_dates_2021)

# query = '''
#     SELECT MMSI
#     FROM AISVesselTracks2021;
# '''
# # Execute the query
# cursor.execute(query)

# # Fetch the results
# results = cursor.fetchall()
# print(results)

# csv_file = 'output2021.csv'
# with open(csv_file, 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(results)

# # Define the path and filename of the output CSV file
# csv_file = '477237100.csv'

# # Write the rows to the CSV file
# with open(csv_file, 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(results)

# # Get the schema of a specific table
# table_name = 'AISVesselTracks2021'
# cursor.execute(f"PRAGMA table_info({table_name});")
# table_info = cursor.fetchall()
# print(f"\nSchema for table '{table_name}':")
# for column in table_info:
#     print(f"Column name: {column[1]}, Data type: {column[2]}")

# cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
# tables = cursor.fetchall()

# cursor.execute("SELECT * FROM sqlite_master WHERE type='table'")
# table_details = cursor.fetchall()

# print("Tables:")
# for table in tables:
#     print(table[0])

# print("\nTable Details:")
# for table_detail in table_details:
#     print(table_detail)

# Close the cursor and connection
cursor.close()
conn.close()