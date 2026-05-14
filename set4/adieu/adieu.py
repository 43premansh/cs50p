names = []
try:
    while True:
        names.append(input("Name: "))
except EOFError:
    print()
    pass

s = 'Adieu, adieu, to '
if len(names) == 0:
    print("no greetings today ig!!")
elif len(names) == 1:
    print(f"{s} {names[0]}")
elif len(names) == 2:
    print(f"{s}{names[0]} and {names[1]}")
else:
    for i in names[:-1]:
        s = s + f'{i.title()}, '
    print(s+f'and {names[-1]}')
