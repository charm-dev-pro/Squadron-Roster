# Import os to remove and rename the files
import os

# Function that removes a cadet from the roster
def remove():
    found = False
# Search for the cadet
    search = input('Enter the first name of the cadet you want to remove: ').upper()
    search2 = input('Enter the last name of the cadet you want to remove: ').upper()
    name = search2 + ',' + search
    file = open('roster.txt', 'r')
    temp_file = open('temp.txt','w')
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
# If the name was found write the information to the temporary file
        if cadet != name:
            temp_file.write(f'{cadet}\n')
            temp_file.write(f'{rank}\n')
            temp_file.write(f'{LD}\n')
            temp_file.write(f'{PT}\n')
            temp_file.write(f'{AE}\n')
            temp_file.write(f'{CD}\n')
            temp_file.write(f'{SDA}\n')
            temp_file.write(f'{Board}\n')
            temp_file.write(f'{Drill}\n')
        else:
            found = True
        cadet = file.readline()
    file.close()
    temp_file.close()
# Rename and remove the file
    os.remove('roster.txt')
    os.rename('temp.txt','roster.txt')
    if found:
        print('Cadet has been removed from the roster')
    else:
        print('Cadet could not be removed from the roster.')
