months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    x = input()
    if '/' in x:
        date = x.split('/')
        if int(date[0]) > 12 or int(date[1]) > 31:
            continue
        else:
            if int(date[0]) < 10 and int(date[0][0]) != 0:
                date[0] = f'0{date[0]}'
            if int(date[1]) < 10:  # and int(date[0][0]) != 0:
                date[1] = f'0{date[1]}'
            print(f"{date[1]}-{date[0]}-{date[2]}")
            break
    else:
        date = x.split()
        date[1] = date[1][:-1]
        if int(date[1]) < 10 and int(date[1][0]) != 0:
            date[1] = f'0{date[1]}'
        date[0] = months.index(date[0]) + 1
        if date[0] < 10:
            date[0] = f'0{date[0]}'

        if int(date[0]) > 12 or int(date[1]) > 31:
            continue
        print(f"{date[0]}-{date[1]}-{date[2]}")
        break
