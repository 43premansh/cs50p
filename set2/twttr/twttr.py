x = input("Input: ")
for i in x :
    if i.lower() not in ['a', 'e', 'i', 'o', 'u'] :
        print(i, end = "")
    else :
        continue

print()