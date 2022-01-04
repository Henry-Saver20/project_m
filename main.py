import discord
import os
from discord.utils import sleep_until
from dotenv import load_dotenv
from discord.ext import commands, tasks
import time
import asyncio

load_dotenv()

intents = discord.Intents().all()

client = commands.Bot(command_prefix='!',intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Yoooo whats up '  + str(message.author) + '!')
    await client.process_commands(message)


@client.command(name="letsgo")
async def play_audio(ctx):
        print("called")
        # Gets voice channel of message author
        voice_channel = ctx.author.voice.channel
        channel = None
        if voice_channel != None:
            channel = voice_channel.name
            vc = await voice_channel.connect()
            p = r".\sounds\letsGo.mp3"
            exe_p = r".\ffmpeg\bin\ffmpeg.exe"
            vc.play(discord.FFmpegPCMAudio(executable=exe_p, source=p))
            # Sleep while audio is playing.
            while vc.is_playing():
                time.sleep(5)
            await vc.disconnect()
        else:
            await ctx.send(str(ctx.author.name) + "is not in a channel.")
        # Delete command after the audio is done playing.
        await ctx.message.delete()

@client.command(name="sloppy")
async def play_audio(ctx):
        print("called")
        # Gets voice channel of message author
        voice_channel = ctx.author.voice.channel
        channel = None
        if voice_channel != None:
            channel = voice_channel.name
            vc = await voice_channel.connect()
            p = r".\sounds\sloppy.mp3"
            exe_p = r".\ffmpeg\bin\ffmpeg.exe"
            vc.play(discord.FFmpegPCMAudio(executable=exe_p, source=p))
            # Sleep while audio is playing.
            while vc.is_playing():
                time.sleep(5)
            await vc.disconnect()
        else:
            await ctx.send(str(ctx.author.name) + "is not in a channel.")
        # Delete command after the audio is done playing.
        await ctx.message.delete()

client.run(os.getenv('TOKEN'))


