#collect all the data in a list
items = []
while True :
    try :
        x = input().upper()
        items.append(x)
    except EOFError :
        break


#start making a dictionary through those values
item_dict = {}
for item in items :
    try :
        if item_dict[item] > 0 :
            item_dict[item] += 1
        else :
            item_dict[item] = 1
    except KeyError :
        item_dict[item] = 1
#if the key repeats itself update the value for that key
#print the dictionary with the values and the quantity
for item in item_dict :
    print(item_dict[item], item)

