from PIL import Image, ImageOps
import sys


if len(sys.argv) != 3 :
    sys.exit("num of args isnt 3")

elif not (sys.argv[1].endswith((".png", "jpeg", "jpg"))) :
    sys.exit("input is not an image")
elif not (sys.argv[2].endswith((".png", "jpeg", "jpg"))) :
    sys.exit("output file is not an image file")

else :
    one =  sys.argv[1].split(".")
    two =  sys.argv[2].split(".")
    if one[1] != two[1] :
        sys.exit("out and in formats dont match")


try :
    input_i = Image.open(sys.argv[1]).convert("RGBA")
except FileNotFoundError:
    sys.exit("provided input was not found")

shirt = Image.open("shirt.png").convert("RGBA")

photo = ImageOps.fit(input_i, shirt.size)

photo.paste(shirt, mask = shirt)

photo.save(sys.argv[2])
