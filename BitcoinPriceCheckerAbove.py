import os
import requests
import json
import time
os.system('cls' if os.name == 'nt' else 'clear')
TARGET_PRICE = 18000
WEBHOOK_URL = "url"

while True:

  response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
  data = response.json()
  price = data['bpi']['USD']['rate_float']

  local_time = time.asctime(time.localtime(time.time()))
  print(f"\033[91m" + f"Current Bitcoin price: ${price}" + "\033[0m")
  print(f"\033[91m" + f"Local time: {local_time}" + "\033[0m")

  if price > TARGET_PRICE:
    print('\033[92m' + "The price is above the target price!" + '\033[0m')

    payload = {
        "content": f"@everyone The current bitcoin price (${price}) is above the target price of ${TARGET_PRICE} at {local_time}!"
    }
    requests.post(WEBHOOK_URL, json=payload)

  time.sleep(60)
