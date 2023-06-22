import pandas
import sqlite3
import os
import csv

# Connect to the SQL file
conn = sqlite3.connect('../AISVesselTracks2022.sqlite')

# Create a cursor object to interact with the database
cursor = conn.cursor()

bl_vessel_ids_2022 = [319133800, 477237100]
bl_vessel_dates_2022 = [None] * len(bl_vessel_ids_2022)
for index, vessel_id in enumerate(bl_vessel_ids_2022):

    query = '''
        SELECT
            date(TrackStartTime),
            time(TrackStartTime)
        FROM AISVesselTracks2022
        WHERE MMSI = '{}';
    '''.format(vessel_id)

    cursor.execute(query)
    bl_vessel_dates_2022[index] = [vessel_id, cursor.fetchall()]

print(bl_vessel_dates_2022)

# for dt in results:
#     print(date(dt))

# dates = []
# for date in results:
#     date_decimal = date[0]
#     dt = datetime.datetime.fromordinal(int(date_decimal)) + datetime.timedelta(days=date_decimal % 1) - datetime.timedelta(days=366)
#     dates.append(dt)

# print(dates)

# # Define the path and filename of the output CSV file
# csv_file = '477237100.csv'

# # Write the rows to the CSV file
# with open(csv_file, 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(results)

# # Get the schema of a specific table
# table_name = 'st_spindexAISVesselTracks2022_Shape_rowid'
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