import discord, os, re
# TODO



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

def answerFormator(text):
    modifiedResult = text[1:len(text)]
    return modifiedResult

# Setup procedure

# Needed default Values

question_number = int(0)
mob_name = str("")
mob_display = str("")
mob_health = 0
mob_damage = 0
mob_type = str("")
mob_armor = 0
mob_armor_thoughness = 0
mob_skills = ""
mob_drops = ""
mob_options = ""
mob_creator_mode = False

question_number = 0
# Blank Mob Object which is being edited
editing_mob = mythicmob.mob(name=mob_name, display=mob_display, health=mob_health, damage=mob_damage, type=mob_type, armor=mob_armor, armor_thoughness=mob_armor_thoughness, skills=mob_skills, drops=mob_drops, options=mob_options)
# Question Protocol
@client.event
async def on_message(message):
    global help_menu
    global question_number
    if message.author == client.user:
        return
    # Command to enter the editor mode | Editor mode shall be only activated for messages sent by the user who
    # activated it
    if message.content == "$mm create":

        await message.channel.send("What should the mobs internal Name be? "
                                   "(NOTE THIS ISNT ITS DISPLAY NAME)\n\n"
                                   "type \"$\" before your answers to the questions")

        question_number = 1
    # Question Protocol


    # Question 1 Name
    if message.content[0] == "$" and question_number == 1:

        editing_mob.name = answerFormator(message.content)
        print(editing_mob.name)

        question_number = 2
        await message.channel.send("Mobs Display Name?")
    # Question 2 Display
    if message.content[0] == "$" and question_number == 2:

        editing_mob.name = answerFormator(message.content)
        print(editing_mob.name)

        question_number = 3
    # Question 3 Health
    if message.content[0] == "$" and question_number == 4:

        editing_mob.name = answerFormator(message.content)
        print(editing_mob.name)

        question_number = 4
        await message.channel.send("Mobs Damage?")
    # Question 4 Damage
    if message.content[0] == "$" and question_number == 5:

        editing_mob.name = answerFormator(message.content)
        print(editing_mob.name)

        question_number = 5
    # Question 5 Type
    if message.content[0] == "$" and question_number == 1:

        editing_mob.name = answerFormator(message.content)
        print(editing_mob.name)

        question_number = 6

    if question_number == 6:
        editing_mob.save()





client.run(token)
