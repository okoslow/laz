
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

unicode_emote = ["☺☻☹♡♥❤⚘❀❃❁✼☀✌♫♪☃❄❅❆☕☂★","｡◕‿‿◕｡","(｡◕‿‿◕｡)","(ಠ‿ಠ)","♥‿♥","(¬‿¬)","ʕ•ᴥ•ʔ","(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧","(ᵔᴥᵔ)","(•ω•)","☜(⌒▽⌒)☞","(づ｡◕‿‿◕｡)づ","(╯°□°）╯︵ ┻━┻","٩(⁎❛ᴗ❛⁎)۶","¯\_(ツ)_/¯"]

def greet(name):
    return "Welcome, " + name + " " + unicode_emote[random.randrange(0, len(unicode_emote)-1)]
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
    target_file.write(str(sleep_seconds))
    target_file.close()
    return sleep_seconds

####################################################################################################################
def command_handler(command):
    if "go" in command and "to" in command or "show" and "me" in command or "open" in command:
        return navigate_web(command)
    elif "heads down for" in command:
        return scheduler(command)

print(command_handler(command))
