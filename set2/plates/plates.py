def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    win = 0
    # max characters  = 6, min chars = 2
    if 6 >= len(s) >= 2:
        win += 1
    else:
        print("length")
        return False

    # starting with atleast two letters
    alphabet = 'abcdefghijklmnopqrstuvwxyz'.upper()
    if s[0] in alphabet and s[1] in alphabet:
        win += 1
    else:
        print("starting letters")
        return False

    # no periods, spaces or punctuation
    for i in s:
        if i in "!\"#$%&'()*+,-./:;<=>?@[\]^_{|}~…–—` ":
            print('punctuation')
            return False
        else:
            win += 1

    # numbers should only come at the end
    # if you encounter a number while traversing the string and the you encounter a letter then return Fasle, else True
    # also it cant start with a 0
    nums = '1234567890'
    for i in range(len(s)):
        if s[i] in nums:
            if s[i-1] not in nums and s[i] == '0':
                print("starting with 0")
                return False
            for j in s[i:]:
                if j in alphabet:
                    print("encountered a letter in the following seq")
                    return False
            else:
                return True


if __name__ == "__main__":
    main()
