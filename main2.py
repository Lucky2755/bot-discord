import discord, random, time
from discord.ext import commands
from bot_logic import gen_pass

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    channel = bot.get_channel(1286715618183348380)
    if channel:
        await channel.send("buonsalve, sono boh 2.0") 
    print(f'Hai fatto l\'accesso come {bot.user}')


    


@bot.command()
async def ciao(ctx):
    await ctx.send(f'Ciao! Sono un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 20):
    await ctx.send("he" * count_heh)

@bot.command()
async def stop(ctx):
    await ctx.send("alla prossima!")
    exit()

@bot.command()
async def moneta(ctx):
    await ctx.send("lancio della moneta in corso....")
    time.sleep(1)
    x = random.randint(1,2)
    if x == 1:
        await ctx.send("TESTA!")
    elif x == 2:
        await ctx.send("CROCE!")

@bot.command()
async def comandi(ctx):
    await ctx.send("posso eseguire i seguenti comandi:")
    time.sleep(1)
    await ctx.send("/ciao")
    time.sleep(1)
    await ctx.send("/heh")
    time.sleep(1)
    await ctx.send("/stop")
    time.sleep(1)
    await ctx.send("/moneta")
    time.sleep(1)
    await ctx.send("/gen")

@bot.command()
async def gen(ctx):
    lunghezza_password = random.randint(10, 20)
    x = gen_pass(lunghezza_password) 
    await ctx.send(f"La tua nuova password è: {x}")


        


bot.run("")