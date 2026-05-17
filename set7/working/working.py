import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):

    if "to" in s:
        s = s.split(" to ")
    else:
        raise ValueError
    st = s[0].split(" ")
    et = s[1].split(" ")

    if st[0].endswith("60") or et[0].endswith("60"):
        raise ValueError

    start = st[0].split(":")
    if start[0] > 12:
        raise ValueError
    if len(start) != 2:
        start.append("00")

    end = et[0].split(":")
    if end[0] > 12:
        raise ValueError
    if len(end) != 2:
        end.append("00")

    if st[1] == "PM":
        start[0] = str(int(start[0]) + 12)
    if et[1] == "PM":
        end[0] = str(int(end[0]) + 12)

    if int(start[0]) < 10:
        start[0] = f"0{int(start[0])}"

    if int(end[0]) < 10:
        end[0] = f"0{int(end[0])}"

    return f'{start[0]}:{start[1]} to {end[0]}:{end[1]}'


if __name__ == "__main__":
    main()
