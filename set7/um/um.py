import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    c = 0
    k = ""
    for i in s :
        if i != " ":
            k += i.lower()
        else :
            
            if k.startswith("um") and (k.endswith((".", ",", " ", "\n")) ):
                c+= 1
            k = ""


    if k.startswith("um") and (k.endswith((".", ",", " ", "\n", "", "?")) ):
        c+= 1

    return c





    


if __name__ == "__main__":
    main()