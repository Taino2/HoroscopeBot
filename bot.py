# Work with Python 3.6
import discord
from theastrologer import Horoscope

TOKEN = 'NTQ4NzA1NjQ2Nzk1NTU0ODQ3.D1JNeA.97t7043kiVkdW9kNlHuDX1hOcUw'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!horoscope'):
        await client.send_message(message.channel, "getting Horoscope")
        msg1 = message.content[11:100]
        print(msg1)
        horoscope = Horoscope(msg1)
        today = horoscope.today()
        await client.send_message(message.channel, today['sunsign'])
        await client.send_message(message.channel, today['horoscope'])
        
        

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
