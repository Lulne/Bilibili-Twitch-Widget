# BiliBili Twitch Widget Setup
 
# Step 1
Create a secrets.json file in the project folder with the below structure:
{
    "twitch_secret": "xxx",
    "deepl_auth_key": "xxx"
}

# Step 2
Create a twitch bot through their portal and generate a token for your bot. Next create an deepl account and generate an API key, assign these keys in your json file

# Step 3
In super().__init__ under the bot class, set the initial_channels to an array of channels you want to listen to (your own channel NAME not link)

# Step 4
In Streamlabs or similar software add a new browser source for the URL: http://localhost:5000/ adjust the width and enable custom framerate. Set custom framerate to 60+ to prevent the text from looking jittery during the scrolling animation
