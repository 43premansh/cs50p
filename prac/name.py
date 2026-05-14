import sys

if len(sys.argv) > 2 :
    sys.exit("Too many args !!")
elif len(sys.argv) < 2 :
    sys.exit("Too few arguments!!")

print(f"My name is {sys.argv[1]}")
