import sys
import requests
import json

if len(sys.argv) != 2:
    sys.exit()
try:
    # no. of bitcoins
    n = float(sys.argv[1])
except ValueError:
    sys.exit()


try:
    response = requests.get(
        "https://rest.coincap.io/v3/assets/bitcoin?apiKey=c039f166c307d8e8b07d55fbc5ca9547b4f5830685593f423b4f41fcb5a3cf57")
    data = response.json()
    price = float(data["data"]["priceUsd"])
    print(f"price of {n} is {n*price}")
except requests.RequestException:
    sys.exit("Request failed")
