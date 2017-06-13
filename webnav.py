from packages import *


def navigate_web(command):
     if "go" in command and "to" in command:
         relevant = command[command.index("to") + 2:]
     elif "open" not in command:
         relevant = command[command.index("me") + 2:]
     else:
         relevant = command[command.index("open") + 4:]
     desired_site = relevant.strip()

     if desired_site.isalpha() and desired_site in commons.common_sites:
         website = commons.common_sites[desired_site]
         print(website)
     else: #ideal behavior: google top result, steal extension and use it
         website = desired_site + ".com"

     return webbrowser.open_new_tab('http://' + website )  # Go to example.com
