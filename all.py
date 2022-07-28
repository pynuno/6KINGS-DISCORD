from colorama import init, Fore, Back, Style
import webbrowser
init(convert=True)
import requests
import time
threads = 3
cancel_key = "ctrl+x"
from webbot import Browser 
import json,requests
from os import system
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

print(Fore.RED +'''

░█████╗░██╗░░██╗██╗███╗░░██╗░██████╗░░██████╗
██╔═══╝░██║░██╔╝██║████╗░██║██╔════╝░██╔════╝
██████╗░█████═╝░██║██╔██╗██║██║░░██╗░╚█████╗░
██╔══██╗██╔═██╗░██║██║╚████║██║░░╚██╗░╚═══██╗
╚█████╔╝██║░╚██╗██║██║░╚███║╚██████╔╝██████╔╝
░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░╚═════╝░╚═════╝░''')
print(Fore.RED +"""This was made by matos#4997""")
print(Fore.RED +"""github - github.com/pynuno""")

print(Fore.RED +'''
[1] Discord Server

[2] Discord Token Login Auto

[3] SelfBot 

[4] Discord Token Checker

''')

option = int(input("--> "))


if option == 1:
    webbrowser.open('https://discord.gg/Tgu2G8jQjZ')
    print('Caso o invite esteja inválido, me chame no discord!')
    time.sleep(1)
    system('cls')
    print(Fore.YELLOW + 'CTRL + C e use "py a.py" novamente.')
    print('Obrigado por entrar em nosso servidor!')
    time.sleep(5)
    system('cls')

if option == 2:
  print('Essa opção foi atualizada para outro arquivo, tente ir em Python/tokenlogin.py')
  print(Fore.YELLOW +'saindo [1]')
  time.sleep(1)
  print(Fore.YELLOW +'saindo [2]')
  time.sleep(1)
  print(Fore.YELLOW +'saindo [3]')
  time.sleep(1)
  print(Fore.YELLOW +'saindo [4]')
  time.sleep(1)
  print(Fore.YELLOW +'saindo [5]')
  system('cls')


if option == 3:
  print('Essa opção foi atualizada para outro arquivo, tente ir em Python/selfbot.py')
  print(Fore.YELLOW +'saindo [1]')
  time.sleep(1)
  print(Fore.YELLOW +'saindo [2]')
  time.sleep(1)
  print(Fore.YELLOW +'saindo [3]')
  time.sleep(1)
  print(Fore.YELLOW +'saindo [4]')
  time.sleep(1)
  print(Fore.YELLOW +'saindo [5]')
  system('cls')



if option == 4:
  pergunta = input('Você tem o token colocado na pasta setting.txt? Use Y/N: ' )
if pergunta == ('Y'):
  with open("setting.txt", "r") as f:
    line = f.read()
    if len(line) == 70:
      print(Fore.GREEN +'\nToken está correto! Você pode logar na conta dele!')
      print(Fore.LIGHTYELLOW_EX +'\nLembrando! Eu só conto os tokens pelos caracteres, então alguns podem estar errados.')
      print(Fore.YELLOW +'\n\nCTRL + C e use "py a.py" novamente.')
    else:
      print(Fore.RED +'\n\nToken errado! Você não pode logar na conta.')
      print(Fore.LIGHTYELLOW_EX +'Lembrando! Eu só conto os tokens pelos caracteres, então alguns podem estar errados.') 
      print('CTRL + C e use "py a.py" novamente.')
      time.sleep(1)
      system('cls')
      print('CTRL + C e use "py a.py" novamente.')
      print('Programa está reiniciando! Espere 3 segundos.')
      time.sleep(3)
elif pergunta == ('N'):
  print(Fore.RED +'Antenção! Antes de usar o programa ou usar esta opção, coloque um token em "setting.txt".')
  print('Programa está reiniciando! Espere 3 segundos.')
  time.sleep(3)
  system('cls')
else:
  print(Fore.GREEN +'Hm.. Você deve usar S/N de Sim/Não!')      
  print('Programa está reiniciando! Espere 3 segundos.')
  time.sleep(3)
  system('cls')
  print(pergunta)










