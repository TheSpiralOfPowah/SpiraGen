import time
import random
import string
import requests

amount = input("""\033[91m
░██████╗██████╗░██╗██████╗░░█████╗░░██████╗░███████╗███╗░░██╗
██╔════╝██╔══██╗██║██╔══██╗██╔══██╗██╔════╝░██╔════╝████╗░██║
╚█████╗░██████╔╝██║██████╔╝███████║██║░░██╗░█████╗░░██╔██╗██║
░╚═══██╗██╔═══╝░██║██╔══██╗██╔══██║██║░░╚██╗██╔══╝░░██║╚████║
██████╔╝██║░░░░░██║██║░░██║██║░░██║╚██████╔╝███████╗██║░╚███║
╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░╚═════╝░╚══════╝╚═╝░░╚══╝

\033[97mYet another f░░░ing nitro generator (And Checker). 🗿

How many codes would you like? (High amounts of codes reccomended, Chances are low, since it is impossible to get a nitro code first-try)
""")
if amount == "":
    amount = 100

length = input("""How long should the codes be? (16 default)           
""")
if length == "":
    length = 16

print("""\033[32m
░██████╗░███████╗███╗░░██╗███████╗██████╗░░█████╗░████████╗██╗███╗░░██╗░██████╗░░░░░░░░░░
██╔════╝░██╔════╝████╗░██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██║████╗░██║██╔════╝░░░░░░░░░░
██║░░██╗░█████╗░░██╔██╗██║█████╗░░██████╔╝███████║░░░██║░░░██║██╔██╗██║██║░░██╗░░░░░░░░░░
██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░██╔══██╗██╔══██║░░░██║░░░██║██║╚████║██║░░╚██╗░░░░░░░░░
╚██████╔╝███████╗██║░╚███║███████╗██║░░██║██║░░██║░░░██║░░░██║██║░╚███║╚██████╔╝██╗██╗██╗
░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝╚═╝╚═╝
      
\033[37mSit tight...""", amount, "Nitro codes are generating...")

validResults = []

# Cook up the codes.

time.sleep(1.0)

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))
# Generates the desired strings
for _ in range(int(amount)):  
    random_string = generate_random_string(int(length))
    doggo = requests.get("https://discord.com/api/v8/entitlements/gift-codes/"+random_string)
    # Time to check the codes!
    if doggo.status_code == 429:
        ratelimittime = float(doggo.headers['Retry-After'])
        print("\033[33mRate limiting! Wait " + str(ratelimittime) + " seconds!")
        time.sleep(ratelimittime)
    else:
        if doggo.status_code == 200:
            print("\033[32m[Valid]: " + "\033[37mhttps://discord.gift/"+random_string)
            validResults.append("https://discord.gift/"+random_string)
        else:
            print("\033[31m[Invalid]: " + "\033[37mhttps://discord.gift/"+random_string)


# Results come out here

print("""\033[32m
████████╗░█████╗░████████╗░█████╗░██╗░░░░░  ██╗░░░██╗░█████╗░██╗░░░░░██╗██████╗░
╚══██╔══╝██╔══██╗╚══██╔══╝██╔══██╗██║░░░░░  ██║░░░██║██╔══██╗██║░░░░░██║██╔══██╗
░░░██║░░░██║░░██║░░░██║░░░███████║██║░░░░░  ╚██╗░██╔╝███████║██║░░░░░██║██║░░██║
░░░██║░░░██║░░██║░░░██║░░░██╔══██║██║░░░░░  ░╚████╔╝░██╔══██║██║░░░░░██║██║░░██║
░░░██║░░░╚█████╔╝░░░██║░░░██║░░██║███████╗  ░░╚██╔╝░░██║░░██║███████╗██║██████╔╝
░░░╚═╝░░░░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝╚══════╝  ░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚═╝╚═════╝░

░█████╗░░█████╗░██████╗░███████╗░██████╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝
██║░░╚═╝██║░░██║██║░░██║█████╗░░╚█████╗░
██║░░██╗██║░░██║██║░░██║██╔══╝░░░╚═══██╗
╚█████╔╝╚█████╔╝██████╔╝███████╗██████╔╝
░╚════╝░░╚════╝░╚═════╝░╚══════╝╚═════╝░
\033[37m""" + str(validResults))

time.sleep(5.0)
