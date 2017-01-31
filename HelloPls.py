import discord
import asyncio
import random
from insults import *

client = discord.Client()
user = discord.User()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))

    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')

    elif message.content.startswith('!insult'):
        for user in message.mentions:
            await client.send_message(message.channel, "<@" +  user.id + "> thou "\
 + random.choice(insult1) + random.choice(insult2) + random.choice(insult3))

client.run(open('token.ini').read())
