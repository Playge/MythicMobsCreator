import discord


#TODO
#  IMPROVE SKILL CREATOR, BY MAKING LIST OF ALL MECHANICS, TARGETERS AND TRIGGERS POSSIBLE AND PRINT THEM OUT
#  FINISH UP QUESTIONAIR
#  CREATE GUI WHICH CAN BE USED IN DISCORD WITH REACIONS
#  CREATE GUI APPLICATION FOR WINDOW, MAC, AND LINUX
#  CREATE WEBPAGE TO MAKE MYTHICMOBS

# Basic Discord Stuff

# Reading the token.txt file
def read_token():
    with open('token.txt', 'r') as f:
        lines = f.readlines()
        return lines[0].strip


# Simplefying variables
token = read_token()
client = discord.Client()


# Playges Discord Mythic Mob Creator v1#

@client.event
class mythicmobs:
    class help:

        # Creating and Printing the help menu


        def help_menu(page):
            help_commands = {
                "Create": "Make a new Mythic mob.",
                "Delete": "Delete a Mob File",  # Want to add Single Mob Deleting soon
                "Edit": "Edit a Mob. All the Mob Stats will be sent into the Chat!",
                "Quit": "Quit the Editor Mode",
                "Lang": "Change the Languages"
            }

            async def on_message(message):
                await message.channel.send("--=Mythic Mob Creator=--" + "\n\n" + "Help:")
                await message.channel.send("Create" + help_commands["Create"])
                await message.channel.send(("Delete" + help_commands["Delete"]))

    # Class Representing the Mob that wll be Created

    class mob:

        #Creating A Skill Mechanic
        def skill(self, mechanic, targeter, trigger):
            try:
                done_skill = str(mechanic) + str(targeter) + str(trigger)
                return done_skill

        #If the Skill isnt setup in the correct way it will print an Error
            except:
                print("Error, your Skill can not be made")

                async def on_message(message):
                    await message.channel.send("Error in Mechanics. Please only use full Words")

        def __init__(self, name, display, health, damage, type, armor, armor_thoughness, skills, drops):
            self.drops = drops
            self.display = display
            self.name = name
            self.health = int(health)
            self.damage = damage
            self.type = type
            self.armor = float(armor)
            self.skills = skills

        def save(self) -> "Saving the Mob in a file":
            filename = self.name + ".yml"
            with open(filename, 'w+') as f:
                f.write(self.name + ":\n  Display: " + self.display + "\n  Type: " + self.type + "\n  Health: " +
                        self.health + "\n  Damage: " + self.damage + "\n  Armor:" + self.armor + "\n  Skills:\n    " +
                        self.skills())


# Class Representing me

class Creator:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

    # Sending infos about me and doing advertisement for my Discord Server
    def infos(self):
        print(self.name)
        print(self.contact)

        @client.event
        async def on_ready(message):
            await message.channel.send("This bot was made by " + self.name)
            await message.channel.send("If you would like to talk to me just join my discord")
            await message.channel.send(self.contact)


# Defining the Class that Represents me the Creator
Playge = Creator("Playge", "LEGIS WORLD | https://discord.gg/t2yXATy")

# Printing my Name and Discord
Playge.infos()


#################
# Creating a mob#
#################

# Saving and Creating a Mob

@client.event
async def on_message(message):
    def reminder():
        return("Start your answer with \"$\"")

    #Saving the authors name so the programm only takes input form that User
    prev_author = message.author

    #Creating an Empty Mob
    newmob = mythicmobs.mob()

    # Formatting the Quesition into Code highliting to make it more readable for the user
    def question(question):
        await message.channel.send("```" + question + "```")

    # Opening The help Menu
    if message.content.startwith("mm help"):
        mythicmobs.help()

    # Starting the Creation Process if someone Types mm create
    if message.content.startwith("mm create"):
        await message.channel.send("```ENTERING CREATOR MODE\n--------------------```\nStart Every Answer with \"$\"")
        counter = 1

    #Asking the Questions to get Informations on the Mob
    if counter == 1:
        question("What should the Mob Name be?" + reminder())
        if message.startwith("$"):
            newmob.name = message[1:]
            counter += 1
    if counter == 2:
        question("What do you want the Mob to be displayed as?" + reminder())
        if message.startwith("$"):
            newmob.name = message[1:]
            counter += 1
    if counter == 3:
        question("How Much Health shall the mob have?")
        if message.startwith("$"):
            newmob.health = message[1:]
            counter += 1
    if counter == 4:
        question("How much Armor Shall the Mob have")
        if message.startwith:
            newmob.armor = message[1:]
            counter += 1
    newmob.save()
