# This expects the .csv from the traewelling.de website in the following format:
# A: journey_type
# B: line_name
# C: arrival_planned
# D: arrival_real
# Please tick the boxes accordingly and rename it export.csv.

import csv
from dateutil import parser

with open('export.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader)  # Skip header row
    total_train, total_localtrain, total_bus, total_tram, total_ferry = 0, 0, 0, 0, 0
    delayed_train, delayed_localtrain, delayed_bus, delayed_tram, delayed_ferry = 0, 0, 0, 0, 0
    delay_amt_train, delay_amt_localtrain, delay_amt_bus, delay_amt_tram, delay_amt_ferry = 0, 0, 0, 0, 0

    for row in reader:
        if (str(row[0]) == "0"):
            break

        eta = parser.isoparse(str(row[2]))
        ata = parser.isoparse(str(row[3]))
        delay = (ata - eta).total_seconds() / 60

        if ((row[0] == 'nationalExpress' or row[0] == 'national') and not str(row[1]).startswith("R")):
            total_train += 1
            delay_amt_train += delay
            if (delay > 6):
                delayed_train += 1
        elif (row[0] == 'regional' or row[0] == 'suburban' or row[0] == 'nationalExpress' and row[1].startswith('R') or row[0] == 'national'):
            total_localtrain += 1
            delay_amt_localtrain += delay
            if (delay > 6):
                delayed_localtrain += 1
        elif (row[0] == 'bus'):
            total_bus += 1
            delay_amt_bus += delay
            if (delay > 6):
                delayed_bus += 1
        elif (row[0] == 'tram'):
            total_tram += 1
            delay_amt_tram += delay
            if (delay > 6):
                delayed_tram += 1
        elif (row[0] == 'ferry'):
            total_ferry += 1
            delay_amt_ferry += delay
            if (delay > 6):
                delayed_ferry += 1
        else:
            raise ValueError(f"Unknown journey type: {row[0]}")
        
    print(f"Total journeys: {total_train + total_localtrain + total_bus + total_tram + total_ferry}")
    print(f"Total train journeys: {total_train} ({delayed_train} delayed, {delay_amt_train:.2f} min delay)")
    print(f"Total local train journeys: {total_localtrain} ({delayed_localtrain} delayed, {delay_amt_localtrain:.2f} min delay)")
    print(f"Total bus journeys: {total_bus} ({delayed_bus} delayed, {delay_amt_bus:.2f} min delay)")
    print(f"Total tram journeys: {total_tram} ({delayed_tram} delayed, {delay_amt_tram:.2f} min delay)")
    print(f"Total ferry journeys: {total_ferry} ({delayed_ferry} delayed, {delay_amt_ferry:.2f} min delay)")
    print(f"Total delay time: {delay_amt_train + delay_amt_localtrain + delay_amt_bus + delay_amt_tram + delay_amt_ferry:.2f} min")
    print(f"Average delay time: {(delay_amt_train + delay_amt_localtrain + delay_amt_bus + delay_amt_tram + delay_amt_ferry) / (delayed_train + delayed_localtrain + delayed_bus + delayed_tram + delayed_ferry) if (delayed_train + delayed_localtrain + delayed_bus + delayed_tram + delayed_ferry) != 0 else 0:.2f} min")
    print(f"Average delay time per journey: {(delay_amt_train + delay_amt_localtrain + delay_amt_bus + delay_amt_tram + delay_amt_ferry) / (total_train + total_localtrain + total_bus + total_tram + total_ferry) if (total_train + total_localtrain + total_bus + total_tram + total_ferry) != 0 else 0:.2f} min")
    print(f"Average delay time per delayed journey: {(delay_amt_train + delay_amt_localtrain + delay_amt_bus + delay_amt_tram + delay_amt_ferry) / (delayed_train + delayed_localtrain + delayed_bus + delayed_tram + delayed_ferry) if (delayed_train + delayed_localtrain + delayed_bus + delayed_tram + delayed_ferry) != 0 else 0:.2f} min")
    print(f"Percentage of delayed journeys: {((delayed_train + delayed_localtrain + delayed_bus + delayed_tram + delayed_ferry) / (total_train + total_localtrain + total_bus + total_tram + total_ferry) * 100) if (total_train + total_localtrain + total_bus + total_tram + total_ferry) != 0 else 0:.2f}%")
    print(f"Percentage of delayed train journeys: {((delayed_train) / (total_train) * 100) if (total_train) != 0 else 0:.2f}%")
    print(f"Percentage of delayed local train journeys: {((delayed_localtrain) / (total_localtrain) * 100) if (total_localtrain) != 0 else 0:.2f}%")
    print(f"Percentage of delayed bus journeys: {((delayed_bus) / (total_bus) * 100) if (total_bus) != 0 else 0:.2f}%")
    print(f"Percentage of delayed tram journeys: {((delayed_tram) / (total_tram) * 100) if (total_tram) != 0 else 0:.2f}%")
    print(f"Percentage of delayed ferry journeys: {((delayed_ferry) / (total_ferry) * 100) if (total_ferry) != 0 else 0:.2f}%")
    print(f"Percentage of delayed journeys per journey type: {((delayed_train + delayed_localtrain) / (total_train + total_localtrain) * 100 if (total_train + total_localtrain) != 0 else 0):.2f}% for train, {((delayed_bus) / (total_bus) * 100 if (total_bus) != 0 else 0):.2f}% for bus, {((delayed_tram) / (total_tram) * 100 if (total_tram) != 0 else 0):.2f}% for tram, {((delayed_ferry) / (total_ferry) * 100 if (total_ferry) != 0 else 0):.2f}% for ferry")    
    print()
    print(f"Average delay per mode of transport:" 
          f"\nTrain: {delay_amt_train / total_train if total_train != 0 else 0:.2f} min"
          f"\nLocal Train: {delay_amt_localtrain / total_localtrain if total_localtrain != 0 else 0:.2f} min"
          f"\nBus: {delay_amt_bus / total_bus if total_bus != 0 else 0:.2f} min"
          f"\nTram: {delay_amt_tram / total_tram if total_tram != 0 else 0:.2f} min"
          f"\nFerry: {delay_amt_ferry / total_ferry if total_ferry != 0 else 0:.2f} min")