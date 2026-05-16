def main() :
    frac = input()
    return gauge(convert(frac))
    
def convert(fraction) :
    x, y = fraction.split("/")
    x, y = int(x), int(y)
    if x > y:
        raise ValueError("X is greater than Y")
    z = round(float(float(x)/y) * 100)
    return z 

def gauge(percentage) :
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else :
        return f"{percentage}%"



if __name__ == "__main__" :
    main()
        
