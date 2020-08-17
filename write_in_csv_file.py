import csv

l2=[]
header=["Service Area Code", "Phone Numbers", "Preferences", "Opstype", "Phone Type"]
l2.append(header)
for i in range(100000):
    l2.append(["000000", "0000000000", "1#2#3#4#5#6#7#8", "A", i])

with open("/home/neethu/Documents/data_1L.csv", "w", newline="") as file:
    writer=csv.writer(file)
    writer.writerows(l2)
