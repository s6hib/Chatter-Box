# Chatter Box

Chatter Box is a feature-rich Discord bot that can perform a variety of tasks, providing fun and entertainment for your server. Whether you need a random joke, an inspirational quote, or some trivia questions, Chatter Box has got you covered.

## Features

Here are some of the commands you can use with Chatter Box:

- `!trivia`: Chatter Box will fetch a trivia question from the Open Trivia Database. Respond with your answer, and the bot will let you know if you're correct.

- `!joke`: Need a laugh? Chatter Box will send a random joke from its repertoire.

- `!quote`: Looking for some inspiration? The bot will send a random quote.

- `!stoic`: Chatter Box can share wisdom from stoic philosophers.

- `!compliment`: Everyone could use a pick-me-up now and then. Chatter Box will send a random compliment.

- `!fact`: Learn something new with a random fact from Chatter Box.

- `!guess`: Test your luck by trying to guess a number between 1 and 10 that Chatter Box is thinking of.

## Setup

To get Chatter Box running on your server, follow these steps:

1. Clone this repository.
2. Install the necessary Python packages with `pip install -r requirements.txt`.
3. Replace `'your-token-here'` with your actual Discord bot token in `main.py`.
4. Run `main.py` with Python 3.7 or later.

## Data

Chatter Box pulls jokes, quotes, compliments, stoic quotes, and facts from a JSON file named `data.json`. You can add or modify entries in this file to customize the bot's responses.
