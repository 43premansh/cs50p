def shorten(word):
    s = ''
    for i in word:
        if i.lower() not in ['a', 'e', 'i', 'o', 'u']:
            s += i
        else:
            continue
    return s
