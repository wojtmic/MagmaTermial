import json
import os
import sys

while True:
    command = input("Enter command: ")

    configs = os.getcwd() + "/commands/configs"
    configs = configs.replace("\\", "/")
    scripts = os.getcwd() + "/commands/scripts"
    scripts = scripts.replace("\\", "/")
    allFiles = os.listdir(configs)
    if allFiles != []:
        if os.path.isfile(configs + "/" + command + ".json"):
            pass
        else:
            print("Command not found!")
            sys.exit()
        for x in allFiles:
            with open(configs + "/" + x, 'r') as f:
                if x == command + ".json":
                    load = json.load(f)
                    args = load['command']['arguments']
                    scriptArgs = ""
                    for i in args:
                        argsToAdd = input("Enter " + str(i["value"]) + ": ")
                        scriptArgs = scriptArgs + argsToAdd + " "
                    script = load['command']['script']
                    os.system("python " + scripts + "/" + script + " " + scriptArgs)
