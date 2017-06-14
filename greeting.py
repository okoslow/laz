import random
import os
import scheduler

NAMEFILE = os.path.abspath('.customname')

def whoami():
    bash_command = "id -F"
    whoami = run_bash(bash_command, False)
    return whoami

def nickname(command):
    relevant = command[command.index("me") + 2: ]
    name = relevant.strip()
    target_file = open(NAMEFILE, 'w')
    target_file.write(name)
    target_file.close()
    return "Your new name has been set!"

def getname():
    target_file = open(NAMEFILE, 'r')
    contents = target_file.read()
    if contents.isalnum():
        target_file.close()
        return contents
    target_file.close()
    return whoami()

UNICODEEMOTE = ["☺☻♡♥❤⚘❀❃❁✼☀✌♫♪☃❄❅❆☕☂★","｡◕‿‿◕｡","(｡◕‿‿◕｡)","(ಠ‿ಠ)","♥‿♥","(¬‿¬)","ʕ•ᴥ•ʔ","(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧","(ᵔᴥᵔ)","(•ω•)","☜(⌒▽⌒)☞","(づ｡◕‿‿◕｡)づ","(╯°□°）╯︵ ┻━┻","٩(⁎❛ᴗ❛⁎)۶","¯\_(ツ)_/¯"]

def greet(name):
    BLOCKED = scheduler.get_block_status()
    if BLOCKED:
        block_message = "\nYou are currently blocked."
    else:
        block_message = "\n"
    return "\nWelcome, " + name + " " + UNICODEEMOTE[random.randrange(0, len(UNICODEEMOTE)-1)] + block_message
