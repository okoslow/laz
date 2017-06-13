import os
HISTORYFILE = os.path.abspath('.commandhistory')

def add_to_history(element):
    to_write = element + "\n"
    target_file = open(HISTORYFILE, 'a')
    target_file.write(to_write)
    target_file.close()
    return

def read_history():
    command_history = []
    target_file = open(HISTORYFILE)
    content = target_file.readlines()
    for line in content:
        command_history.append(line[0:len(line)-1])
    target_file.close()
    return command_history

def get_recents(lookback): #looks through [lookback] past commands
    history = read_history()
    return history[len(history) - lookback:]

def get_freqs(history):
    frequency_count = {}
    for item in history:
        if item in frequency_count:
            frequency_count[item] += 1
        else:
            frequency_count[item] = 1

    frequencies = []
    for unique_command in frequency_count:
        frequencies.append(frequency_count[unique_command])
    frequencies.sort()
    return frequency_count, frequencies

def get_used_task(frequency_count, frq_val):
    most_used = ""
    for unique_command in frequency_count:
        if frequency_count[unique_command] == frq_val:
             most_used = unique_command
    return most_used

def x_in_y_most_recents(x, y):
    history = get_recents(y)
    frequency_count, frequencies = get_freqs(history)
    most_recently_used = []
    for i in range(x):
        if len(frequencies) - i > 0:
            most_recently_used.append(get_used_task(frequency_count, frequencies[i]))
    return list(reversed(most_recently_used))

def output_recents(history_array):
    print("Would you like to: ")
    for i in range(len(history_array)):
        if i == len(history_array)-1:
            print(" - " + history_array[i] + " ?")
        else:
            print(" - " + history_array[i])
    return ""
