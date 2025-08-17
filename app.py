import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.typing = True
intents.presences = True

def is_authorized(ctx):
    # Your authorization check logic here
    return True
intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix='e!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command(aliases=['mode'])
@commands.check(is_authorized)
async def status(ctx, activity_type, *, text):
    activity = None
    if activity_type == 'playing':
        activity = discord.Game(name=text)
    elif activity_type == 'streaming':
        activity = discord.Streaming(name=text, url='https://www.twitch.tv/dammnranaah')
    elif activity_type == 'listening':
        activity = discord.Activity(type=discord.ActivityType.listening, name=text)
    elif activity_type == 'watching':
        activity = discord.Activity(type=discord.ActivityType.watching, name=text)

    if activity:
        await bot.change_presence(activity=activity)
        await ctx.send(f'Status updated: {activity_type} {text}')
    else:
        await ctx.send('Invalid activity type. Available types: playing, streaming, listening, watching')

bot.run('YOUR_TOKEN_BABY')