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
        
        m = re.search(r'Padersprinter.*?(\d{2,4})', line, re.IGNORECASE)
        if (m):
            return ("Padersprinter",int(m.group(1)))
        
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
            return ("TWV",int(m.group(1)))
        
        m = re.search(r'TD.*?(\d{3,4})', line, re.IGNORECASE)
        if (m):
            return ("TWV",int(m.group(1)))
        
        m = re.search(r'Transdev OWL.*?(\d{3,4})', line, re.IGNORECASE)
        if (m):
            return ("TWV",int(m.group(1)))
        
        m = re.fullmatch(r'ASEAG.*?(\d{3,4})', line, re.IGNORECASE)
        if (m):
            return ("ASEAG",int(m.group(1)))
        
        m = re.search(r'RRX\s+(\d{3}\s+\d{3})', line, re.IGNORECASE)
        if (m):
            return ("RRX", m.group(1))
        
        m = re.fullmatch(r'ET.*?(\d{3,4})', line, re.IGNORECASE)
        if (m):
            return ("ET",int(m.group(1)))
        
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
        
        m = re.search(r'Hermesmeyer.*?(\d{2,4})$', line.strip(), re.IGNORECASE)
        if (m):
            return ("Hermesmeyer", int(m.group(1)))
        
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
        
        m = re.search(r'X31K.*?(\d{4})', line, re.IGNORECASE)
        if m:
            return ("Øresundstog", int(m.group(1))) 
        m = re.search(r'Skåne.*?(\d{4})', line, re.IGNORECASE)
        if m:
            return ("Øresundstog", int(m.group(1))) 
        m = re.search(r'DSB ET.*?(\d{4})', line, re.IGNORECASE)
        if m:
            return ("Øresundstog", int(m.group(1))) 
        
        m = re.search(r'DSB MF.*?(\d{4})', line, re.IGNORECASE)
        if m:
            return ("DSB", int(m.group(1)))
        
        m = re.search(r'DSB,.*?(\d{4})', line, re.IGNORECASE)
        if m:
            return ("DSB", int(m.group(1))) 
        
        m = re.search(r'ET\s+(\d\.\d{2})[a-h]?', line, re.IGNORECASE)
        if m:
            return ("ET", m.group(1))
        
        m = re.search(r'VT(\d\.\d{2})[a-h]?', line, re.IGNORECASE)
        if m:
            return ("VT", m.group(1))
        
        m = re.search(r'Hochbahn.*?(\d{3,4})', line, re.IGNORECASE)
        if m:
            return ("Hochbahn", int(m.group(1))) 
        
        m = re.search(r'DT\s+5\s+(\d{3}(?:-\d)?)', line, re.IGNORECASE)
        if m:
            return ("Hochbahn DT 5", m.group(1))
        
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
            return ("Edzards", int(m.group(1)))
        
        m = re.search(r'Stoffregen.*?(\d{2,3})', line, re.IGNORECASE)
        if m:
            return ("Stoffregen", int(m.group(1)))
        
        m = re.search(r'(Spiekeroog\s+[IVXLCDM]+)', line, re.IGNORECASE)
        if m:
            return ("ferry", m.group(1))

        m = re.search(r'SkyTrain\s+(\d\.\d{1})[a-h]?', line, re.IGNORECASE)
        if m:
            return ("SkyTrain", m.group(1))

        
        
        
        


        

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
    print(f"{operator}:")
    for vehicle in fleet[operator]:
        print(f"  {vehicle}: {fleet[operator][vehicle]}")



with open("output.txt", "w", encoding="utf-8") as f:
    for operator in fleet:
        fleet[operator] = dict(sorted(fleet[operator].items(), key=lambda x: x[1], reverse=True))
        sorted_fleet = sorted(fleet.items(), key=lambda x: x[0], reverse=False)
    for operator in fleet:
        f.write(f"{operator}:\n")
        for vehicle in fleet[operator]:
            f.write(f"  {vehicle}: {fleet[operator][vehicle]}\n")


