greet = input()
out = 0
if greet.lower().startswith('hello'):
    out = 0
elif greet.lower().startswith('h') :
    out = 20
else :
    out = 100

print(out)