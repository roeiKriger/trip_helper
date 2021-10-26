import csv

counter = 0
dict = {}
with open("uscities.csv") as cities:
    reader = csv.reader(cities)
    dict = {rows[0] for rows in reader}

print(dict)
print("aa")


