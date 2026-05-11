f = input()
if f.endswith('.gif'):
    print("image/gif")
elif f.endswith('.jpg'):
    print("image/jpeg")
elif f.endswith('.jpeg'):
    print("image/jpeg")
elif f.endswith('.pdf'):
    print("application/pdf")
elif f.endswith('.txt'):
    print("text/plain")
elif f.endswith('.zip'):
    print("application/zip")
elif f.endswith('.png'):
    print("image/png")
else:
    print("application/octet-stream")
