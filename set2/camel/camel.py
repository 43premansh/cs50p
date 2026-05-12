def main() :
    camel = input("camelCase: ")
    snake_case(camel)

def snake_case(x):
    for i in range(len(x)) :
        if x[i].upper() != x[i] :
            print(x[i], end = "")
        else :
            print("_" + x[i].lower(), end = "")
    print()

main()