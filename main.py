import discord, os, re

client = discord.Client()

# Reading Token from external File
with open(file="token.txt", mode="r") as f:
    token = f.read()

# Help Document with all commands in it
with open(file="help.txt", mode="r") as f:
    help_menu = f.read()

# Startup Logic
@client.event
async def on_ready():
    print("MythicCreator v.1 logged in as {0.user}".format(client))
    print("")
    print("Creator: Playge")


@client.event
async def on_message(message):
    if message.author == client.user:
        return


class mythicmob:
    class help:
        def page(self, type):
            if type == "name":
                return()
    class mob:

        def __init__(self, name, display, health, damage, type, armor, armor_thoughness, skills, drops, options):
            self.drops = drops
            self.display = display
            self.name = name
            self.health = int(health)
            self.damage = int(damage)
            self.type = type
            self.armor_thoughness = float(armor_thoughness)
            self.armor = float(armor)
            self.skills = skills
            self.options = options

        # Saving and Formatting proccedure
        def save(self) -> "Saving the Mob in a file":
            filename = self.name + ".yml"
            with open(filename, 'w+') as f:
                f.write(self.name + ":\n  Display: " + self.display +
                        "\n  Type: " + self.type +
                        "\n  Health: " + str(self.health) +
                        "\n  Damage: " + str(self.damage) +
                        "\n  Armor:" + str(self.armor) +
                        "\n  Armor_toughness:" + str(self.armor_thoughness) +
                        "\n  Skills:\n    " + self.skills())


# The Questionaire which retrieves all the wanted values

# Needed Values

question_number = 1
editor_mode = 0

# All Commands with their aliases
def command(number):
    commands = ("set", "edit", "save", "discard")
    try:
        return str("mm " + commands[number] + "> ")
    except:
        return

# Question Protocol
@client.event
async def on_message(message):
    global editor_mode
    global help_menu
    if message.author == client.user:
        return
    # Command to enter the editor mode | Editor mode shall be only activated for messages sent by the user who 
    # activated it 
    if message.startswith("$mm create"):
        await message.channel.send("You are entering Editor Mode!")
        await message.channel.send(help_menu)
        editor_mode = 1
    if message.startswith(command(0)) & editor_mode:
        # Everything after "mm [command] > " is considered a command argument
        # TODO Create function which read the arguments and sets the specified values
        command_arguments = []
        pass
        # Search the message string sent by the user who entered the creator mode


client.run(token)
