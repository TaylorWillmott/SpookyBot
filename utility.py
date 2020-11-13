from asyncio import sleep
from random import randint

async def rtd(message, args):
  numbers = ['one','two','three','four','five','six','seven','eight','nine','ten']
  try:
    limit = int(args[0])
  except:
    limit = 6
  sentmessage = await message.channel.send(f'Rolling a d{limit}...')
  await sleep(3)
  result = randint(1,limit)
  if result < len(numbers):
    await sentmessage.edit(content = sentmessage.content + f'\nYou rolled a :{numbers[result-1]}:')
  else:
    await sentmessage.edit(content = sentmessage.content + f'\nYou rolled a {str(result)}')

commands = {
  'rtd': [rtd, 'Roll the dice. Will you be lucky?'],
}
