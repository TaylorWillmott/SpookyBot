# Import External Modules
import discord, os, json

# Import Bot Command Modules
import utility

client = discord.Client()

with open('config.json') as file:
  config = json.load(file)
print('Config has been loaded.')
for item in config:
  print(f'  {item} = {config[item]}')

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}#{client.user.discriminator} ({client.user.id})')

commands = {
  'rtd': utility.rtd,
}

@client.event
async def on_message(message):
  if message.content.startswith(config['prefix']):
    splitmessage = message.content.split()
    cmd = splitmessage[0]
    for command in commands:
      if cmd == f'{config["prefix"]}{command}':
        args = splitmessage[1:]
        await commands[command](message, args)
        break
  elif message.content.startswith(f'<@!{client.user.id}>'):
    splitmessage = message.content.split()
    cmd = splitmessage[1]
    for command in commands:
      if cmd == command:
        args = splitmessage[2:]
        await commands[command](message, args)
        break

client.run(os.environ['TOKEN'])