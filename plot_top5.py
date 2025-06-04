import matplotlib.pyplot as plt

# Read the output from Hadoop
countries = []
flights = []

with open("top5countries.txt", "r") as file:
    for line in file:
        country, total = line.strip().split('\t')
        countries.append(country)
        flights.append(int(total))

# Plotting
plt.figure(figsize=(10, 6))
plt.bar(countries, flights, color='skyblue')
plt.title('Top 5 Busiest Countries by Total Flights (2024)')
plt.xlabel('Country')
plt.ylabel('Total Flights')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
