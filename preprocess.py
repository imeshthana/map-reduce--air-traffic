import csv
from collections import defaultdict

input_file = "airport_traffic_2024.csv"
output_file = "flights_by_country_2024.csv"

country_flights = defaultdict(int)

# Reading file with common delimiters
with open(input_file, 'r', encoding='utf-8') as file:
    sample = file.read(2048)
    delimiter = ',' if ',' in sample else '\t'

with open(input_file, 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=delimiter)
    for row in reader:
        if row['YEAR'].strip() == '2024':
            country = row['STATE_NAME'].strip()
            try:
                flights = int(row['FLT_TOT_1'].strip())
            except ValueError:
                flights = 0
            country_flights[country] += flights

with open(output_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Country', 'Total_Flights_2024'])
    for country, total in sorted(country_flights.items()):
        writer.writerow([country, total])

