from tabulate import tabulate
import csv
import sys

if len(sys.argv) > 2 :
    sys.exit("Too many command Line Arguments")
elif not sys.argv[1].endswith(".csv") :
    sys.exit("Not a csv !!")

f = sys.argv[1]
items = []

with open(f) as file :
    try :
        reader = csv.DictReader(file)
    except FileNotFoundError :
        sys.exit("File not found")
    for row in reader :
        items.append(row)

#items is a list of dictionaries now

print(tabulate(items, headers= "keys", tablefmt="grid"))
