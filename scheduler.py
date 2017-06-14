import random
import datetime
import os

SLEEPFILE = os.path.abspath('.timewrites')
BLOCKFILE = os.path.abspath('.currentlyblocked')
UNICODEEMOTE = ["☺☻♡♥❤⚘❀❃❁✼☀✌♫♪☃❄❅❆☕☂★","｡◕‿‿◕｡","(｡◕‿‿◕｡)","(ಠ‿ಠ)","♥‿♥","(¬‿¬)","ʕ•ᴥ•ʔ","(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧","(ᵔᴥᵔ)","(•ω•)","☜(⌒▽⌒)☞","(づ｡◕‿‿◕｡)づ","(╯°□°）╯︵ ┻━┻","٩(⁎❛ᴗ❛⁎)۶","¯\_(ツ)_/¯"]

# ####################################################################################################################

def get_block_status():
    target_file = open(BLOCKFILE, 'r')
    block_status = target_file.read()
    target_file.close()
    BLOCKED = False
    if block_status == "ON":
        BLOCKED = True
    return BLOCKED

def unblock():
    target_file = open(BLOCKFILE, 'w')
    block_status = target_file.truncate()
    target_file.close()
    return "Your block time has been removed."

def web_access_handler(block_state):
    WEB_ACCESS = True
    if block_state:
        WEB_ACCESS = False
    return WEB_ACCESS

# ####################################################################################################################

def scheduler(command):
    relevant = command[command.index("for") + 3:]
    if "hours" in relevant:
        relevant = relevant[0:relevant.index("hours")]
        relevant = relevant.strip()
        sleep_seconds = int(relevant)*3600
    elif "minutes" or "mins" in relevant:
        relevant = relevant[0:relevant.index("min")]
        relevant = relevant.strip()
        sleep_seconds = int(relevant)*60
    else:
        return "Please enter a valid unit of time (minutes or hours)."

    target_file = open(SLEEPFILE, 'w')
    unform_wake = datetime.datetime.now() + datetime.timedelta(seconds=sleep_seconds)
    timewrite = str(unform_wake.month) + " " + str(unform_wake.day) + " " + str(unform_wake.year) + " " + str(unform_wake.hour) + ":" + str(unform_wake.minute)
    target_file.write(timewrite)
    target_file.close()
    BLOCKED = True

    new_target = open(BLOCKFILE, 'w')
    write_block = new_target.write("ON")
    new_target.close()

    return "Your timeblock has been scheduled.  Good luck! " + UNICODEEMOTE[random.randrange(0, len(UNICODEEMOTE)-1)]

def wake_update():
    target_file = open(SLEEPFILE, 'r')
    wake_time = target_file.read()
    wake_time = datetime.datetime.strptime(wake_time, '%m %d %Y %H:%M')
    time_till_wake = datetime.datetime.now() - wake_time
    if "-" in str(time_till_wake):
        target_file.truncate() #empty wakefile
        target_file.close()
        new_target = open(BLOCKFILE, 'w') #clear blockfile
        new_target.truncate()
        new_target.close()

        BLOCKED = False
        return "You're not currently assigned a block!"
    else:
        target_file.close()
        BLOCKED = True
        return "You have " + str(time_till_wake) + " left."
