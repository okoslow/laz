
#imports, globals
####################################################################################################################
import webbrowser
# import urllib.request
# import json
import subprocess
import random
import datetime
import os
####################################################################################################################
GOOGLE_API_KEY = 'AIzaSyAO6Hgd8SRecYqkEicR4NkW0Q80PHG0jHM'
SLEEPFILE = os.path.abspath('.timewrites')
BLOCKFILE = os.path.abspath('.currentlyblocked')
BLOCKED = False
WEB_ACCESS = True
####################################################################################################################
def run_bash(bash_command):
    bash_output = str(subprocess.check_output(['bash','-c', bash_command]))
    return bash_output

####################################################################################################################
def whoami():
    bash_command = "id -F"
    whoami = run_bash(bash_command)
    whoami = whoami[2:len(whoami)-3]
    return whoami

unicode_emote = ["☺☻♡♥❤⚘❀❃❁✼☀✌♫♪☃❄❅❆☕☂★","｡◕‿‿◕｡","(｡◕‿‿◕｡)","(ಠ‿ಠ)","♥‿♥","(¬‿¬)","ʕ•ᴥ•ʔ","(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧","(ᵔᴥᵔ)","(•ω•)","☜(⌒▽⌒)☞","(づ｡◕‿‿◕｡)づ","(╯°□°）╯︵ ┻━┻","٩(⁎❛ᴗ❛⁎)۶","¯\_(ツ)_/¯"]

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
    return " "

def web_access_handler(block_state):
    if block_state:
        WEB_ACCESS = False
    return WEB_ACCESS

def greet(name):
    BLOCKED = get_block_status()
    if BLOCKED:
        block_message = "\nYou are currently blocked."
    else:
        block_message = ""
    return "Welcome, " + name + " " + unicode_emote[random.randrange(0, len(unicode_emote)-1)] + block_message
####################################################################################################################

common_sites = {

    #social media
    "fb" : "facebook.com",
    "facebook" : "facebook.com",

    #streaming
    "solarmovie": "solarmoviez.to",
    "sm": "solarmoviez.to",
    "couchtuner": "couchtuner.nu",
    "other couchtuner": "couchtuner.video",
    "sockshare": "sockshare.net",

    #news
    "nytimes": "nytimes.com",
    "nyer": "newyorker.com",

    #dev
    "localhost": "localhost:3003", #add support for different ports
    "work": "localhost:3003",
    "local": "localhost:3003",
    "pydocs": "docs.python.org/",
    "stack": "stackoverflow.com",
    "stackoverflow": "stackoverflow.com",
    "github": "github.com",
    "gerrit": "code.brigade.zone",
    "jira": "brigade.atlassian.net/secure/Dashboard.jspa",
    "latex": "sharelatex.com"
}

####################################################################################################################

print(greet(whoami()))
command = str(input("What do you want to do? \n")).lower()

####################################################################################################################

def navigate_web(command):
     if "go" in command and "to" in command:
         relevant = command[command.index("to") + 2:]
     elif "open" not in command:
         relevant = command[command.index("me") + 2:]
     else:
         relevant = command[command.index("open") + 4:]
     desired_site = relevant.strip()

     if desired_site.isalpha() and desired_site in common_sites:
         website = common_sites[desired_site]
         print(website)
     else: #ideal behavior: google top result, steal extension and use it
         website = desired_site + ".com"

     return webbrowser.open_new_tab('http://' + website )  # Go to example.com

####################################################################################################################

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

    return "Your timeblock has been scheduled.  Good luck! " + unicode_emote[random.randrange(0, len(unicode_emote)-1)]

def wake_update():
    target_file = open(SLEEPFILE, 'r')
    wake_time = target_file.read()
    wake_time = datetime.datetime.strptime(wake_time, '%m %d %Y %H:%M')
    # target_file.close()
    # return wake_time
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


####################################################################################################################

BLOCKED = get_block_status()
WEB_ACCESS = web_access_handler(BLOCKED)


def command_handler(command):
    if "go" in command and "to" in command or "goto" in command or "showme" in command:
        if WEB_ACCESS:
            navigate_web(command)
            return ""
        else:
            return "You don't currently have web access."
    elif "headsdownfor" in command:
        return scheduler(command)
    elif "blocktime" in command or "time" in command:
        return wake_update()
    elif "unblock" in command:
        return unblock()
    else:
        return "Invalid command"

print(command_handler(command))
