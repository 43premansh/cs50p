Total = 0
while True :
    
    x = int(input("How much are you putting in? "))

    if x in [25, 10, 5]:
        #accept and add it to the total amt he input into the machine
        Total += x
        if (Total - 50) > 0  :
            print(f"I owe you {Total - 50}, and here's you coke!!")
            break
        elif (Total - 50) == 0 :
            print("Here's your coke, dont forget to share it with CS50!!")
            break
        else :
            print(f"remaning amount to get the coke = {50 - Total}")
    else :
        #reject and return the leftover he needs to input to get the coke
        print("put in the allowed denomination, please")