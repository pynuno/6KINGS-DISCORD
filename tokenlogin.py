
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webbot import Browser 
import json,requests
from colorama import init, Fore, Back, Style
init(convert=True)
import time
from os import system

print(Fore.GREEN +'''
████████╗░█████╗░██╗░░██╗███████╗███╗░░██╗  ██╗░░░░░░█████╗░░██████╗░██╗███╗░░██╗
╚══██╔══╝██╔══██╗██║░██╔╝██╔════╝████╗░██║  ██║░░░░░██╔══██╗██╔════╝░██║████╗░██║
░░░██║░░░██║░░██║█████═╝░█████╗░░██╔██╗██║  ██║░░░░░██║░░██║██║░░██╗░██║██╔██╗██║
░░░██║░░░██║░░██║██╔═██╗░██╔══╝░░██║╚████║  ██║░░░░░██║░░██║██║░░╚██╗██║██║╚████║
░░░██║░░░╚█████╔╝██║░╚██╗███████╗██║░╚███║  ███████╗╚█████╔╝╚██████╔╝██║██║░╚███║
░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝  ╚══════╝░╚════╝░░╚═════╝░╚═╝╚═╝░░╚══╝''')

print('''
[1] Token Login
''')








option = int(input("--> "))

if option == 1:
    Tokenzin = str(input("Insira seu token : "))
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get('https://discord.com/login')
driver.execute_script('window.t = "' + Tokenzin + '";window.localStorage = document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage;window.setInterval(() => window.localStorage.token = `"${window.t}"`); window.location.reload();')
system('cls')
while True:
    print('Conectado na conta!')
    print('------------------------------------------------------')
    print(Fore.YELLOW +'Ctrl + C e use "py a.py" para usar o arquivo novamente!')
    time.sleep(3)
    system('cls')

