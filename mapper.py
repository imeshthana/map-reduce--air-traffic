
import sys
import csv

reader = csv.reader(sys.stdin)
next(reader)  # Skip header

for row in reader:
    if len(row) < 2:
        continue
    country = row[0].strip()
    try:
        flights = int(row[1].strip())
        print(f"{country}\t{flights}")
    except ValueError:
        continue
