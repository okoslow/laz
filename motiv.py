import os
MOTIVFILE = os.path.abspath('.motiv')

def plus_one():
    score = str(get_score(True) + 1)
    target_file = open(MOTIVFILE, 'w')
    target_file.write(score)
    target_file.close()
    return "Yay!! A job well done <3."

def get_score(silent):
    target_file = open(MOTIVFILE)
    content = target_file.read()
    target_file.close()
    if silent:
        return int(content)
    else:
        return "Your score is now: " + str(content)
