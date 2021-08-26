import discord
from discord.ext import commands
import sys
from asyncio.tasks import sleep

import requests
from bs4 import BeautifulSoup
import re


#Gain bot's token, stored in seperate file for security
f = open('token.txt', 'r')
TOKEN = f.read()
f.close()

#Set bot's prefix
client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
    print("Bot is ready")
    #await client.change_presence(activity=discord.Game(name='that grind'))

@client.event
async def on_message(message):
    if(message.content == "<:bagger1:620408099571761166><:bagger2:620408100385456128><:bagger3:620408099920150563>" or 
    message.content == "<:bagger1:620408099571761166> <:bagger2:620408100385456128> <:bagger3:620408099920150563>"):
        print("Bagger288")
        channel = client.get_channel(181058167487070208)
        audio_source = discord.FFmpegPCMAudio("bagger288.mp3")
        vc = await channel.connect()
        player = vc.play(audio_source, after=None)
        while vc.is_playing():
            await sleep(1)
        await vc.disconnect()

    elif("https://ifunny.co/" in message.content):
        ifunnyLink = message.content.split(" ")[-1]

        if("picture" in ifunnyLink):

            html = requests.get(ifunnyLink, headers={'User-Agent': 'Mozilla/5.0'})
            bs = BeautifulSoup(html.text, "html5lib")
            images = bs.find_all('img', {'data-src': re.compile(r'img.ifunny.co')})

            await message.channel.send(images[0].attrs['data-src'])

        elif("video" in ifunnyLink):
            html = requests.get(ifunnyLink, headers={'User-Agent': 'Mozilla/5.0'})
            bs = BeautifulSoup(html.text, "html.parser")

            videos = bs.find_all('video', {'data-src': re.compile(r'img.ifunny.co')})

            await message.channel.send(videos[0].attrs['data-src'])


client.run(TOKEN)