import json
import os

os.system("Title MagmaTerminal")

configs = os.getcwd() + "/commands/configs"
configs = configs.replace("\\", "/")
allFiles = os.listdir(configs)
for x in allFiles:
    with open(configs + "/" + x) as f:
        load = json.load(f)
        name = load['command']['name']
        desc = load['command']['description']
        print(str(name) + " -- " + str(desc))