import discord
import asyncio
import random

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

        ins1 = ["artless ",
        "bawdy ",
        "beslubbering ",
        "bootless ",
        "churlish ",
        "cockered ",
        "clouted ",
        "craven ",
        "currish ",
        "dankish ",
        "dissembling ",
        "droning ",
        "errant ",
        "fawning ",
        "fobbing ",
        "froward ",
        "frothy ",
        "gleeking ",
        "goatish ",
        "gorbellied ",
        "impertinent ",
        "infectious ",
        "jarring ",
        "loggerheaded ",
        "lumpish ",
        "mammering ",
        "mangled ",
        "mewling ",
        "paunchy ",
        "pribbling ",
        "puking ",
        "puny ",
        "pualling ",
        "rank ", 
        "reeky ",
        "roguish ",
        "ruttish ",
        "saucy ",
        "spleeny ",
        "spongy ",
        "surly ",
        "tottering ",
        "unmuzzled ",
        "vain ",
        "venomed ",
        "villanious ",
        "warped ",
        "wayward ",
        "weedy ",
        "yeasty "]

        ins2 = ["base-court ",
        "bat-fowling ",
        "beef-witted ",
        "beetle-headed ",
        "boil-brained ",
        "clapper-clawed ",
        "clay-brained ",
        "common-kissing ",
        "crook-pated ",
        "dismal-dreaming ",
        "dizzy-eyed ",
        "doghearted ",
        "dread-bolted ",
        "earth-vexing ",
        "elf-skinned ",
        "fat-kidneyed ",
        "fen-sucked ",
        "flap-mouthed ",
        "fly-bitten ",
        "folly-fallen ",
        "fool-born ",
        "full-gorged ",
        "guts-griping ",
        "half-faced ",
        "hasty-witted ",
        "hedge-born ",
        "hell-hated ",
        "idle-headed ",
        "ill-breeding ",
        "ill-nurtured ",
        "knotty-pated ",
        "milk-livered ",
        "motley-minded ",
        "onion-eyed ",
        "plume-pluked ",
        "pottle-deep ",
        "pox-marked ",
        "reeling-ripe ",
        "rough-hewn ",
        "rude-growing ",
        "rump-fed ",
        "shard-borne ",
        "sheep-biting ",
        "spur-galled ",
        "swag-bellied ",
        "tardy-gaited ",
        "tickle-brained ",
        "toad-spotted ",
        "unchin-snouted ",
        "weather-bitten "]

        ins3 = ["apple-john.",
        "baggage.",
        "barnacle.",
        "bladder.",
        "boar-pig.",
        "bugbear.",
        "bum-bailey.",
        "canker-blossom.",
        "clack-dish.",
        "clotpole.",
        "coxcomb.",
        "codpiece.",
        "death-token.",
        "dewberry.",
        "flap-dragon.",
        "flax-wench.",
        "flirt-gill.",
        "foot-licker.",
        "fustilarian.",
        "giglet.",
        "gudgeon.",
        "haggard.",
        "harpy.",
        "hedge-pig.",
        "horn-beast.",
        "hugger-mugger.",
        "joithead.",
        "lewdster.",
        "lout.",
        "maggot-pie.",
        "malt-worm.",
        "mammet.",
        "measle.",
        "minnow.",
        "miscreant.",
        "moldwarp.",
        "mumble-news.",
        "nut-hook.",
        "pigeon-egg.",
        "pignut.",
        "puttock.",
        "pumpion.",
        "ratsbane.",
        "scut.",
        "skainsmate.",
        "strumpet.",
        "varlot.",
        "vassal.",
        "whey-face.",
        "wagtail."]

        for user in message.mentions:
            await client.send_message(message.channel, "<@" +  user.id + "> thou " + random.choice(ins1) + random.choice(ins2)\
 + random.choice(ins3))

client.run(open('token.ini').read())
