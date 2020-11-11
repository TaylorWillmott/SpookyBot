import discord, os

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}#{client.user.discriminator} ({client.user.id})')

@client.event
async def on_message(message):
  if message.content.startswith('s!'):
    print(f'Potential Command Detected: {message.content}')
  elif message.content.startswith(f'<@!{client.user.id}>'):
    print(f'Potential Command Detected: {message.content}')

client.run(os.environ['TOKEN'])