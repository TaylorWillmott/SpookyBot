import requests, discord
from random import randint

async def xkcd(message, args):
  latest = requests.get('https://xkcd.com/info.0.json').json()
  num = randint(1, latest['num'])
  comic = requests.get('https://xkcd.com/' + str(num) + '/info.0.json').json()

  embed = discord.Embed()
  embed.set_image(url=comic['img'])
  embed.set_footer(text=comic['alt'])
  embed.set_author(name=f'xkcd #{num} - {comic["title"]}', url=f'https://xkcd.com/{num}')
  await message.channel.send(embed=embed)