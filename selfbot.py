import discord
from discord.ext import commands
from colorama import init, Fore, Back, Style
init(convert=True)
client = commands.Bot(command_prefix=".", self_bot=True)
client.remove_command('help')

print(Fore.RED + '''
░██████╗███████╗██╗░░░░░███████╗██████╗░░█████╗░████████╗  ░░░░░░  ███╗░░░███╗░█████╗░████████╗░█████╗░░██████╗
██╔════╝██╔════╝██║░░░░░██╔════╝██╔══██╗██╔══██╗╚══██╔══╝  ░░░░░░  ████╗░████║██╔══██╗╚══██╔══╝██╔══██╗██╔════╝
╚█████╗░█████╗░░██║░░░░░█████╗░░██████╦╝██║░░██║░░░██║░░░  █████╗  ██╔████╔██║███████║░░░██║░░░██║░░██║╚█████╗░
░╚═══██╗██╔══╝░░██║░░░░░██╔══╝░░██╔══██╗██║░░██║░░░██║░░░  ╚════╝  ██║╚██╔╝██║██╔══██║░░░██║░░░██║░░██║░╚═══██╗
██████╔╝███████╗███████╗██║░░░░░██████╦╝╚█████╔╝░░░██║░░░  ░░░░░░  ██║░╚═╝░██║██║░░██║░░░██║░░░╚█████╔╝██████╔╝
╚═════╝░╚══════╝╚══════╝╚═╝░░░░░╚═════╝░░╚════╝░░░░╚═╝░░░  ░░░░░░  ╚═╝░░░░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═════╝░''')
print(Fore.GREEN +'Self-Bot feito por matos#4997\n\n\n\n\n')

print(Fore.RED +'Olá! Você está testando a beta do selfbot\nCaso encontre algum erro, entre no nosso servidor: https://discord.gg/yWBwdftxnd')
a = input('\n\nQual seu token: ')
token ="" + a


print(Fore.YELLOW+ '\n\nSELF-BOT INICIADO COM SUCESSO.')


print(Fore.GREEN +'\n\nCaso queira saber meus comandos use: .help')
@client.command(name="help")
async def help(ctx):
  await ctx.send('Para de user .help arrombado.')


client.run(token, bot=False)
