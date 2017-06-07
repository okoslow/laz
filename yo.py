
#imports
####################################################################################################################

import webbrowser

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

command = str(input("What do you want to do?")).lower()

####################################################################################################################

if "go" in command and "to" in command or "show" and "me" in command :
     ######
     #parsing
     if "go" in command and "to" in command:
         relevant = command[command.index("to") + 2:]
     else:
         relevant = command[command.index("me") + 2:]
     desired_site = relevant.strip()

     ######
     #fetching
     if desired_site.isalpha() and desired_site in common_sites:
         website = common_sites[desired_site]
         print(website)
     else: #ideal behavior: google top result, steal extension and use it
         website = desired_site + ".com"

     ######
     #opening
     webbrowser.get('safari')
     webbrowser.open_new_tab('http://' + website )  # Go to example.com
