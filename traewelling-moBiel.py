# ONLY the messages, still export.csv

import csv
import re

def sec_extract_vehicle_number(value):
    lines = value.splitlines()
    for line in lines:
        m = re.search(r'moBiel.*?(\d{3,4})', line, re.IGNORECASE)
        if (m):
            return int(m.group(1))

        m = re.search(r'Vamos.*?(\d{3,4})', line, re.IGNORECASE)
        if (m):
            return int(m.group(1))

        m = re.search(r'M8[CD].*?(\d{3,4})', line)
        if (m):
            return int(m.group(1))

        m = re.search(r'MB4.*?(\d{3,4})', line)
        if (m):
                return int(m.group(1))

        m = re.fullmatch(r'(61|62|73)\d{2}', line.strip())
        if (m):
            return int(line.strip())

    return None




fleet = dict()
#MB4
for i in range(11, 16):
    fleet[int(f"5{i}")] = 0
#M8D
for i in range(60, 96):
    fleet[int(f"5{i}")] = 0
#Vamos
for i in range(1, 41):
    if i > 9:
        fleet[int(f"50{i}")] = 0
    else:
        fleet[int(f"500{i}")] = 0
#69x
for i in range(96, 99):
    fleet[int(f"6{i}")] = 0
# 61xx
for i in range(0, 60):
    if i > 9:
        fleet[int(f"61{i}")] = 0
    else:
        fleet[int(f"610{i}")] = 0
# 62xx
for i in range(96, 100):
    fleet[int(f"62{i}")] = 0  # All > 9
# 63xx
for i in range(0, 8):
    if i > 9:
        fleet[int(f"63{i}")] = 0
    else:
        fleet[int(f"630{i}")] = 0
# 73xx
for i in range(0, 77):
    if i > 9:
        fleet[int(f"73{i}")] = 0
    else:
        fleet[int(f"730{i}")] = 0
# 74xx
for i in range(1, 18):
    if i > 9:
        fleet[int(f"74{i}")] = 0
    else:
        fleet[int(f"740{i}")] = 0


with open('export.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)  # Skip header row

        for row in reader:
            vehicle = sec_extract_vehicle_number(str(row).strip().lstrip("['").rstrip("']").strip())

            if (vehicle is not None):
                if (vehicle not in fleet):
                    fleet[vehicle] = 0
                fleet[vehicle] += 1


sorted_fleet = sorted(fleet.items(), key=lambda x: x[0], reverse=False)

for i in sorted_fleet:
    if (str(i[0]).startswith("9")):
        sorted_fleet.remove(i)

for i in sorted_fleet:
    print(f"moBiel {i[0]}: {i[1]}")


print()
print("Top 20 moBiel vehicles by journeys:")
sorted_fleet = sorted(fleet.items(), key=lambda x: x[1], reverse=True)
for i in range(0,20):
    if (i > 8):
        print(f"{i+1}: moBiel {sorted_fleet[i][0]}: {sorted_fleet[i][1]}")
        continue
    print(f"0{i+1}: moBiel {sorted_fleet[i][0]}: {sorted_fleet[i][1]}")

M8D, M8C, MB4, GTZ8B, C2LE, C2G, C2, O530LE, O530G, Caetano, eCitaro, eCitaroG = 0,0,0,0,0,0,0,0,0,0,0,0
for i in sorted_fleet:
    if (int(i[0]) in range(511, 516)):
        MB4 += i[1]
    elif (int(i[0]) in range(560, 596)):
        M8D += i[1]
    elif (int(i[0]) in range(516, 560)):
        M8C += i[1]
    elif (int(i[0]) in range(5001, 5041)):
        GTZ8B += i[1]
    elif (int(i[0]) in range(6100, 6107)):
        O530LE += i[1]
    elif (int(i[0]) in range(6107, 6110)):
        C2 += i[1]
    elif (int(i[0]) == 6154):
        C2 += i[1]
    elif (int(i[0]) in range(6110, 6160)):
        C2LE += i[1]
    elif (int(i[0]) in range(6296, 6300)):
        Caetano += i[1]
    elif (int(i[0]) in range(6300, 6320)):
        eCitaro += i[1]
    elif (int(i[0]) in range(7301, 7308)):
        O530G += i[1]
    elif (int(i[0]) in range(7308, 7377)):
        C2G += i[1]
    elif (int(i[0]) in range(7401, 7418)):
        eCitaroG += i[1]

print()
print("Top 10 moBiel vehicle types by journeys:")
print(f"01: MB4: {MB4}")
print(f"02: M8D: {M8D}")
print(f"03: M8C: {M8C}")
print(f"04: GTZ8B: {GTZ8B}")
print(f"05: C2LE: {C2LE}")
print(f"06: C2G: {C2G}")
print(f"07: C2: {C2}")
print(f"08: O530LE: {O530LE}")
print(f"09: O530G: {O530G}")
print(f"10: Caetano: {Caetano}")
print(f"11: eCitaro: {eCitaro}")
print(f"12: eCitaroG: {eCitaroG}")  
    
    
