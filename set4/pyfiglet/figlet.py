import pyfiglet
import sys
import random


if (sys.argv[1] == '-f' or sys.argv[1] == '--font') and sys.argv[2] in pyfiglet.FigletFont.getFonts() :
    pass
else :
    sys.exit("error")

print(pyfiglet.figlet_format(input("Input: "), font=sys.argv[2].lower()))
