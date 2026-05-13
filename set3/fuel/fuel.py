#create a getint function which prompts the user to get the no. desired 
#and catches ValueError and Divisionby zero error
#if the percentage is less than 1 output E
#if the percentage is greater than 99 output F
def main() :
    z = getper("what's x?", "what's y?")
    if z == 0 :
        print("E") 
    elif z == 99 :
        print("F")
    else :
        print(f"{z}%")
    

def getper(prompt1, prompt2) :
    while True :
        try :
            x = int(input(prompt1))
            y = int(input(prompt2))

            return int((x/y)*100)
        except ValueError :
            print("the input is not an integer, put in a integer")
        except ZeroDivisionError :
            print("input a positive integer in y, cant divide with 0")
        else :
            break

main()
        
