import discord
from threading import Thread
import time

TOKEN = 'NDczNzUxNDE5NjY5OTcwOTQ0.DkGfbg.qQE0BJe9mwq1ihmaStOatt7ObsY'

client = discord.Client()


@client.event
async def on_message(message):

    def start_music(param):
        global a
        global player
        global b
        a = True
        b = 1

        if param == 1:
            def start_music_in_thread():
                channel = client.get_channel("408661560580636682")
                vc = client.join_voice_channel(channel)
                player = vc.create_ffmpeg_player('testing.mp3')
                player.start()
                while a:
                    print("here2")
                    if b == 2:
                        print("here")
                        player.stop()

            music_thread = Thread(target=start_music_in_thread)
            music_thread.start()

        if param == 2:
            a = False
            b = 2
            start_music(2)

    if message.author == client.user:
        return

    if message.content.startswith("!stopp"):
        a = False
        await  client.send_message(message.channel, "Hi")
        start_music(2)

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith("!creator"):
        msg = "My creator is Geneus003"
        msg2 = "EMail: geneus003@gmail.com"
        msg3 = "Qiwi: +79832095427"
        await  client.send_message(message.channel, msg)
        await  client.send_message(message.channel, msg2)
        await  client.send_message(message.channel, msg3)

    if message.content.startswith("!music"):
        msg = "gachi music"
        await  client.send_message(message.channel, msg)
        channel = client.get_channel("408661560580636682")
        vc = await client.join_voice_channel(channel)
        player = vc.create_ffmpeg_player('testing.mp3', after=lambda: print('done'))
        player.start()
        start_music(1)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)