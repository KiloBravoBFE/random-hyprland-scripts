# This expects the .csv from the traewelling.de with only line name and the tags ticked.

import csv

with open('export.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader)  # Skip header row

    vehicles = dict()
    models = dict()

    for row in reader:
        if (str(row[0]) == "0"): 
            break

        if row[1] not in models:
            models[row[1]] = 0
        if row[4] not in vehicles:
            vehicles[row[4]] = 0
        models[row[1]] += 1
        vehicles[row[4]] += 1

sorted_vehicles = (sorted(vehicles.items(), key=lambda x: x[1], reverse=True))
#for i in sorted_vehicles:
 #   print(f"{i[0][7:11]}: {i[1]}") if i[0].startswith("moBiel") or i[0].startswith("BVG") or i[0].startswith("VAG") else None

mobiel_sorted = sorted(
    ((k, v) for k, v in vehicles.items() if k.startswith("moBiel")),
    key=lambda x: int(x[0].split()[1]),  # Gets the number after 'moBiel'
    reverse=False
)

for i in mobiel_sorted:
    print(f"{i[0][7:11]}: {i[1]}")