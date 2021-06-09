import discord
import asyncio

client = Discord.Client()

@client.event
async def on_ready():
    await client.change_presence(activity=discord.game(name="encouraging CP people"))

    print("Ready")

@client.event
async def on_ready():
    print ('were loged as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
    return

    if message.content.startswith('>hola'):
        await message.channel.send('**hey, whats up!**')

    client.run(ODUyMTc5OTc0MjIyOTA1NDE0.YMDEcg.DadIuY-bBYp8l5OksIlKC0Bfp50)

