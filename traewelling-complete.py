# ONLY the messages, still export.csv

import csv
import re

mobiel_fleet = dict()
#MB4
for i in range(11, 16):
    mobiel_fleet[int(f"5{i}")] = 0
#M8D
for i in range(60, 96):
    mobiel_fleet[int(f"5{i}")] = 0
#Vamos
for i in range(1, 41):
    if i > 9:
        mobiel_fleet[int(f"50{i}")] = 0
    else:
        mobiel_fleet[int(f"500{i}")] = 0
#69x
for i in range(96, 99):
    mobiel_fleet[int(f"6{i}")] = 0
# 61xx
for i in range(0, 60):
    if i > 9:
        mobiel_fleet[int(f"61{i}")] = 0
    else:
        mobiel_fleet[int(f"610{i}")] = 0
# 62xx
for i in range(96, 100):
    mobiel_fleet[int(f"62{i}")] = 0  # All > 9
# 63xx
for i in range(0, 8):
    if i > 9:
        mobiel_fleet[int(f"63{i}")] = 0
    else:
        mobiel_fleet[int(f"630{i}")] = 0
# 73xx
for i in range(0, 77):
    if i > 9:
        mobiel_fleet[int(f"73{i}")] = 0
    else:
        mobiel_fleet[int(f"730{i}")] = 0
# 74xx
for i in range(1, 18):
    if i > 9:
        mobiel_fleet[int(f"74{i}")] = 0
    else:
        mobiel_fleet[int(f"740{i}")] = 0


