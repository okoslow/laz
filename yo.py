 #LOOK MA NO MOUSE
####################################################################################################################
import webbrowser
import subprocess
import random
import datetime
import os
# ####################################################################################################################
GOOGLE_API_KEY = 'AIzaSyAO6Hgd8SRecYqkEicR4NkW0Q80PHG0jHM'
SLEEPFILE = ""
BLOCKFILE = ""
NAMEFILE = ""
HISTORYFILE = ""
# ####################################################################################################################
def run_bash(bash_command, silent):
    bash_output = subprocess.check_output(['bash','-c', bash_command])
    if not silent:
        return str(bash_output)[2:len(str(bash_output)) -3]
    else:
        return ""
# ####################################################################################################################
CURRENTDIR = run_bash('pwd', True)
LOCALDIR = run_bash('cd ~/', True)
SLEEPFILE = os.path.abspath('.timewrites')
BLOCKFILE = os.path.abspath('.currentlyblocked')
NAMEFILE = os.path.abspath('.customname')
HISTORYFILE = os.path.abspath('.commandhistory')
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

unicode_emote = ["☺☻♡♥❤⚘❀❃❁✼☀✌♫♪☃❄❅❆☕☂★","｡◕‿‿◕｡","(｡◕‿‿◕｡)","(ಠ‿ಠ)","♥‿♥","(¬‿¬)","ʕ•ᴥ•ʔ","(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧","(ᵔᴥᵔ)","(•ω•)","☜(⌒▽⌒)☞","(づ｡◕‿‿◕｡)づ","(╯°□°）╯︵ ┻━┻","٩(⁎❛ᴗ❛⁎)۶","¯\_(ツ)_/¯"]

def greet(name):
    BLOCKED = get_block_status()
    if BLOCKED:
        block_message = "\nYou are currently blocked."
    else:
        block_message = ""
    return "Welcome, " + name + " " + unicode_emote[random.randrange(0, len(unicode_emote)-1)] + block_message
# ####################################################################################################################
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

valid_commands = [
    "go to",
    "goto",
    "show me",
    "showme",
    "headsdownfor",
    "hdfor",
    "blocktime",
    "time",
    "unblock",
    "callme",
    "call me",
    "run",
    "quit",
    "exit",
    "nothing",
    "go",
]
# ####################################################################################################################
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

    return "Your timeblock has been scheduled.  Good luck! " + unicode_emote[random.randrange(0, len(unicode_emote)-1)]

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

# ####################################################################################################################
def validity_checker(command):
    for valid_command in valid_commands:
        if valid_command in command:
            return True

def add_to_history(element):
    to_write = element + "\n"
    target_file = open(HISTORYFILE, 'a')
    target_file.write(to_write)
    target_file.close()
    return

def command_handler(): #eventually turn this into a command->fn dict
    command = ""
    while "quit" not in command  or "exit" not in command or "nothing" not in command or "go" not in command:
        command = str(input("What do you want to do? \n")).lower()
        if "go" in command and "to" in command or "goto" in command or "show" in command and "me" in command:
            if WEB_ACCESS:
                navigate_web(command)
                print("Launching web.")
            else:
                print("You don't currently have web access.")
        elif "headsdownfor" in command or "hdfor" in command:
            print(scheduler(command))
        elif "blocktime" in command or "time" in command:
            print(wake_update())
        elif "unblock" in command:
            print(unblock())
        elif "callme" in command or "call me" in command:
            print(nickname(command))
        elif "run" in command:
            print(run_bash(command[command.index("run")+3:]))
        elif "quit" in command  or "exit" in command or "nothing" in command or "go" in command:
            break
        else:
            print("Invalid command: " + command)

        if validity_checker(command):
            add_to_history(command)
    return "Have a nice day! (=^..^=)"

####################################################################################################################
# execution block
BLOCKED = get_block_status()
WEB_ACCESS = web_access_handler(BLOCKED)

print(greet(getname()))
results = command_handler()
print(results)

RETURNDIR = run_bash('cd ' + LOCALDIR, True)
