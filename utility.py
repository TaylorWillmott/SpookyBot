from random import randint

async def rtd(message, args):
  numbers = ['one','two','three','four','five','six','seven','eight','nine','ten']
  try:
    limit = int(args[0])
  except:
    limit = 6
  result = randint(1,limit)
  await message.channel.send(content = f'You rolled a {str(result)}')
  if result < len(numbers):
    await message.channel.send(content = f'You rolled a :{numbers[result-1]}:')
  else:
    await message.channel.send(content = f'You rolled a {str(result)}')