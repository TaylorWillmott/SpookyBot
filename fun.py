import requests, discord, inspirobot, urllib.parse
from random import randint

async def xkcd(message, args):
  invalid_num = False # Tracks if we tried and failed to fetch a specific comic.

  # Attempt to fetch specific comic if one was requested.
  if len(args) > 0:
    try:
      num = args[0]
      comic = requests.get(f'https://xkcd.com/{str(int(num))}/info.0.json').json()
    except:
      invalid_num = True
      comic = None

  # If we haven't already grabbed a specific comic, get a random one instead.
  try:
    len(comic)
  except:
    latest = requests.get('https://xkcd.com/info.0.json').json()
    num = randint(1, latest['num'])
    comic = requests.get('https://xkcd.com/' + str(num) + '/info.0.json').json()

  # Now we have a comic, create and send the embed.
  embed = discord.Embed()
  embed.set_image(url=comic['img'])
  embed.set_footer(text=comic['alt'])
  embed.set_author(name=f'xkcd #{num} - {comic["title"]}', url=f'https://xkcd.com/{num}')
  await message.channel.send(
    invalid_num and "That doesn't look like a valid comic ID. I'll fetch a random one instead..." or "",
    embed=embed)

async def dadjoke(message, args):
  joke = requests.get('https://icanhazdadjoke.com', headers={"Accept": "text/plain"}).text
  await message.channel.send(joke)

async def quote(message, args):
  sentmessage = await message.channel.send('Thinking...')
  await sentmessage.edit(content=inspirobot.flow()[0])

async def inspire(message, args):
  sentmessage = await message.channel.send('Thinking...')
  await sentmessage.edit(content=inspirobot.generate().url)

async def gif(message, args):
  if len(args) > 0:
    query = ' '.join(args)
    sentmessage = await message.channel.send(f"Searching for '{query}' gifs...")
    response = requests.get(f'https://api.giphy.com/v1/gifs/search?q={urllib.parse.quote(query)}&api_key=hCKgiae5XgjiYbKPTdgrSuh8P7l2xWMT').json()
    if len(response['data']) > 0:
      await sentmessage.edit(content=response['data'][0]['url'])
    else:
      await sentmessage.edit(content=f"Sorry, I couldn't find any gifs related to '{query}'!")
  else:
    sentmessage = await message.channel.send("Fetching a random gif...")
    response = requests.get('https://api.giphy.com/v1/gifs/random?api_key=hCKgiae5XgjiYbKPTdgrSuh8P7l2xWMT').json()
    await sentmessage.edit(content=response['data']['url'])
