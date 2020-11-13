# Import External Modules
import discord, os
from random import randint
from asyncio import sleep

# Import Bot Command Modules
import utility, fun

# Set Up Config Dictionary
config = {
  'prefix': 's!',
  'activities': {
    'playing': [
    # Playing...
      "Discord Bot Simulator",
      "Among Us 2",
      "Cyberpunk 2077"
    ],
    'listening': [
    # Listening to...
      "Human Music",
      "Creepy Songs",
      "Caramelldansen",
      "a Podcast",
      "TV Static"
    ],
    'watching': [
    # Watching...
      "the ships roll in"
    ],
    'competing': [
    # Competing in...
      "an Eating Contest"
    ]
  }
}

# Randomised Activities
activities = []
try: # Playing...
  for thing in config['activities']['playing']:
    activities.append(discord.Game(thing))
except:
  print("Something went wrong when trying to import 'activities.playing'")

try: # Listening to...
  for thing in config['activities']['listening']:
    activities.append(discord.Activity(type=discord.ActivityType.listening, name=thing))
except:
  print("Something went wrong when trying to import 'activities.listening'")

try: # Watching...
  for thing in config['activities']['watching']:
    activities.append(discord.Activity(type=discord.ActivityType.watching, name=thing))
except:
  print("Something went wrong when trying to import 'activities.watching'")

try: # Competing in...
  for thing in config['activities']['competing']:
    activities.append(discord.Activity(type=discord.ActivityType.competing, name=thing))
except:
  print("Something went wrong when trying to import 'activities.competing'")

if len(activities) == 0:
  activities.append(discord.Game(''))

client = discord.Client()

@client.event
async def on_ready():
    print(f'Prefix: {config["prefix"]}')
    print(f'Logged in as {client.user.name}#{client.user.discriminator} ({client.user.id})')
    print(f'{client.user.name} is now online in {len(client.guilds)} servers!')
    while True:
      await client.change_presence(status = discord.Status.idle, activity = activities[randint(0,len(activities)-1)])
      await sleep(randint(300, 600))

commands = {
  # Utility
  'rtd': [utility.rtd, 'Roll the dice. Will you be lucky?'],
  # Fun
  'xkcd': [fun.xkcd, 'Grab a specific xkcd comic or let the bot pick one.'],
  'dadjoke': [fun.dadjoke, 'Dad jokes are funny, right?'],
  'quote': [fun.quote, 'Have the bot come up with a quote for you.'],
  'inspire': [fun.inspire, 'Have the bot make you an inspirational image.'],
  'gif': [fun.gif, 'Get a gif related to your search'],
}

async def bothelp(message, args):
  embed = discord.Embed(title = f'{client.user.name} Commands', description = '')
  embed.set_author(name=f'My prefix is currently set to: {config["prefix"]}')
  for command in commands:
    embed.description += f'{config["prefix"]}{command} - {commands[command][1]}\n'
  await message.channel.send(embed=embed)

commands['help'] = [bothelp, "You're looking at it!"]

async def ping(message, args):
  await message.channel.send(f'Pong! (~{round(client.latency*1000)}ms)')

commands['ping'] = [ping, "Ping the bot to check its latency."]

@client.event
async def on_message(message):
  if not isinstance(message.channel, discord.channel.DMChannel):
    if message.content.startswith(config['prefix']):
      splitmessage = message.content.split()
      cmd = splitmessage[0]
      for command in commands:
        if cmd == f'{config["prefix"]}{command}':
          await message.add_reaction('👍')
          args = splitmessage[1:]
          await commands[command][0](message, args)
          break
    elif message.content.startswith(f'<@!{client.user.id}>'):
      splitmessage = message.content.split()
      cmd = splitmessage[1]
      for command in commands:
        if cmd == command:
          await message.add_reaction('👍')
          args = splitmessage[2:]
          await commands[command][0](message, args)
          break

client.run(os.environ['TOKEN'])