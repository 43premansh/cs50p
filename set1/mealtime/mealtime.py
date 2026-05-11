def main():
    time = input("What's the time now? ")
    time = convert(time)
    x1, x2, y1, y2, z1, z2 = 7, 8, 12, 13, 18, 19
    if x2 >= time >= x1 :
        print("Breakfast Time")
    elif y2 >= time >= y1 :
        print("Lunch Time")
    elif z2 >= time >= z1 :
        print("Dinner Time")
    else :
        print("Focus on ur work!!")


def convert(time):
    h, m = time.split(":")
    t =  int(h) + int(m)/60
    return t


if __name__ == "__main__":
    main()