def sec_extract_vehicle_number(value):

    lines = value.splitlines()
    for line in lines:
        m = re.search(r'moBiel.*?(\d{3,4})', line, re.IGNORECASE)
        if (m):
            return ("moBiel",int(m.group(1)))

        m = re.search(r'Vamos.*?(\d{3,4})', line, re.IGNORECASE)
        if (m):
            return ("moBiel",int(m.group(1)))

        m = re.search(r'M8[CD].*?(\d{3,4})', line)
        if (m):
            return ("moBiel",int(m.group(1)))

        m = re.search(r'MB4.*?(\d{3,4})', line)
        if (m):
                return ("moBiel",int(m.group(1)))

        m = re.fullmatch(r'(61|62|73)\d{2}', line.strip())
        if (m):
            return ("moBiel",int(line.strip()))
        
        m = re.fullmatch(r'(61|62|73)\d{4}', line.strip())
        if (m):
            return ("moBiel",int(line.strip()))
        
        m = re.match(r'^(61|62|73)\d{2,}', line.strip())
        if (m):
            return ("moBiel", int(m.group(0)))
        
        m = re.match(r'Rasche\s+(\d{3,4})', line, re.IGNORECASE)
        if (m):
            return ("Rasche", int(m.group(1)))
        
        m = re.search(r'VT\s+(\d{3}\s+\d{3})', line, re.IGNORECASE)
        if (m):
            return ("VT", m.group(1))
        
        m = re.search(r'Wellhausen.*?(\d{3,4})', line, re.IGNORECASE)
        if (m):
            return ("Wellhausen",int(m.group(1)))
        
        m = re.search(r'WH(\d{3})', line, re.IGNORECASE)
        if m:
            return ("Wellhausen", int(m.group(1)))
        
        m = re.search(r'Motzek.*?(\d{3,4})', line, re.IGNORECASE)
        if (m):
            return ("Motzek",int(m.group(1)))
        
        m = re.search(r'PaderSprinter.*?(\d{2,4})', line, re.IGNORECASE)
        if (m):
            return ("PaderSprinter",int(m.group(1)))
        
        m = re.search(r'KVP.*?(\d{3,4})', line, re.IGNORECASE)
        if (m):
            return ("Kraftverkehrsgesellschaft Paderborn",int(m.group(1)))
        
        m = re.search(r'Kraftverkehrsgesellschaft Paderborn.*?(\d{3,4})', line, re.IGNORECASE)
        if (m):
            return ("Kraftverkehrsgesellschaft Paderborn",int(m.group(1)))
        
        m = re.search(r'Mietrach.*?(\d{3,4})', line, re.IGNORECASE)
        if (m):
            return ("Mietrach",int(m.group(1)))
        
        m = re.search(r'Leeker.*?(\d{3,4})', line, re.IGNORECASE)
        if (m):
            return ("Leeker",int(m.group(1)))
        
        m = re.fullmatch(r'Brandt.*?(\d{3,4})', line, re.IGNORECASE)
        if (m):
            return ("Brandt",int(m.group(1)))
        
        m = re.search(r'Stötzel.*?(\d{3,4})', line, re.IGNORECASE)
        if (m):
            return ("Stötzel",int(m.group(1)))
        
        m = re.search(r'Redecker.*?(\d{3,4})', line, re.IGNORECASE)
        if (m):
            return ("Redecker",int(m.group(1)))
        
        m = re.search(r'Niemeyer.*?(\d{3,4})', line, re.IGNORECASE)
        if (m):
            return ("Niemeyer",int(m.group(1)))
        
        m = re.fullmatch(r'BVO.*?(\d{3,4})', line, re.IGNORECASE)
        if (m):
            return ("BVO",int(m.group(1)))
        
        m = re.search(r'BVO\s+(\d{3,4})', line, re.IGNORECASE)
        if (m):
            return ("BVO", int(m.group(1)))
        
        m = re.search(r'TWV.*?(\d{3,4})', line, re.IGNORECASE)
        if (m):
            return ("Teutoburger Wald Verkehr",int(m.group(1)))
        
        m = re.search(r'TD.*?(\d{3,4})', line, re.IGNORECASE)
        if (m):
            return ("Teutoburger Wald Verkehr",int(m.group(1)))
        
        m = re.search(r'Transdev OWL.*?(\d{3,4})', line, re.IGNORECASE)
        if (m):
            return ("Teutoburger Wald Verkehr",int(m.group(1)))
        
        m = re.fullmatch(r'ASEAG.*?(\d{3,4})', line, re.IGNORECASE)
        if (m):
            return ("ASEAG",int(m.group(1)))
        
        m = re.search(r'RRX\s+(\d{3}\s+\d{3})', line, re.IGNORECASE)
        if (m):
            return ("RRX", m.group(1))
        
        
        m = re.search(r'KVB.*?(\d{3,4})', line, re.IGNORECASE)
        if (m):
            return ("KVB",int(m.group(1)))
        
        m = re.fullmatch(r'Rosenkranz.*?(\d{2,4})', line, re.IGNORECASE)
        if (m):
            return ("Rosenkranz",int(m.group(1)))
        
        m = re.search(r'Orth.*?(\d{3,4})', line, re.IGNORECASE)
        if m:
            return ("Orth", int(m.group(1)))

        m = re.search(r'Rosenkranz.*?(\d{2,4})', line, re.IGNORECASE)
        if (m):
            return ("Rosenkranz",int(m.group(1)))
        
        m = re.search(r'Ostwestfalen.*?(\d{3,4})', line, re.IGNORECASE)
        if (m):
            return ("BVO",int(m.group(1)))
        
        m = re.search(r'Heeperhölzer\s+(\d{3,4})', line, re.IGNORECASE)
        if m:
            return ("Der Heeperhölzer", int(m.group(1)))
        
        m = re.search(r'Taeter.*?(\d{3,4})$', line.strip(), re.IGNORECASE)
        if (m):
            return ("Taeter", int(m.group(1)))
        
        m = re.search(r'Bröskamp.*?(\d{3,4})', line, re.IGNORECASE)
        if (m):
            return ("Bröskamp", int(m.group(1)))
        
        m = re.search(r'Wittler.*?(\d{3,4})', line, re.IGNORECASE)
        if (m):
            return ("Wittler", int(m.group(1)))     

        m = re.search(r'Königsborner.*?(\d{3,4})', line, re.IGNORECASE)
        if m:
            return ("Königsborner", int(m.group(1)))
        
        m = re.search(r'Hermesmeyer\s([A-Z]{2})\s(\d{2,4})$', line.strip(), re.IGNORECASE)
        if m:
            code = m.group(1).upper()  # e.g., "LA", "BF", "BD"
            number = int(m.group(2))   # e.g., 65
            return ("Hermesmeyer", f"{code} {number}")
        
        m = re.search(r'Rheinbahn.*?(\d{3,4})$', line.strip(), re.IGNORECASE)
        if (m):
            return ("Rheinbahn", int(m.group(1)))
        
        m = re.search(r'National Express.*?(\d{3,4})', line, re.IGNORECASE)
        if m:
            return ("National Express", int(m.group(1)))
        
        m = re.search(r'NordWestBahn.*?(\d{3,4})', line, re.IGNORECASE)
        if m:
            return ("VT", f"643 {m.group(1)}")
        
        m = re.search(r'M/F\s+([^\d\n]+)', line, re.IGNORECASE)
        if m:
            return ("ferry", m.group(1).strip())
        
        m = re.search(r'M/S\s+([A-Za-zÄÖÜäöüß\s\-]+?)(?=[\r\n\(\:\-]|$)', line, re.IGNORECASE)
        if m:
            ferry_name = m.group(1).strip()
            if ferry_name.lower() != "estonia":
                return ("ferry", ferry_name)
        
        m = re.search(r'Tz.*?(\d{3,4})', line, re.IGNORECASE)
        if (m and int(m.group(1))!=412):
            return ("ICE", int(m.group(1)))
        
        m = re.search(r'Sieckendiek.*?(\d{3,4})', line, re.IGNORECASE)
        if m:
            return ("Sieckendiek", int(m.group(1)))
        
        m = re.search(r'Oester-Barkey.*?(\d{3,4})', line, re.IGNORECASE)
        if m:
            return ("Oester-Barkey", int(m.group(1))) 
        
        m = re.search(r'Bernie Reisen.*?(\d{3,4})', line, re.IGNORECASE)
        if m:
            return ("Bernie Reisen", int(m.group(1))) 
        
        m = re.search(r'Stadtbus Gütersloh.*?(\d{2,3})', line, re.IGNORECASE)
        if m:
            return ("Stadtbus Gütersloh", int(m.group(1)))
        
        m = re.search(r'Höber.*?(\d{3,4})', line, re.IGNORECASE)
        if m:
            return ("Höber", int(m.group(1))) 
        
        m = re.search(r'X31K.*?(\d{4})', line, re.IGNORECASE)
        if m:
            return ("Øresundståg", int(m.group(1))) 
        m = re.search(r'Skåne.*?(\d{4})', line, re.IGNORECASE)
        if m:
            return ("Øresundståg", int(m.group(1))) 
        m = re.search(r'DSB ET.*?(\d{4})', line, re.IGNORECASE)
        if m:
            return ("Øresundståg", int(m.group(1))) 
        m = re.search(r'Västtåg.*?(\d{4})', line, re.IGNORECASE)
        if m:
            return ("Västtåg", int(m.group(1))) 
        
        m = re.search(r'DSB MF.*?(\d{4})', line, re.IGNORECASE)
        if m:
            return ("DSB", int(m.group(1)))
        
        m = re.search(r'DSB FH.*?(\d{4})', line, re.IGNORECASE)
        if m:
            return ("DSB", int(m.group(1)))
        
        m = re.search(r'DSB EC.*?(\d{4})', line, re.IGNORECASE)
        if m:
            return ("DSB", int(m.group(1)))
        m = re.search(r'DSB,.*?(\d{4})', line, re.IGNORECASE)
        if m:
            return ("DSB", int(m.group(1))) 
        
        m = re.search(r'\bET\s+(\d+(?:\.\d+)+)[a-h]?', line, re.IGNORECASE)
        if m:
            return ("ET", m.group(1))
        
        m = re.search(r'ET\s+(\d{3}\s+\d{3})', line, re.IGNORECASE)
        if (m):
            return ("ET", m.group(1))
        
        m = re.search(r'VT.*?(\d\.\d{2})[a-h]?', line, re.IGNORECASE)
        if m:
            return ("VT", m.group(1))
        
        m = re.search(r'Hochbahn.*?(\d{3,4})', line, re.IGNORECASE)
        if m:
            return ("Hochbahn", int(m.group(1))) 
        
        m = re.search(r'DT\s+5\s+(\d{3}(?:-\d)?)', line, re.IGNORECASE)
        if m:
            return ("Hochbahn", "DT 5 "+m.group(1))
        
        m = re.search(r'Böddeker.*?(\d{3,4})', line, re.IGNORECASE)
        if m:
            return ("Böddeker", int(m.group(1))) 
        
        m = re.search(r'Emsdettener.*?(\d{3,4})', line, re.IGNORECASE)
        if m:
            return ("Emsdettener", int(m.group(1))) 
        
        m = re.search(r'Erfmann.*?(\d{3,4})', line, re.IGNORECASE)
        if m:
            return ("Erfmann", int(m.group(1))) 
        
        m = re.search(r'VR.*?(\d{3,4})', line, re.IGNORECASE)
        if m:
            return ("VR Sverige", int(m.group(1))) 
        
        m = re.search(r'SL.*?(\d{3,4})', line, re.IGNORECASE)
        if m:
            return ("Storstockholms Lokaltrafik", int(m.group(1))) 
        
        m = re.search(r'Tholen Busreise.*?(\d{3,4})', line, re.IGNORECASE)
        if m:
            return ("Tholen", int(m.group(1))) 
        
        m = re.search(r'Omnibus Kückelheim.*?(\d{3,4})', line, re.IGNORECASE)
        if m:
            return ("Kückelheim", int(m.group(1))) 
        
        m = re.search(r'Reifers Reisen.*?(\d{3,4})', line, re.IGNORECASE)
        if m:
            return ("Reifers", int(m.group(1))) 
        
        m = re.search(r'Kanalreisen Kruse.*?(\d{3,4})', line, re.IGNORECASE)
        if m:
            return ("Kanalreisen Kruse", int(m.group(1))) 
        
        m = re.search(r'Held Reisen.*?(\d{3,4})', line, re.IGNORECASE)
        if m:
            return ("Held Reisen", int(m.group(1))) 
        
        m = re.search(r'Edzards.*?(\d{3,4})', line, re.IGNORECASE)
        if m:
            return ("Edzards-Reisen", int(m.group(1)))
        
        m = re.search(r'Stoffregen.*?(\d{2,3})', line, re.IGNORECASE)
        if m:
            return ("Stoffregen", int(m.group(1)))
        
        m = re.search(r'(Spiekeroog\s+[IVXLCDM]+)', line, re.IGNORECASE)
        if m:
            return ("ferry", m.group(1))

        m = re.search(r'SkyTrain\s+(\d\.\d{1})[a-h]?', line, re.IGNORECASE)
        if m:
            return ("SkyTrain", m.group(1))

        m = re.search(r'GSAB.*?(\d{2,3})', line, re.IGNORECASE)
        if m:
            return ("Göteborgs Spårvägar", int(m.group(1)))
        
        m = re.search(r'Keolis.*?(\d{3,4})', line, re.IGNORECASE)
        if m:
            return ("Keolis", int(m.group(1)))
        
        m = re.search(r'Nobina.*?(\d{2,4})', line, re.IGNORECASE)
        if m:
            return ("Nobina", int(m.group(1)))
        
        m = re.search(r'Transdev.*?(\d{2,4})', line, re.IGNORECASE)
        if m:
            return ("Transdev", int(m.group(1)))
        
        m = re.search(r'Ukna.*?(\d{3,4})', line, re.IGNORECASE)
        if m:
            return ("Ukna Busstrafik", int(m.group(1)))
        
        m = re.search(r'Leja-Touring.*?(\d{4,5})', line, re.IGNORECASE)
        if m:
            return ("Leja-Touring", int(m.group(1)))

        m = re.search(r'Sana Transport.*?(\d{3,4})', line, re.IGNORECASE)
        if m:
            return ("Sana Transport", int(m.group(1)))

        m = re.search(r'BVG.*?(\d{3,4})', line, re.IGNORECASE)
        if m:
            return ("Berliner Verkehrsbetriebe", int(m.group(1)))
        
        m = re.search(r'Schröder Reisen.*?(\d{3,4})', line, re.IGNORECASE)
        if m:
            return ("Schröder Reisen", int(m.group(1)))

        m = re.search(r'Ruhrbahn.*?(\d{3,4})', line, re.IGNORECASE)
        if (m):
            return ("Ruhrbahn",int(m.group(1)))
        
        m = re.search(r'Carlsteins.*?(\d{3,4})', line, re.IGNORECASE)
        if (m):
            return ("Carlsteins",int(m.group(1)))
        
        m = re.search(r'Vy Buss.*?(\d{3,4})', line, re.IGNORECASE)
        if (m):
            return ("Vy Buss",int(m.group(1)))

        m = re.search(r'Josef Rettler.*?(\d{3,4})', line, re.IGNORECASE)
        if (m):
            return ("Josef Rettler",int(m.group(1)))
        
        m = re.search(r'Wächter.*?(\d{3,4})', line, re.IGNORECASE)
        if (m):
            return ("Willi Wächter",int(m.group(1)))
        
        m = re.search(r'Lippemobil.*?(\d{3,4})', line, re.IGNORECASE)
        if (m):
            return ("Lippemobil",int(m.group(1)))

        m = re.search(r'\b(973|974|975)\b', line)
        if m:
            return ("Stötzel", int(m.group(1)))
        
        if re.search(r'9857', line):
            return ("Redecker", 9857)
        
        if re.search(r'932', line):
            return ("Wellhausen", 932)
        
        if re.search(r'922', line):
            return ("Motzek", 922)
        
        if re.search(r'7354', line):
            return ("moBiel", 7354)
        if re.search(r'1125', line):
            return ("moBiel", 1125)


        
        
        m = re.fullmatch(r'73\d{2}', line.strip())
        if (m and int(line.strip()) in mobiel_fleet):
            return ("moBiel", int(line.strip()))
        
        m = re.fullmatch(r'^(\d{3,4})$', line.strip(), re.IGNORECASE)
        if (m and int(m.group(1)) in mobiel_fleet):
            return ("moBiel", int(m.group(1)))
        
        m = re.search(r'(\d{3,4})', line)
        if (m and int(m.group(1)) in mobiel_fleet):
            return ("unknown", int(m.group(1)))

        
        m = re.search(r'^(\d{3,4})', line.strip(), re.IGNORECASE)
        if (m and int(m.group(1)) in mobiel_fleet):
            return ("Unknown", int(m.group(1)))
        
        m = re.fullmatch(r'^(\d{3,4})$', line.strip(), re.IGNORECASE)
        if (m):
            return ("Unknown", int(m.group(1)))
        

        print(f"Unknown vehicle number in line: {line}")
    return None

