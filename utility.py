from random import randint

async def rtd(message, args):
  try:
    limit = int(args[0])
  except:
    limit = 6
  result = randint(1,limit)
  await message.channel.send(content = f'You rolled a {str(result)}')