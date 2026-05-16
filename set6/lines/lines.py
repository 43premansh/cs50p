import sys

if len(sys.argv) != 2:
    sys.exit("Too many command line arguments.")
elif not sys.argv[1].endswith('.py'):
    sys.exit("Not a python file !")


try :
    with open(sys.argv[1]) as file:
        lines = file.readlines()
except FileNotFoundError :
    sys.exit("File Not Found!!")

n = 0
for line in lines:
    if line.strip() == "" or line.strip().startswith("#"):
        n += 1

print(len(lines) - n)
