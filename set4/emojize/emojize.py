import emoji
import sys


if len(sys.argv) != 2 :
    sys.exit()

s = sys.argv[1]
   
print(emoji.emojize(s, language='alias'))
