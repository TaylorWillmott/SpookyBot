# What is SpookyBot?
SpookyBot is a custom Discord bot written for [Spectral Servers](https://spectralservers.com) as a hobby project.

## Can I use this code for my own bot?
Feel like getting your hands dirty, eh?
If you want to get into the world of Discord bot development I'd encourage you contribute directly to SpookyBot.
That way, everyone using this repo can benefit from your work!

However, if you're determined to have full control over your bot, you're welcome to use this code as a base with a couple of caveats:
- Please actually make substantial changes for your own bot. Don't just steal the code and publish it as-is.
- If you release your bot publicly, please link back to this repository ([spookybot.spectralservers.com/source](https://spookybot.spectralservers.com/source)).

## How can I contribute?
There are two main areas where you can contribute to SpookyBot: ideas and code.

If you have an idea for a feature or other improvement, feel free to [raise an issue](https://github.com/TheRandomnessGuy/SpookyBot/issues/new) and it might get implemented; this is a hobby project though so no promises!
Same goes for bugs; if you find one please raise an issue and I'll try to get it fixed.

Alternatively, if you feel like having a go at some coding yourself you can take a fork of the repo and try to either resolve an existing issue (check out the [Good First Issue](https://github.com/TheRandomnessGuy/SpookyBot/labels/Good%20First%20Issue) label if you're unsure) or implement an idea of your own.
When your code is ready to be merged back into the main repo, make a pull request and I'll take a look at it!

# How can I use SpookyBot?
If you'd like to use SpookyBot for yourself you have two main options:
- Invite my instance of it to your server (SpookyBot#1505).
- Use the contents of this repository to host your own instance.

## Using My Instance
Be warned that as this is currently a hobby project I can't make any guarantees regarding the uptime/stability of my SpookyBot instance.
If you desperately need 100% uptime you should probably host an instance yourself.

That being said, using my pre-made instance is by far the easiest way of using SpookyBot.
Simply use the [invite link](https://spookybot.spectralservers.com) and add the bot to whichever server you wish as you would any other bot.

## Self-Hosting
Whilst SpookyBot is fairly simple to set up on your own system, there is some prep-work required.
Your first step should be to take a copy of the repository (ideally a git clone so you can pull updates via git) and set it up in a folder on the system you'll be using to host your instance.

Once that's done, you'll need to make sure all the requirements are installed.
The simplest way to do this is to use the included `requirements.txt` file.
Simply run the following command in your new SpookyBot folder and it should grab all the required packages for you:
`pip install -r requirements.txt`

When you have all the requirements sorted, you're almost ready to start your bot instance!
All that's left to do is provide your bot token, which means you'll need to register an application over at the [Discord Developer Portal](https://discord.com/developers/applications). 
Once you've created an application, go to its **Bot** tab and click **Add Bot**.
This will create the bot account you'll be using for your SpookyBot instance. Then, on the page for your newly created bot, you'll want to click the **Copy** button under the **Token** heading to get your bot's token.

Now you have a bot token, you need to make sure the `main.py` script has access to it when it runs.
To do this, you'll need to create an environment variable called `TOKEN` with your bot token as its value.
If you then run `main.py`, the bot should go live on the new bot account.
Of course, you won't be able to interact with it unless it's on a server so next you'll need to make an invite link.

To make an invite link, head back to your application on the [Discord Developer Portal](https://discord.com/developers/applications) and go to the **OAuth2** section.
Once there, direct your attention to the OAuth2 URL Generator (specifically the **scopes** section) where you will want to tick the **bot** tickbox and then copy the URL that appears.
If you open this URL in a web browser, you will be greeted with the standard Discord bot connection screen where you are given a choice of which server you want the bot to join.

## Using Commands
Once you've got SpookyBot on your server, you'll need to know how to make it run commands.
Specific info about said commands can be found in the next section but first you have a couple of options for getting the bot's attention.

The default prefix is `s![command]`, though this can be changed if you are self-hosting the bot by changing the 'prefix' value in the config dictionary in `main.py`.
With this prefix, if you wanted to run the help command for example, you would type `s!help` into a channel where the bot has both read and write message permissions (other commands may require more permissions to work correctly).

Alternatively, the bot will always respond to you mentioning it before a command, regardless of the currently set prefix.
Again using the help command as an example, you would type `@SpookyBot help` into an appropriate text channel.
This can be useful if you are unsure of the prefix as the help message displays it near the beginning.

# Commands
The code for SpookyBot is split between `main.py` and the external module files.
The main script imports all the module scripts and then programmatically imports all the commands from them, meaning new commands can be added to existing modules with no modification to `main.py`.

To add a new command to an existing module, you would simply need to edit the module file to define the function it should run and add an entry for it in the 'commands' dictionary at the end of the file.

To add a new module, you would need to make two changes to `main.py` for it to be fully imported.
Firstly, it would need to be imported as a Python module (likely just added to the existing list of module imports).
Secondly, you would need to add a for-loop for your module to import all of its commands (see the loops for the existing modules for how to structure this).

## Core Commands
| Command | Description | Syntax |
| :-----: | :---------: | :----: |
| help | Posts a list of all the commands the bot currently supports to the chat. | `s!help` |
| ping | Posts the bot's current Discord API latency to the chat. | `s!ping` |

## Utility
| Command | Description | Syntax |
| :-----: | :---------: | :----: |
| rtd | Rolls a dice of the specified size (default 6) and posts the result to the chat. | `s!rtd [limit(optional)]` |

## Fun
| Command | Description | Syntax |
| :-----: | :---------: | :----: |
| xkcd | Posts a specified (or random) comic from XKCD to the chat. | `s!xkcd [number(optional)]` |
| dadjoke | Posts a random dad joke from [icanhazdadjoke.com](https://icanhazdadjoke.com) to the chat. | `s!dadjoke` |
| quote | Posts a randomly generated quote from [inspirobot.me](https://inspirobot.me/) to the chat. | `s!quote` |
| inspire | Posts a randomly generated inspirational image from [inspirobot.me](https://inspirobot.me/) to the chat. | `s!inspire` |
| gif | Posts a random gif or the top result for your search query from [giphy.com](https://giphy.com/) to the chat. | `s!gif [query(optional)]` |
