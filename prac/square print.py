def main() :
    print_square(3)

def print_square(size) :

    #for iterating over rows
    for i in range(size) :

        #for laying each brick in the row
        for j in range(size) :
            print("#", end = "")

        #for the new line needed when we are done with the row
        print()

main()