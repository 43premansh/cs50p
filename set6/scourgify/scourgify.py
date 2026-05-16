import csv
import sys


if len(sys.argv) < 3:
    sys.exit("Too few args!!")

elif len(sys.argv) > 3:
    sys.exit("Too many args!!")


i = sys.argv[1]
o = sys.argv[2]


try:
    with open(i) as in_file:
        reader = csv.DictReader(in_file)
        for row in reader:
            first, last = row["name"].split()
            first = first[:-1]
            last = last[:-1]
            house = row["house"]
            with open(o, "a") as out_file:
                writer = csv.writer(out_file)
                writer.writerow([first, last, house])
except FileNotFoundError:
    sys.exit(f"couldnt read {i} !!")
