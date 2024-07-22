from flask import Flask, jsonify, send_from_directory
import os
import json
from threading import Thread
from twitchio.ext import commands
import deepl

# Flask app setup
app = Flask(__name__)


# Load secrets from the JSON file
with open('secrets.json', 'r') as f:
    secrets = json.load(f)

# Get the Twitch secret
twitch_secret = secrets.get('twitch_secret')
deepl_auth_key = secrets.get('deepl_auth_key')
translator = deepl.Translator(deepl_auth_key)

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(token=twitch_secret, prefix="!", initial_channels=["LulneWolfy", "t___homas", "ExtraEmily"])
        self.last_messages = []

    async def event_ready(self):
        print(f"Logged in as | {self.nick}")

    async def event_message(self, message):
        print(f"Message from {message.author.name}: {message.content}")
        # Store the message
        self.last_messages.append(f"{message.author.name}: {translator.translate_text(message.content, target_lang='ZH')}")
        if len(self.last_messages) > 5:
            self.last_messages.pop(0)

        await self.handle_commands(message)

    @commands.command(name="hello")
    async def hello(self, ctx):
        await ctx.send(f"Hello {ctx.author.name}!")


# Create the bot instance
bot = Bot()


@app.route('/messages')
def messages():
    return jsonify(bot.last_messages)


@app.route('/')
def serve_html():
    return send_from_directory(os.getcwd(), 'index.html')


def start_flask():
    app.run(debug=False, port=5000)



# Start the Flask server in a separate thread
flask_thread = Thread(target=start_flask)
flask_thread.daemon = True
flask_thread.start()

# Run the Twitch bot
bot.run()
