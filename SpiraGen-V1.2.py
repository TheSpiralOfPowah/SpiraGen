import time
import random
import string
import requests
import keyboard

# You can edit the things in this block until it reaches the "Stop Here" comment. If you edit beyond the stop comment, you will likely f░░k something up.

# If you have webhooks enabled (True/False), you need to put in the webhook link.
webhooks = False
webhook_url = "https://discord.com/api/webhooks/.../..."

# This shows advanced info for checking the codes if True.
Debug_info = False

# Stop here. This is where you can't edit. Beyond this point, you aren't allowed to edit anything else. This is the no-go zone.

def webhookmessage(message):
    if webhooks:
        payload = {
        "content": message,
        "username": "SpiraGen",
        "avatar_url": "https://cdn.discordapp.com/attachments/1123391869280342077/1164394236691615794/spiral.gif?ex=65430da3&is=653098a3&hm=cf9e178751efa03d3c0773cfe5bf5a00bd24530509e636c20fbb1ccd9af294b2&",
        }

        response = requests.post(webhook_url, json=payload)

        if response.status_code == 204:
            print("Message sent successfully!")
        else:
            print("Failed to send message.")

webhookmessage("SpiraGen booted up!")
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

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))
# Generates the desired strings
for _ in range(int(amount)):  
    random_string = generate_random_string(int(length))
    doggo = requests.get("https://discord.com/api/v8/entitlements/gift-codes/"+random_string)
    if Debug_info:
        print("\033[37mDebug info: " + str(doggo) + str(doggo.headers))
    # Time to check the codes!
    if doggo.status_code == 429:
        ratelimittime = float(doggo.headers['Retry-After'])
        print("\033[33mRate limiting! Wait " + str(ratelimittime) + " seconds!")
        time.sleep(ratelimittime)
    else:
        if doggo.status_code == 200:
            print("\033[32m[Valid]: " + "\033[37mhttps://discord.gift/"+random_string)
            validResults.append("https://discord.gift/"+random_string)
            webhookmessage("https://discord.gift/"+random_string)
        else:
            print("\033[31m[Invalid]: " + "\033[37mhttps://discord.gift/"+random_string)
            if keyboard.is_pressed('q'):
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
░╚════╝░░╚════╝░╚═════╝░╚══════╝╚═════╝░ (Mid Generation)
\033[37m""" + str(validResults))
                
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
░╚════╝░░╚════╝░╚═════╝░╚══════╝╚═════╝░ (After End)
\033[37m""" + str(validResults))

time.sleep(5.0)
