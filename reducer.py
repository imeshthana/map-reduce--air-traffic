#!/usr/bin/env python3
import sys
from collections import defaultdict

country_flights = defaultdict(int)

for line in sys.stdin:
    parts = line.strip().split('\t')
    if len(parts) != 2:
        continue
    country, flights = parts
    try:
        flights = int(flights)
    except ValueError:
        continue
    country_flights[country] += flights

# Sort and get top 5
top_5 = sorted(country_flights.items(), key=lambda x: x[1], reverse=True)[:5]

for country, total in top_5:
    print(f"{country}\t{total}")

