import discord, os, re, command

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


# Setup procedure

# Needed default Values

question_number = int(0)
editor_mode = bool(0)
creator_mode = bool(0)
mob_name = str("")

# Blank Mob Object which is being edited
editing_mob = mythicmob.mob(name=mob_name)
# Question Protocol
@client.event
async def on_message(message):
    global editor_mode
    global help_menu
    global creator_mode
    if message.author == client.user:
        return
    # Command to enter the editor mode | Editor mode shall be only activated for messages sent by the user who
    # activated it
    if message.startswith("$mm create"):
        await message.channel.send("You are entering Creator Mode!")
        await message.channel.send(help_menu)
        creator_mode = 1
    if message.startswith("$mm edit"):
        await message.channel.send("You are entering Editor Mode! for" + editing_mob.name())
        await message.channel.send(help_menu)
        creator_mode = 1
    if message.startswith(command.select(0)) & editor_mode:
        # Everything after "mm [command] > " is considered a command argument
        # TODO Create function which read the arguments and sets the specified values
        command_arguments = []
        pass
        # Search the message string sent by the user who entered the creator mode


client.run(token)
