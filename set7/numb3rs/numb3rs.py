import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    try :
        nums = ip.split(".")
        for num in nums :
            if num.startswith("0") and int(num) != 0 :
                return False
        nums[0], nums[1], nums[2], nums[3] = int(nums[0]), int(nums[1]), int(nums[2]), int(nums[3])
    except ValueError :
        return False 
    else :
        for num in nums :
            if 0<= num <=255 :
                pass
            else :
                return False
    return True


if __name__ == "__main__":
    main()