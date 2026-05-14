import random
while True :
    try :
        n = int(input("Level : "))
        if n < 1 :
            continue
    except ValueError :
        continue
    else :
        break

gn = random.randint(1, int(n))

prompt = "Guess the number !!"

while True :
    try :
        ans = int(input(prompt))
    except ValueError :
        prompt = "not an integer!, give an integer please :)"
        continue
    if ans < gn :
        prompt = "Too small!"
        continue
    elif ans > gn :
        prompt = "Too large!"
        continue
    else :
        break

print("You got it, you are the king!!")

