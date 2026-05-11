x = input(
    "What is the Answer to the Great question of life, the Universe, and Everything? ")

match x.lower().strip():
    case "42" | "fortytwo" | "forty two" | "forty-two":
        print("Yes")
    case _:
        print("No")
