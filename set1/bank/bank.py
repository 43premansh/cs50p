def main() :
    print(value(input("Enter the greeting:")))

def value(greet) :
    out = 0
    if greet.lower().startswith('hello'):
        out = 0
    elif greet.lower().startswith('h') :
        out = 20
    else :
        out = 100
    return out 


if __name__ == "__main__" :
    main()