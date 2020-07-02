import discord

client = discord.Client()

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$Testing"):
        await message.channel.send("Hello!")

client.run("NzI4MTc0NTg1NTQyODY5MTEy.Xv2kEA.AVA_PA8pTB2ixnp5IzP-582E274")
