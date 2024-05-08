import discord
from responses import doResponse
from scehduler import scheduler
#make the timer work in here thru an event, just call the methods ig

async def send_message(message, user_message,):
    response = doResponse(user_message)

def runBot():
    TOKEN = 
    client = discord.Client(intents=discord.Intents.default())

    @client.event
    async def on_ready():
        print("im working")
        scheduler()
    
    client.run(TOKEN)

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        channel = str(message.channel)
