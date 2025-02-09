from dotenv import load_dotenv
import os
from discord import Intents
from discord.ext import commands, tasks
import requests
import random
import requests

load_dotenv()
TOKEN: str = os.getenv('DISCORD_TOKEN')
WEATHER_API_KEY: str = os.getenv('WEATHER_API')
QUOTES_API_KEY: str = os.getenv('QUOTES_API')

intents: Intents = Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

users = set() # users set

# on ready
@bot.event
async def on_ready():
  print(f'Bot is connected as {bot.user}')
  
@bot.command(name='start')
async def start(ctx):
  users.add(ctx.author.id)
  print(users)
  command_list = ", ".join([f'!{command.name}' for command in bot.commands])
  await ctx.reply(f'Welcome! My commands: {command_list}')
    
    
async def add_reaction_to_message(message, emoji="✅"):
  try:
      # Add reaction
      await message.add_reaction(emoji)
  except Exception as e:
      print(f"Error: {e}")
    
# /ping - показывает что бот работает
@bot.command(name='ping')
async def ping(ctx):
  await add_reaction_to_message(ctx.message, "✅") 
  await ctx.reply('pong')
  
# /say - повторяет сообщение
@bot.command(name='say')
async def say(ctx, *message: str):
  if not message:
    await ctx.reply('Enter commads: !say {TEXT}')
    return
  response = " ".join(message)
  await ctx.send(response)
  return
    
# /joke - рандомная шутка по API
@bot.command(name='joke')
async def joke(ctx):
  response = requests.get("https://official-joke-api.appspot.com/random_joke")
  joke = response.json()
  await ctx.reply(f"{joke['setup']} - {joke['punchline']}")
  
# /roll - бросает кубик  
@bot.command(name='roll')
async def roll(ctx):
  dice_roll = random.randint(1, 6)
  await ctx.send(f"You threw out {dice_roll}")

        
# /weather
@bot.command(name='weather')
async def weather(ctx, *, city: str = None):
  try:  
    if city is None:
      await ctx.reply('Enter command: !weather {PLACE}')
      return
    
    url = f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={city}&aqi=no"
    response = requests.get(url)
    data = response.json()
    
    if "error" in data:
      await ctx.send(f"The {city} not found. Please, enter again.")
      return
    
    # Variables with information about weather
    location = data['location']['name']
    region = data['location']['region']
    country = data['location']['country']
    temp_c = data['current']['temp_c']
    condition = data['current']['condition']['text']
    wind_speed = data['current']['wind_kph']
    humidity = data['current']['humidity']
    feels_like = data['current']['feelslike_c']
    
    # Final version of weather
    weather_info = f"Погода в {location}, {region}, {country}:\n" \
    f"Temp: {temp_c}°C\n" \
    f"Condition: {condition}\n" \
    f"Wind: {wind_speed} км/ч\n" \
    f"Humidity: {humidity}%\n" \
    f"Feels like: {feels_like}°C"
    
    await ctx.send(weather_info) # send weather info
    
  except Exception as e:
    await ctx.send(f"Error: {e}.")
  
  # await ctx.send(weather_info)

# /random
@bot.command(name='random')
async def randomize(ctx, start: str = None, end: str = None):
  if start is None or end is None:
    # if arguments didn't get
    await ctx.send("Enter command: !random {START} {END}")
    return
  try:
    # arguments to integers
    start = int(start)
    end = int(end)
    
    if start >= end:
        await ctx.send("Number 'start' should be greater than 'end'.")
        return
    
    # Генерация случайного числа
    random_num = random.randint(start, end)
    await ctx.send(f"Random integer: {random_num}")

  except ValueError:
    # В случае, если start или end не являются числами
    await ctx.send("Please, enter correct integers. Example: !random 1 100")

# /yesno - отвечает да или нет
@bot.command(name='yesno')
async def yesno(ctx, *, message: str = None):
  try:
    if message is None:
      await ctx.reply('Enter command: !yesno {QUESTION}')
      return
    await ctx.reply(random.choice(['Yes!', 'No!']))
  except Exception as e:
    return
  
# /chance - оценивает шансы
@bot.command(name='chance')
async def chance(ctx, *, message: str = None):
  try:
    if message is None:
      await ctx.reply('Enter command: !chance {EVENT}')
      return
    chance_value = random.randint(0, 100)
    await ctx.reply(f'The probability of this event is equal to {chance_value}%')
  except Exception as e:
    return
  
# /quote - random quote
@bot.command(name='quote')
async def quote(ctx):
  api_url = 'https://api.api-ninjas.com/v1/quotes'
  headers = {'X-Api-Key': QUOTES_API_KEY}

  try:
    response = requests.get(api_url, headers=headers)
    response.raise_for_status()  # request errors check

    quotes = response.json()
    if quotes:  # Проверяем, есть ли данные
      quote = random.choice(quotes).get('quote', 'No quote available.')
      await ctx.reply(quote)
    else:
      await ctx.reply("Cannot get any quote.")
  except Exception as e:
    await ctx.reply(f"Error: {e}")

bot.run(TOKEN)