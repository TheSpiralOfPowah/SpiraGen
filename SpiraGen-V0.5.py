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
╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░╚═════╝░╚══════╝╚═╝░░╚══╝ (DEMO)

\033[97mYet another f░░░ing nitro generator. 🗿

How many codes would you like? (High amounts of codes reccomended, Chances are low, since it is impossible to get a nitro code first-try)
               
""")

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

time.sleep(2.0)

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))
# Generates the desired strings
for _ in range(int(amount)):  
    random_string = generate_random_string(int(length))
    print("\033[34m[DEMO VER UNCHECKED]: " + "\033[37mhttps://discord.gift/"+random_string) # Delete this line.

time.sleep(5.0)