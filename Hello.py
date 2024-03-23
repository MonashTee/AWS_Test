import json
filename = "userName.json"
name = ""
#check for a history file
try:
    with open (filename) as f:
        name = json.load(f)
except FileNotFoundError:
    name = input("Hello! what's your name?")
    with open(filename, "w") as f:
        json.dump(name,f)
        print("We'll remember you when you come back, "+ name+ "!")

# If the user was found in the history file, welcome them back
        if name == json.load(f):
            print("welcome back, " + name + "!")
else:
    print("welcome back, " + name + "!")