fleet = dict()

with open('export-3.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)  # Skip header row

        for row in reader:
            data = sec_extract_vehicle_number(str(row).strip().lstrip("['").rstrip("']").strip())
            vehicle = data[1] if data is not None else None
            operator = data[0] if data is not None else None

            #print(operator, vehicle)

            if (operator == "unknown"):
                if (vehicle in mobiel_fleet):
                    if ("moBiel" not in fleet):
                        fleet["moBiel"] = dict()
                    if (vehicle not in fleet["moBiel"]):
                        fleet["moBiel"][vehicle] = 0
                    fleet["moBiel"][vehicle] += 1
                continue

            if (operator is not None):
                if (operator not in fleet):
                    fleet[operator] = dict()
            if (vehicle is not None):
                if (vehicle not in fleet[operator]):
                    fleet[operator][vehicle] = 0
                fleet[operator][vehicle] += 1
                


for operator in fleet:
    fleet[operator] = dict(sorted(fleet[operator].items(), key=lambda x: x[1], reverse=True))
sorted_fleet = sorted(fleet.items(), key=lambda x: x[0], reverse=False)
for operator in fleet:
    sum = 0
    for vehicle in fleet[operator]:
        sum += fleet[operator][vehicle]
    #print(f"({sum}) - {operator}:")
    for vehicle in fleet[operator]:
        pass
        #print(f"  {vehicle}: {fleet[operator][vehicle]}")



with open("output.txt", "w", encoding="utf-8") as f:
    for operator in fleet:
        fleet[operator] = dict(sorted(fleet[operator].items(), key=lambda x: x[1], reverse=True))
        sorted_fleet = sorted(fleet.items(), key=lambda x: x[0], reverse=False)
    for operator in fleet:
        f.write(f"{operator}:\n")
        for vehicle in fleet[operator]:
            f.write(f"  {vehicle}: {fleet[operator][vehicle]}\n")

    f.write("\n \n")
    sums = dict()
    for operator in fleet:
        sum = 0
        for vehicle in fleet[operator]:
            sum += fleet[operator][vehicle]
        sums[operator] = sum
    sorted_sums = sorted(sums.items(), key=lambda x: x[1], reverse=True)
    for operator, sum in sorted_sums:
        f.write(f"({sum}) - {operator}\n")






# VEHICLE TYPE STATISTICS

def fleet_range(start, end, taxonomy):
    return (range(start, end + 1), taxonomy)


CLASSIFICATION_RULES = {

    "PaderSprinter": [
        fleet_range(11, 12, "MAN/LionsCity/A21/NL313"),
        fleet_range(13, 17, "MAN/LionsCity/A21/NL323"),
        fleet_range(18, 59, "MB/Citaro/C2/3D"),
        fleet_range(111, 183, "MB/Citaro/C2/G/4D"),
        fleet_range(301, 301, "MB/Citaro/eCitaro/FuelCell/G/4D"),
    ],

    "BVO": [
        fleet_range(663, 683, "MB/Citaro/eCitaro/2D"),
        fleet_range(938, 942, "MAN/LionsCity/12C/NL330/EfficientHybrid"),
        fleet_range(1300, 1308, "MAN/LionsIntercity/43C/LE360/EfficientHybrid"),
        fleet_range(2127, 2133, "MAN/LionsIntercity/32C/LE330/EfficientHybrid"),
        fleet_range(4100, 4119, "MAN/LionsCity/12C/NL330/EfficientHybrid"),
        fleet_range(4140, 4147, "IVECO/Crossway/LE/12M"),
        fleet_range(4189, 4193, "MAN/LionsCity/A20/NÜ323"),
        fleet_range(4300, 4303, "MAN/LionsCity/18C/NG360/EfficientHybrid"),
        fleet_range(4343, 4343, "MB/Citaro/C2/G/3D"),
        fleet_range(4347, 4348, "MAN/LionsCity/A23/NG363"),
        fleet_range(4361, 4363, "MB/Citaro/C2/G/4D"),
    ],

    "Kraftverkehrsgesellschaft Paderborn": [
        fleet_range(201, 208, "MB/Citaro/C2/G/4D"),
        fleet_range(214, 215, "MB/Citaro/C2/3D"),
        fleet_range(216, 219, "MB/Citaro/C2/G/4D"),
    ],

    "moBiel": [
        fleet_range(696, 698, "MB/Citaro/Facelift/K/2D"),
        fleet_range(767, 773, "MB/Citaro/Facelift/G/3D"),
        fleet_range(1125, 1125, "MB/Citaro/C2/LE/2D"),
        fleet_range(6100, 6107, "MB/Citaro/Facelift/LE/2D"),
        fleet_range(6108, 6109, "MB/Citaro/C2/2D"),
        fleet_range(6110, 6129, "MB/Citaro/C2/LE/2D"),
        fleet_range(6130, 6159, "MB/Citaro/C2/LE/Hybrid/2D"),
        fleet_range(6296, 6299, "Caetano/H2.CityGold/2D"),
        fleet_range(6300, 6307, "MB/Citaro/eCitaro/FuelCell/2D"),
        fleet_range(7300, 7309, "MB/Citaro/Facelift/G/3D"),
        fleet_range(7310, 7356, "MB/Citaro/C2/G/3D"),
        fleet_range(7357, 7376, "MB/Citaro/C2/G/Hybrid/3D"),
        fleet_range(7400, 7419, "MB/Citaro/eCitaro/FuelCell/G/3D"),

        fleet_range(511, 515, "DUEWAG/MB4"),
        fleet_range(516, 559, "DUEWAG/M8C"),
        fleet_range(560, 595, "DUEWAG/M8D"),
        fleet_range(5001, 5040, "HeiterBlick/GTZ8-B/Vamos"),
    ],

    "Rasche":[
        fleet_range(907, 908, "MB/Citaro/C2/2D"),
        fleet_range(910, 910, "MB/Citaro/C2/2D"),
        fleet_range(914, 914, "MB/Citaro/C2/2D"),
        fleet_range(923, 923, "MAN/LionsCity/12C/NL330/EfficientHybrid"),
        fleet_range(953, 955, "Solaris/Urbino/III/12"),
        fleet_range(963, 963, "MB/Citaro/C2/LE/Hybrid/2D"),
        fleet_range(9815, 9815, "MB/Citaro/C2/G/Hybrid/3D"),
        fleet_range(9840, 9840, "Solaris/Urbino/III/12"),
        fleet_range(9861, 9862, "MB/Citaro/C2/G/3D"),
        fleet_range(9870, 9870, "Solaris/Urbino/IV/12"),
        fleet_range(9986, 9986, "MB/Citaro/C2/G/Hybrid/3D"),
    ],

    "Motzek": [
        fleet_range(921, 921, "MB/Citaro/Facelift/LE/2D"),
        fleet_range(922, 923, "MB/Citaro/C2/LE/2D"),
        fleet_range(924, 924, "MB/Citaro/Facelift/LE/2D"),
        fleet_range(925, 925, "MB/Citaro/C2/LE/2D"),
        fleet_range(927, 928, "MB/Citaro/Facelift/2D"),
        fleet_range(929, 929, "MB/Citaro/Vorfacelift/2D"),
        fleet_range(9776, 9778, "MB/Citaro/eCitaro/2D"),
    ],

    "Wellhausen": [
        fleet_range(931, 931, "MB/Citaro/C2/2D"),
        fleet_range(932, 933, "MB/Citaro/C2/LE/2D"),
        fleet_range(934, 934, "MB/Citaro/Vorfacelift/2D"),
        fleet_range(937, 937, "MB/Citaro/C2/2D"),
        fleet_range(972, 972, "MB/Citaro/C2/2D"),
    ],

    "Redecker": [
        fleet_range(3000, 3000, "MB/Citaro/C2/LE/Hybrid/2D"),
        fleet_range(9343, 9343, "MB/Citaro/CapaCity/L/4D"),
        fleet_range(9700, 9703, "MB/Citaro/eCitaro"),
        fleet_range(9817, 9825, "MB/Citaro/C2/2D"),
        fleet_range(9843, 9843, "MB/Citaro/C2/2D"),
        fleet_range(9844, 9844, "MB/Citaro/C2/G/3D"),
        fleet_range(9855, 9855, "MB/Citaro/C2/G/Hybrid/3D"),
        fleet_range(9857, 9857, "MB/Citaro/C2/G/Hybrid/3D"),
        fleet_range(9859, 9859, "MB/Citaro/CapaCity/L/4D"),
        fleet_range(9869, 9869, "MB/Citaro/C2/G/3D"),
    ],

    "Oester-Barkey": [
        fleet_range(991, 992, "MB/Citaro/C2/LE/Ü/2D"),
        fleet_range(994, 995, "Setra/S415/LE/Business"),
        fleet_range(6605, 6606, "MB/Citaro/C2/LE/Ü/2D"),
        fleet_range(6608, 6609, "Setra/S415/LE/Business"),
        fleet_range(6611, 6612, "Setra/S415/NF"),
    ],

    "Teutoburger Wald Verkehr": [
        fleet_range(1026, 1083, "IVECO/Crossway/LE/12M"),
        fleet_range(4006, 4006, "MB/Citaro/C2/G/3D"),
        fleet_range(6010, 6015, "IVECO/Crossway/LE/12M"),
    ],

    "Niemeyer": [
        fleet_range(913, 914, "MAN/LionsCity/A78/EL293"),
        fleet_range(915, 915, "MB/Citaro/C2/LE/2D"),
        fleet_range(916, 917, "MAN/LionsCity/A78/EL293"),
        fleet_range(918, 918, "MB/Citaro/Facelift/LE/2D"),
    ],

    "Stötzel": [
        fleet_range(390, 390, "IVECO/Crossway/LE/12M"),
        fleet_range(440, 440, "MB/Citaro/C2/LE/2D"),
        fleet_range(910, 910, "IVECO/Crossway/LE/12M"),
        fleet_range(973, 974, "MB/Citaro/C2/G/3D"),
        fleet_range(975, 975, "MB/Citaro/C2/LE/Hybrid/2D"),
        fleet_range(977, 977, "MB/Citaro/C2/G/4D"),
        fleet_range(978, 981, "MB/Citaro/C2/LE/2D"),
        fleet_range(9847, 9848, "MB/Citaro/C2/2D"),
        fleet_range(9849, 9849, "MB/Citaro/C2/G/3D"),
        fleet_range(9850, 9851, "MB/Citaro/C2/2D"),
        fleet_range(9925, 9945, "IVECO/Crossway/Facelift/LE/12M"),
        fleet_range(9967, 9973, "MB/Citaro/C2/G/3D"),
    ],

    "Sieckendiek": [
        fleet_range(6600, 6600, "MAN/LionsCity/A21/LE/NLxx3"),
        fleet_range(6800, 6800, "MAN/LionsCity/A21/NLxx3"),
    ],

    "Bröskamp": [
        fleet_range(9031, 9031, "MB/Citaro/C2/LE/2D"),
    ],

    "Mietrach": [
        fleet_range(905, 905, "Solaris/Urbino/IV/12"),
        fleet_range(907, 907, "MAN/LionsCity/A21/NLxx3"),
        fleet_range(909, 909, "Solaris/Urbino/III/12"),
        fleet_range(960, 960, "MAN/LionsCity/A21/NLxx3"), # same as 907
    ],

    "Der Heeperhölzer": [
        fleet_range(9822, 9822, "MB/Citaro/C2/G/3D"),
        fleet_range(9831, 9831, "MB/Citaro/Facelift/2D"),
        fleet_range(9833, 9833, "MB/Citaro/C2/G/3D"),
    ],

    "Leeker": [
        fleet_range(440, 440, "MB/Citaro/C2/LE/2D"),
        fleet_range(700, 700, "Setra/S415/LE/Business"),
        fleet_range(8080, 8080, "MB/Citaro/C2/LE/2D"),
    ],

    "Orth": [
        fleet_range(110, 110, "MB/Tourismo/II/RHD/16M"),
        fleet_range(333, 333, "IVECO/Crossway/LE/12M"),
        fleet_range(1050, 1050, "IVECO/Crossway/LE/12M"),
    ],

    "Willi Wächter": [
        fleet_range(770, 770, "Setra/S415/LE/Business"),
    ],

    "Josef Rettler": [
        fleet_range(870, 870, "MB/Citaro/C2/LE/2D"),
    ],

    "Held Reisen": [
        fleet_range(116, 116, "Scania/Citywide/LFA/II/18M"),
    ],

    "Wittler": [
        fleet_range(245, 245, "MB/Citaro/C2/LE/Hybrid/2D"),
    ],

    "Königsborner": [
        fleet_range(367, 367, "MB/Citaro/C2/2D"),
    ],

    "Stadtbus Gütersloh": [
        fleet_range(25, 25, "MB/Citaro/C2/LE/2D"),
    ],

    "Rosenkranz": [
        fleet_range(4257, 4257, "IVECO/Crossway/LE/12M"),
    ],

    "Böddeker": [
        fleet_range(1080, 1083, "MB/Citaro/C2/2D"),
    ],

    "Höber": [
        fleet_range(506, 506, "MAN/LionsCity/A78/LE/ELxx3"),
    ],

    "Reifers": [
        fleet_range(400, 400, "MAN/LionsCity/A21/NLxx3"),
    ],

    "Bernie Reisen": [
        fleet_range(2480, 2480, "MB/Citaro/C2/G/NGT/4D"),
        fleet_range(4280, 4280, "MB/Citaro/Facelift/G/CNG/3D"),
    ],

    "Erfmann": [
        fleet_range(5411, 5468, "MB/Citaro/C2/G/3D"),
    ],

    "Kückelheim": [
        fleet_range(9411, 9411, "MB/Citaro/C2/Hybrid/2D"),
    ],

    "Edzards-Reisen": [
        fleet_range(252, 252, "Setra/S431/DT"),
        fleet_range(254, 254, "MB/Intouro/III/L"),
        fleet_range(298, 298, "Setra/S415/LE/Business"),
    ],

    "Stoffregen": [
        fleet_range(15, 15, "MAN/LionsRegio/R14/ÜL364"),
        fleet_range(66, 66, "VanHool/TDX25/Astromega"),
    ],

    "Emsdettener": [
        fleet_range(130, 130, "Setra/S517/HD"),
    ],

    "Kanalreisen Kruse": [
        fleet_range(441, 441, "MAN/LionsRegio/R12/ÜLxx4"),
    ],

    "Tholen": [
        fleet_range(972, 972, "MB/Citaro/Facelift/G/3D"),
    ],

    "Berliner Verkehrsbetriebe": [
        fleet_range(1000, 1199, "MB/Citaro/C2/2D"),
        fleet_range(1801, 1815, "Solaris/Urbino/IV/electric/12"),
        fleet_range(1816, 1830, "MB/Citaro/C2/eCitaro/2D"),
        fleet_range(3550, 3749, "AlexanderDennis/Enviro/500/MMC"),
        fleet_range(4426, 4781, "Scania/Citywide/LFA"),
        fleet_range(4785, 5415, "MB/Citaro/C2/G/3D"),
        fleet_range(5420, 5709, "Solaris/Urbino/IV/electric/18"),

        fleet_range(2904, 3013, "ABB/F92"),
        fleet_range(6001, 6019, "Stadler/JK/24"),
        fleet_range(8001, 8040, "Bombardier/Flexity/Berlin/GT8/11/ERL"),
        fleet_range(9001, 9157, "Bombardier/Flexity/Berlin/GT8/11/ZRL"),
    ],

    "Schröder Reisen": [
        fleet_range(8640, 8659, "MAN/LionsCity/12C/NL330/EfficientHybrid"),
    ],

    "ASEAG": [
        fleet_range(227, 302, "MB/Citaro/Facelift/G/3D"),
        fleet_range(504, 509, "MB/Citaro/C2/G/Ü/3D")
    ],

    "Taeter": [
        fleet_range(1914, 1914, "MB/Citaro/Facelift/G/3D"),
    ],

    "Ruhrbahn": [
        fleet_range(1051, 1082, "Bombardier/Flexity/Essen/M8D-NF4"),
        fleet_range(1501, 1534, "ADtranz/Flexity/Classic/M8D-NF"),
        fleet_range(1601, 1627, "Bombardier/Flexity/Essen/M8D-NF2"),
        fleet_range(5191, 5145, "DUEWAG/B80C"),
        fleet_range(5221, 5230, "York/Docklands/P89"),
        fleet_range(5231, 5240, "LHB/Docklands/P86"),
        fleet_range(5303, 5321, "CAF/N6D-HF1"),
    ],

    "KVB": [
        fleet_range(2201, 2260, "DUEWAG/B80D"),
        fleet_range(2301, 2333, "DUEWAG/B80D"),
        fleet_range(5101, 5215, "Bombardier/Flexity/Swift/K5000"),
    ],

    "Rheinbahn": [
        fleet_range(4002, 4288, "DUEWAG/B80D"),
        fleet_range(8342, 8398, "MAN/LionsCity/A23/NG363"),
    ],

    "Hochbahn": [
        fleet_range(4001, 4960, "MB/Citaro/CapaCity/L/5D"),
        fleet_range(7430, 7458, "MB/Citaro/C2/G/3D"),
        fleet_range(8209, 8244, "MB/Citaro/C2/3D"),
    ],

    "Göteborgs Spårvägar": [
        fleet_range(300, 380, "ASEA/M31"),
        fleet_range(401, 465, "AnsaldoBreda/Sirio/M32"),
        fleet_range(490, 499, "Bombardier/Flexity/M33B"),
        fleet_range(501, 540, "Bombardier/Flexity/M33"),
        fleet_range(601, 660, "Bombardier/Flexity/M34"),
        fleet_range(701, 770, "ASEA/M28"),
        fleet_range(801, 860, "Hägglunds/M29"),
    ],

    "Vy Buss": [
        fleet_range(2402, 2445, "Volvo/7900/A/Electric"),
        fleet_range(2451, 2452, "Volvo/7900/Electric"),
    ],

    "Nobina": [
        fleet_range(350, 379, "Volvo/7900/Electric"),
        fleet_range(4674, 4674, "MAN/LionsIntercity/44C/LE320"),
        fleet_range(4793, 4793, "MAN/LionsIntercity/43C/LE280"),
    ],

    "Transdev": [
        fleet_range(8500, 8522, "MB/Citaro/CapaCity/L/4D"),
    ],

    "Ukna Busstrafik": [
        fleet_range(1002, 1004, "Setra/S416/LE/Business"),
    ],

    "Leja-Touring": [
        fleet_range(55336, 55347, "MAN/LionsCity/A44/LE/L/NL323")
    ],

    "Keolis" :[
        fleet_range(7636, 7636, "Volvo/8900/LE/14.8M"),
    ],

    "Sana Transport": [
        fleet_range(7406, 7406, "VDL/Bova/Synergy/DD")
    ],

    "Carlsteins": [
        fleet_range(3211, 3220, "Volvo/8900/15M"),
    ],

    "VR Sverige": [
        fleet_range(7781, 7908, "Scania/OmniLink/CK270UA/6x2/2LB"),
        fleet_range(8401, 8414, "Scania/OmniLink/CK280UA/6x2/2LB"),
    ],

    "ICE": [

        fleet_range(1, 100, "ICE/ICE1"),
        fleet_range(101, 200, "ICE/ICE2"),
        fleet_range(301, 406, "ICE/ICE3"),
    ],

    "Västtåg": [
        fleet_range(9041, 9074, "Bombardier/Regina/X52"),
    ],

    "Øresundståg": [
        fleet_range(4000, 5000, "Bombardier/CrusalisContessa/X31K"),
    ],

    "DSB": [
        fleet_range(400, 417, "Talgo/203/EC"),
        fleet_range(5001, 5096, "ABB/IC3/MFA"),
        fleet_range(5201, 5296, "ABB/IC3/MBF"),
        fleet_range(5401, 5496, "ABB/IC3/FF"),
        fleet_range(5601, 5683, "AnsaldoBreda/MG/IC4"),
        fleet_range(5801, 5883, "AnsaldoBreda/MG/IC4"),
        fleet_range(6601, 6683, "AnsaldoBreda/FH/IC4"),
        fleet_range(6801, 6883, "AnsaldoBreda/FG/IC4"),
    ],
 
    "ICE": [
        fleet_range(1, 190, "SIEMENS/401/ICE1"),
        fleet_range(201,244, "SIEMENS/402/ICE2"),
        fleet_range(301, 363, "SIEMENS/403/ICE3"),
        fleet_range(4601, 4617, "SIEMENS/406/ICE3M"),
        fleet_range(4701, 4717, "SIEMENS/407/ICE3"),
        fleet_range(8001, 8999, "SIEMENS/408/ICE3neo"),
        fleet_range(1101, 1199, "SIEMENS/411/ICET"),
        fleet_range(1501, 1531, "SIEMENS/415/ICET"),
        fleet_range(9001, 9999, "SIEMENS/412/ICE4"),                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
    ],

    "National Express": [
        fleet_range(350, 370, "Bombardier/TALENT/2")
    ],

    "Storstockholms Lokaltrafik": [
        fleet_range(423, 423, "Bombardier/Flexity/Swift/A32"),
        fleet_range(2000, 2500, "Bombardier/C20"),
        fleet_range(6149, 6149, "Alstom/Coradia/Nordic/X60"),
    ],
}



SPECIAL_VEHICLES = {

    ("moBiel", 6115):
        "MB/Citaro/C2/LE/Ü/2D",

    ("moBiel", 6154):
        "MB/Citaro/Hybrid/2D",

    ("Hochbahn", 8242):
        "MB/Citaro/Facelift/2D",

}

STRING_CLASSIFICATION_RULES = {

    "Hermesmeyer": [
        (r"BD \d{2}", "MB/Citaro/C2/3D"),(r"BE \d{2}", "MB/Citaro/C2/3D"),(r"BF \d{2}", "MB/Citaro/C2/3D"),(r"BI \d{2}", "MB/Citaro/C2/3D"),(r"BN \d{2}", "MB/Citaro/C2/3D"),
        (r"BZ \d{2}", "MB/Citaro/C2/3D"),(r"LA \d{2}", "MB/Citaro/C2/3D"),(r"LF \d{2}", "MB/Citaro/C2/3D"),(r"LN \d{2}", "MB/Citaro/C2/3D"),(r"BD \d{2}", "MB/Citaro/C2/3D"),
        (r"BC \d{2}", "MB/Citaro/C2/3D"), (r"LW \d{2}", "MB/Citaro/C2/G/3D"), (r"LE \d{2}", "MB/Citaro/C2/LE/2D"), (r"LG \d{2}", "MB/Citaro/C2/LE/Hybrid/2D"), (r"LM \d{2}", "MB/Citaro/C2/LE/Hybrid/2D"),
        (r"LI \d{2}", "MB/Citaro/C2/G/Hybrid/3D"), (r"BO \d{2}", "MB/Citaro/Facelift/2D"), (r"BX \d{2}", "MB/Citaro/Facelift/2D"), (r"LO \d{2}", "MB/Citaro/Facelift/G/3D"),
        (r"LT \d{2}", "MB/Citaro/Facelift/LE/Ü/2D"), (r"LV \d{2}", "Solaris/Urbino/III/18"), (r"BY \d{2}", "Setra/S415/LE/Business"), (r"GY \d{2}", "Setra/S515/LE"), (r"LY \d{2}", "Setra/S415/LE/Business"),
    ],

    "RRX": [
        (r"^462 \d{3}$", "SIEMENS/DesiroHC/RRX"),
    ],

    "VT": [
        (r"^643 2\d{2}$", "Bombardier/TALENT/1/643/2-Teiler"),
        (r"^643 3\d{2}$", "Bombardier/TALENT/1/643/3-Teiler"),
        (r"^643 7\d{2}$", "Bombardier/TALENT/1/643/3-Teiler"),
        (r"^644 \d{3}$", "Bombardier/TALENT/1/644"),
        (r"^\d\.\d{2}$", "Bombardier/TALENT/1/643/3-Teiler"),
    ],

    "ET": [
        (r"^4\.\d{2}$", "Stadler/FLIRT/ET4"),
        (r"^5\.\d{2}$", "Stadler/FLIRT/ET5"),
        (r"^6\.\d{2}$", "Stadler/FLIRT/ET6"),
        (r"^7\.\d{2}$", "Stadler/FLIRT/ET7"),
        (r"^8\.\d{2}$", "Stadler/FLIRT/ET8"),
        (r"^445 \d{3}$", "Bombardier/Twindexx/445"),
        (r"^481 \d{3}$", "Bombardier/481"),
        (r"^484 \d{3}$", "Stadler/484"),
    ],

    "SkyTrain": [
        (r"\d.\d", "SIEMENS/SIPEM/SkyTrain"),
    ],

    "Hochbahn": [
        (r"^DT 5 \d{3}-\d", "Alstom/DT5"),
        (r"^DT 5 \d{3}", "Alstom/DT5"),
    ],
}



LABELS = {

    "MB": "Mercedes-Benz",

    "ICE1": "ICE 1",
    "ICE2": "ICE 2",
    "ICE3": "ICE 3",
    "ICE3M": "ICE 3M",
    "ICE3neo": "ICE 3neo",
    "ICE4": "ICE 4",
    "ICET": "ICE T",
    "ICETD": "ICE TD",
}



def classify_vehicle(operator, vehicle):

    key = (operator, vehicle)

    if key in SPECIAL_VEHICLES:
        return SPECIAL_VEHICLES[key]

    rules = CLASSIFICATION_RULES.get(operator, [])

    if isinstance(vehicle, int):
        for vehicle_range, taxonomy in rules:
            if vehicle in vehicle_range:
                return taxonomy

    string_rules = STRING_CLASSIFICATION_RULES.get(operator, [])

    if isinstance(vehicle, str):
        for pattern, taxonomy in string_rules:
            if re.fullmatch(pattern, vehicle):
                return taxonomy

    return None



def insert_tree(tree, taxonomy, count):

    parts = taxonomy.split("/")

    current = tree

    for part in parts:

        if part not in current:

            current[part] = {
                "_count": 0,
                "_children": {}
            }

        current[part]["_count"] += count

        current = current[part]["_children"]


def pretty(part):
    return LABELS.get(part, part)



taxonomy_tree = {}

unclassified = {}

for operator in fleet:

    for vehicle in fleet[operator]:

        trip_count = fleet[operator][vehicle]

        taxonomy = classify_vehicle(
            operator,
            vehicle
        )

        if taxonomy is None:

            key = f"{operator} {vehicle}"

            unclassified[key] = (
                unclassified.get(key, 0)
                + trip_count
            )

            continue

        insert_tree(
            taxonomy_tree,
            taxonomy,
            trip_count
        )



COUNT_WIDTH = 8


def write_tree(f, tree, prefix=""):

    items = sorted(
        tree.items(),
        key=lambda x: x[1]["_count"],
        reverse=True
    )

    for index, (name, data) in enumerate(items):

        is_last = index == len(items) - 1

        branch = "└── " if is_last else "├── "

        f.write(
            f"{data['_count']:>{COUNT_WIDTH}} "
            f"{prefix}{branch}"
            f"{pretty(name)}\n"
        )

        next_prefix = (
            prefix + ("    " if is_last else "│   ")
        )

        write_tree(
            f,
            data["_children"],
            next_prefix
        )




specific_types = {}

for operator in fleet:

    for vehicle in fleet[operator]:

        trip_count = fleet[operator][vehicle]

        taxonomy = classify_vehicle(
            operator,
            vehicle
        )

        if taxonomy is None:
            continue

        specific_types[taxonomy] = (
            specific_types.get(taxonomy, 0)
            + trip_count
        )




with open(
    "output-vehicle-types.txt",
    "w",
    encoding="utf-8"
) as f:

    f.write(
        "=== VEHICLE TYPE TREE ===\n\n"
    )

    write_tree(
        f,
        taxonomy_tree
    )

    f.write(
        "\n\n=== MOST SPECIFIC TYPES ===\n\n"
    )

    for taxonomy, count in sorted(
        specific_types.items(),
        key=lambda x: x[1],
        reverse=True
    ):

        pretty_name = " ".join(
            pretty(part)
            for part in taxonomy.split("/")
        )

        f.write(
            f"{count:>{COUNT_WIDTH}} "
            f"{pretty_name}\n"
        )

    f.write(
        "\n\n=== UNCLASSIFIED VEHICLES ===\n\n"
    )

    for vehicle, count in sorted(
        unclassified.items(),
        key=lambda x: x[1],
        reverse=True
    ):

        f.write(
            f"{count:>{COUNT_WIDTH}} "
            f"{vehicle}\n"
        )

print(
    "Vehicle statistics written to "
    "output-vehicle-types.txt"
)