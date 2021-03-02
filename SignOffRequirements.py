# Import os to rename and remove the files
import os

# Function that prints the menu options
def sign_off_menu():
    print('Which one would you like to sign off?')
    print('1) Leadership test')
    print('2) PT test')
    print('3) Aerospace Test')
    print('4) Character Development')
    print('5) SDA')
    print('6) Promotion Board')
    print('7) Drill Test')

# Function that signs off on promotion requirements
def sign_off():
    found = False
# Get the cadet's name and search in the file
    cadet_first = input('Enter the first name of a cadet: ').upper()
    cadet_last = input('Enter the last name of a cadet: ').upper()
    name = cadet_last + ',' + cadet_first
    file = open('roster.txt','r')
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
# Call the menu if the name is found and enter the choice
        if cadet == name:
            sign_off_menu()
            choice = int(input('Enter choice: '))
# If statements that perform the tasks assigned with their choice. This will update the information
            if choice == 1:
                print(LD)
                new = input('Enter "YES", "NO", or "N/A: ').upper()
                if new == 'YES' or 'NO' or 'N/A':
                    temp_file.write(name + '\n')
                    temp_file.write(rank + '\n')
                    temp_file.write(f'Leadership:{new}' + '\n')
                    temp_file.write(PT + '\n')
                    temp_file.write(AE + '\n')
                    temp_file.write(CD + '\n')
                    temp_file.write(SDA + '\n')
                    temp_file.write(Board + '\n')
                    temp_file.write(Drill + '\n')
                    found = True
                else:
                    found = False
            elif choice == 2:
                print(PT)
                new = input('Enter "YES", "NO", or "N/A: ').upper()
                if new == 'YES' or 'NO' or 'N/A':
                    temp_file.write(name + '\n')
                    temp_file.write(rank + '\n')
                    temp_file.write(LD + '\n')
                    temp_file.write(f'PT:{new}' + '\n')
                    temp_file.write(AE + '\n')
                    temp_file.write(CD + '\n')
                    temp_file.write(SDA + '\n')
                    temp_file.write(Board + '\n')
                    temp_file.write(Drill + '\n')
                    found = True
                else:
                    found = False
            elif choice == 3:
                print(AE)
                new = input('Enter "YES", "NO", or "N/A: ').upper()
                if new == 'YES' or 'NO' or 'N/A':
                    temp_file.write(name + '\n')
                    temp_file.write(rank + '\n')
                    temp_file.write(LD + '\n')
                    temp_file.write(PT + '\n')
                    temp_file.write(f'Aerospace Test:{new}' + '\n')
                    temp_file.write(CD + '\n')
                    temp_file.write(SDA + '\n')
                    temp_file.write(Board + '\n')
                    temp_file.write(Drill + '\n')
                    found = True
                else:
                    found = False
            elif choice == 4:
                print(CD)
                new = input('Enter "YES", "NO", or "N/A: ').upper()
                if new == 'YES' or 'NO' or 'N/A':
                    temp_file.write(name + '\n')
                    temp_file.write(rank + '\n')
                    temp_file.write(LD + '\n')
                    temp_file.write(PT + '\n')
                    temp_file.write(AE + '\n')
                    temp_file.write(f'CD:{new}' + '\n')
                    temp_file.write(SDA + '\n')
                    temp_file.write(Board + '\n')
                    temp_file.write(Drill + '\n')
                    found = True
                else:
                    found = False
            elif choice == 5:
                print(SDA)
                new = input('Enter "YES", "NO", or "N/A: ').upper()
                if new == 'YES' or 'NO' or 'N/A':
                    temp_file.write(name + '\n')
                    temp_file.write(rank + '\n')
                    temp_file.write(LD + '\n')
                    temp_file.write(PT + '\n')
                    temp_file.write(AE + '\n')
                    temp_file.write(CD + '\n')
                    temp_file.write(f'SDA:{new}' + '\n')
                    temp_file.write(Board + '\n')
                    temp_file.write(Drill + '\n')
                    found = True
                else:
                    found = False
            elif choice == 6:
                print(Board)
                new = input('Enter "YES", "NO", or "N/A: ').upper()
                if new == 'YES' or 'NO' or 'N/A':
                    temp_file.write(name + '\n')
                    temp_file.write(rank + '\n')
                    temp_file.write(LD + '\n')
                    temp_file.write(PT + '\n')
                    temp_file.write(AE + '\n')
                    temp_file.write(CD + '\n')
                    temp_file.write(SDA + '\n')
                    temp_file.write(f'Promotion Board:{new}' + '\n')
                    temp_file.write(Drill + '\n')
                    found = True
                else:
                    found = False
            elif choice == 7:
                print(Drill)
                new = input('Enter "YES", "NO", or "N/A: ').upper()
                if new == 'YES' or 'NO' or 'N/A':
                    temp_file.write(name + '\n')
                    temp_file.write(rank + '\n')
                    temp_file.write(LD + '\n')
                    temp_file.write(PT + '\n')
                    temp_file.write(AE + '\n')
                    temp_file.write(CD + '\n')
                    temp_file.write(SDA + '\n')
                    temp_file.write(Board + '\n')
                    temp_file.write(f'Drill:{new}' + '\n')
                    found = True
                else:
                    found = False
# If the name is not found, write everything to the file
        else:
            temp_file.write(cadet + '\n')
            temp_file.write(rank + '\n')
            temp_file.write(LD + '\n')
            temp_file.write(PT + '\n')
            temp_file.write(AE + '\n')
            temp_file.write(CD + '\n')
            temp_file.write(SDA + '\n')
            temp_file.write(Board + '\n')
            temp_file.write(Drill + '\n')
        cadet = file.readline()
    temp_file.close()
    file.close()
# Remove and rename the files
    os.remove('roster.txt')
    os.rename('temp.txt','roster.txt')
    if found:
        print('The file has been updated.')
    else:
        print('The file was not found.')
