import random


def main():
    l = get_level()
    x, y, ans = [], [], []
    for i in range(10) :
        x.append(generate_integer(l))
        y.append(generate_integer(l))
        ans.append(x[i] + y[i])

    score = 0
    for i in range(10) :
        for k in range(3):
            try :
                X = int(input(f"{x[i]} + {y[i]} = "))
                if X == ans[i] :
                    score += 1
                    break 
                else :
                    print("EEE")
                    continue
            except ValueError:
                print("EEE")
        else :
            print(f"{x[i]} + {y[i]} = {ans[i]}")
                
    print(f"Score : {score}/10")

            





def get_level():

    while True :
        try:
            x = int(input("Level: "))
            if x not in [1, 2, 3]:
                continue
            return x
        except ValueError:
            print("put 1, 2 or 3 mann!")
            continue


def generate_integer(level):
    if level == 1 :
        a, b = 9, 0
    else :
        a = pow(10,level) - 1
        b = pow(10, level - 1)
    return random.randint(b, a)


main()