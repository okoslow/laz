 #LOOK MA NO MOUSE
####################################################################################################################
import datetime
import scheduler
import greeting
import webnav
import history
import commons
import terminal
import music
import os
# ####################################################################################################################
GOOGLE_API_KEY = 'AIzaSyAO6Hgd8SRecYqkEicR4NkW0Q80PHG0jHM'
# ####################################################################################################################
CURRENTDIR = terminal.run_bash('pwd', True)
LOCALDIR = terminal.run_bash('cd ~/', True)
# ####################################################################################################################
def validity_checker(command):
    for valid_command in commons.valid_commands:
        if valid_command in command:
            return True

def command_handler(): #eventually turn this into a command->fn dict
    command = ""
    while "quit" not in command  or "exit" not in command or "nothing" not in command or "go" not in command:
        command = str(input("What do you want to do? \n")).lower()
        if "go" in command and "to" in command or "goto" in command or "show" in command and "me" in command:
            if True:
                webnav.navigate_web(command)
                print("Launching web.")
            else:
                print("You don't currently have web access.")
        elif "headsdownfor" in command or "hdfor" in command:
            print(scheduler.scheduler(command))
        elif "blocktime" in command or "time" in command:
            print(scheduler.wake_update())
        elif "unblock" in command:
            print(scheduler.unblock())
        elif "callme" in command or "call me" in command:
            print(greeting.nickname(command))
        elif "lyrics" in command and "by" in command:
            print(music.query_handler(command))
        elif "run" in command:
            print(terminal.run_bash(command[command.index("run")+3:]))
        elif "quit" in command  or "exit" in command or "nothing" in command or "go" in command:
            break
        else:
            print("Invalid command: " + command)

        if validity_checker(command):
            history.add_to_history(command)
    return "Have a nice day! (=^..^=)"

####################################################################################################################
# execution block
BLOCKED = scheduler.get_block_status()
WEB_ACCESS = scheduler.web_access_handler(BLOCKED)

print(greeting.greet(greeting.getname()))
print(history.output_recents(history.x_in_y_most_recents(4, 20)))
results = command_handler()
print(results)

RETURNDIR = terminal.run_bash('cd ' + LOCALDIR, True)
