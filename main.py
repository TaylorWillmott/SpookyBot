# Import External Modules
import discord, os, json
from random import randint

# Import Bot Command Modules
import utility

with open('config.json') as file:
  config = json.load(file)
print('Config has been loaded.')
for item in config:
  print(f'  {item} = {config[item]}')

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

client = discord.Client( status = discord.Status.idle, activity = activities[randint(0,len(activities)-1)])

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}#{client.user.discriminator} ({client.user.id})')

commands = {
  'rtd': [utility.rtd, 'Roll the dice. Will you be lucky?'],
}

async def bothelp(message, args):
  embed = discord.Embed(title = f'{client.user.name} Commands', description = '')
  embed.set_author(name=f'My prefix is currently set to: {config["prefix"]}')
  for command in commands:
    embed.description += f'{config["prefix"]}{command} - {commands[command][1]}\n'
  await message.channel.send(embed=embed)

commands['help'] = [bothelp, "You're looking at it!"]

@client.event
async def on_message(message):
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