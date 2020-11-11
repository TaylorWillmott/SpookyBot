import discord, os, json

client = discord.Client()

with open('config.json') as file:
  config = json.load(file)
print('Config has been loaded.')
for item in config:
  print(f'  {item} = {config[item]}')

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}#{client.user.discriminator} ({client.user.id})')

@client.event
async def on_message(message):
  if message.content.startswith(config['prefix']):
    print(f'Potential Command Detected: {message.content}')
  elif message.content.startswith(f'<@!{client.user.id}>'):
    print(f'Potential Command Detected: {message.content}')

client.run(os.environ['TOKEN'])