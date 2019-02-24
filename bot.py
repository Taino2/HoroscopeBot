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

    if message.content.startswith('!ping'):
        await client.send_message(message.channel, "Pong")

    
    if message.content.startswith('!horoscope'):
        await client.send_message(message.channel, "getting Horoscope")
        msg1 = message.content[11:100]
        print(msg1)
        horoscope = Horoscope(msg1.lower())
        today = horoscope.today()
        await client.send_message(message.channel, 'Hello {0.author.mention} Taino says that your Horoscope will be:'.format(message))
        msg2 = today['horoscope']
        await client.send_message(message.channel, msg2[:msg2.rfind('(')])

    if message.content.startswith('!exit'):
        exit()
        

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
