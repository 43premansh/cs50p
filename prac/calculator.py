def square(n) :
    return n*n

def main() :
    x = int(input())
    return square(x)


if __name__ == "__main__": # without this importing it to other programs will cause problems
    main()