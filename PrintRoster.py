# Function that prints the roster
def print_roster():
    file = open('roster.txt','r')
    contents = file.read()
    print(contents)
