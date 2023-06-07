import discord
import requests
import html
import json
import random
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

# Load data from json file
with open('data.json', 'r') as f:
  data = json.load(f)

jokes = data['jokes']
quotes = data['quotes']
compliments = data['compliments']
stoic_quotes = data['stoic_quotes']
facts = data['facts']


@bot.event
async def on_ready():
  print(f'We have logged in as {bot.user}')


@bot.command()
async def trivia(ctx):
  response = requests.get('https://opentdb.com/api.php?amount=1&type=multiple')
  data = response.json()
  question = html.unescape(data['results'][0]['question'])
  correct_answer = html.unescape(data['results'][0]['correct_answer'])
  await ctx.send(f"Here's a question for you:\n{question}")

  def check(m):
    return m.content.lower() == correct_answer.lower(
    ) and m.channel == ctx.channel

  msg = await bot.wait_for('message', check=check)
  await ctx.send(
    f"Congratulations {msg.author.mention}, you got the correct answer: {correct_answer}!"
  )


@bot.command()
async def joke(ctx):
  await ctx.send(random.choice(jokes))


@bot.command()
async def quote(ctx):
  await ctx.send(random.choice(quotes))


@bot.command()
async def stoic(ctx):
  await ctx.send(random.choice(stoic_quotes))


@bot.command()
async def compliment(ctx):
  await ctx.send(random.choice(compliments))


@bot.command()
async def fact(ctx):
  await ctx.send(random.choice(facts))


@bot.command()
async def guess(ctx, user_guess: int):
  # Generate a random number between 1 and 10
  number = random.randint(1, 10)

  if user_guess == number:
    await ctx.send("Congratulations, you guessed the number!")
  else:
    await ctx.send(f"Sorry, the number was {number}. Better luck next time!")


@guess.error
async def guess_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send('You need to guess a number! Try `!guess <number>`.')


bot.run(
  'your-token-here')
