# Function that searches for a cadet and prints their current status
def check_progress():
    found = False
# Search for name
    search = input('Enter the first name of a cadet: ').upper()
    search2 = input('Enter the last name of a cadet: ').upper()
    name = search2 + ',' + search
    file = open('roster.txt', 'r')
    cadet = file.readline()
    while cadet != '':
        rank = file.readline().rstrip('\n')
        cadet = cadet.rstrip('\n')
        LD = file.readline().rstrip('\n')
        PT = file.readline().rstrip('\n')
        AE = file.readline().rstrip('\n')
        CD = file.readline().rstrip('\n')
        SDA = file.readline().rstrip('\n')
        Board = file.readline().rstrip('\n')
        Drill = file.readline().rstrip('\n')
# Print the information if the name was in the roster
        if cadet == name:
            print(name)
            print(rank)
            print(LD)
            print(PT)
            print(AE)
            print(CD)
            print(SDA)
            print(Board)
            print(Drill)
            found = True
        cadet = file.readline()
    file.close()
    if not found:
        print('The cadet was not found in the roster.')

