def select(number):
    commands = ("set", "edit", "save", "discard")
    try:
        return str("mm " + commands[number] + " > ")
    except:
        pass
def arguments(command):
    x = len(command -1)
    return command[x:]
