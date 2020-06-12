import string
import random
import requests

codes = []

proxie_list = []

with open("https.txt", "r") as f:
    for proxy in f.readlines():
        proxie_list.append(proxy.replace("\n", ""))

def generateCodes(amount):
    validCodes = []
    chars = string.ascii_letters + string.digits
    for x in range(amount):
        code = ''.join(random.choice(chars) for i in range(16))
        #print("Code: #" + str(x + 1) + " : " + code)
        codes.append(code)
        try:
            proxies = {
                'https': random.choice(proxie_list)
            }
            r = requests.get("https://discordapp.com/api/v6/entitlements/gift-codes/{}?with_application=false&with_subscription_plan=true".format(code), proxies=proxies)
            if("Unknown Gift Code" in r.text):
                print("[INVALID]:   Code: #" + str(x + 1) + " : " + code)
            elif("You are being rate limited." in r.text):
                print("[ERROR]:   You are getting limited, change ip or use other proxys")
            else:
                print("[VALID]:   Code: #" + str(x + 1) + " : " + code)
                print(r.text)
                validCodes.append(code)
        except Exception as e:
            print("[ERROR]:   timeout")
            continue
    if(validCodes.count > 0):
        with open("valid.txt", "w") as validFile:
            for validCode in validCodes:
                validFile.writelines("https://discord.com/gifts/" + validCode)

print("[IMPORTANT]:   Please only use https proxies!")

amount = input("Amount of Codes ?:")

generateCodes(int(amount))