# Discord Bot

## 📌 Description
This bot for Discord executes various commands including weather, random numbers, quotes, jokes and more. Written in **Python** using the **discord.py** library and API to retrieve data.

## ⚡ Functionality
- **General commands**:
  - `!ping` - checks if the bot is working.
  - `!say {text}` - repeats the entered message.
  - `!roll` - rolls a die (1-6).
  - `!random {beginning} {end}` - random number in the specified range.
  - `!yesno {question}` - answers “yes” or “no”.
  - `!chance {event}` - estimates the probability in percent.
- **API-requests**:
  - `!joke` – get random joke.
  - `!quote` – get random quote.
  - `!weather {place}` – show current weather in specific place.

## 🚀 Setup and startup

### 🔹 1. Repository cloning
```bash
git clone https://github.com/alexkuznecov16/discord-bot.git
cd discord-bot
```
### 🔹 2. Creating and activating virtual environment (recommended)
#### Windows:
```bash
python -m venv venv
venv\Scripts\activate
```
#### macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 🔹 3. Dependency installation
```bash
pip install -r requirements.txt
```

### 🔹 4. Configuring environment variables
Create the `.env` file and add:
```ini
DISCORD_TOKEN=your_bot_token
WEATHER_API=your_key_weather_api
QUOTES_API=your_key_quotes_api
```

### 🔹 5. Launching the bot
```bash
python main.py
```

## 🛠 Technologies used
- **Python**
- **discord.py** – to interact with Discord API
- **requests** – for API-requests
- **dotenv** – to load environment variables

## 📜 License
This project is distributed under the MIT license. Free to use and refine!

## 📞 Contacts
If you have any questions or suggestions, please contact me:
- LinkedIn: [Alexander Kuznecov](https://www.linkedin.com/in/alexander-kuznecov/)
- Telegram: [kznws](https://t.me/kznws11)