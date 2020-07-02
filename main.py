import discord

client = discord.Client()

# Reading Token from external File
with open(file="token.txt",mode="r") as f:
    token = f.read()

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
    
    class mob:
        
        def __init__(self, name, display, health, damage, type, armor, armor_thoughness, skills, drops):
            self.drops = drops
            self.display = display
            self.name = name
            self.health = int(health)
            self.damage = int(damage)
            self.type = type
            self.armor = float(armor)
            self.skills = skills

        def save(self) -> "Saving the Mob in a file":
            filename = self.name + ".yml"
            with open(filename, 'w+') as f:
                f.write(self.name + ":\n  Display: " + self.display + "\n  Type: " + self.type + "\n  Health: " +
                        str(self.health) + "\n  Damage: " + str(self.damage) + "\n  Armor:" + str(self.armor) + 
                        "\n  Skills:\n    " + self.skills())

client.run(token)
