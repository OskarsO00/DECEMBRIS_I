import csv

filename = input("Ievadiet faila nosaukumu: ")

data = []

with open(filename, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(row)

#@# 1.
print("Masiva garums:", len(data))

#$# 2.
print("Pirma elementa saturs:", data[0])

#%# 3.
print("Pirmo 5 elementu saturs:", data[:5])