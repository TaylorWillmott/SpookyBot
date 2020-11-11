from random import randint

async def rtd(message, args):
  result = randint(1,6)
  await message.channel.send(content = f'You rolled a {str(result)}')