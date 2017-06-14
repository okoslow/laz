import subprocess

def run_bash(bash_command, silent):
    bash_output = subprocess.check_output(['bash','-c', bash_command])
    if not silent:
        return str(bash_output)[2:len(str(bash_output)) -3]
    else:
        return ""
