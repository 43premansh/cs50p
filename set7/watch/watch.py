import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    source = re.search(r"https?://(?:www\.)?youtube\.com/embed/(\w+)\"", s)
    try :
        code = source.groups(1)
    except AttributeError :
        return None
    return f"https://youtu.be/{code[0]}"


if __name__ == "__main__":
    main()