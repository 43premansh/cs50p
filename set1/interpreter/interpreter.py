exp = input("Expression :")
x, op, y = exp.split()
x, y = int(x), int(y)
match op:
    case "+":
        print(f"{x+y:.1f}")
    case "-":
        print(f"{x-y:.1f}")
    case "*":
        print(f"{x*y:.1f}")
    case "/":
        print(f"{x/y:.1f}")
    case _:
        print("idk how to do that!, sry")
