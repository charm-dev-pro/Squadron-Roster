# Import os to rename and remove the files
import os

# Function the prints the rank options
def ranks():
    print('0) Cadet')
    print('1) C/Amn')
    print('2) C/A1C')
    print('3) C/SrA')
    print('4) C/SSgt')
    print('5) C/TSgt')
    print('6) C/MSgt')
    print('7) C/SMSgt')
    print('8) C/CMSgt')
    print('9) C/2d Lt.')
    print('10) C/1st Lt.')
    print('11) C/Capt.')
    print('12) C/Maj.')
    print('13) C/Lt. Col.')
    print('14) C/Col.')


# Function that changes a cadet's rank
def change_rank():
    global new
    found = False
# Search for the cadet
    cadet_first = input('Enter the first name of a cadet: ').upper()
    cadet_last = input('Enter the last name of a cadet: ').upper()
    name = cadet_last + ',' + cadet_first
    file = open('roster.txt', 'r')
    temp_file = open('temp.txt', 'w')
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
# If the name is found change the rank
        if cadet == name:
            print(rank)
            ranks()
            cadet_rank = int(input("Enter an option for the cadet's rank: "))
            if cadet_rank == 0 or 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10 or 11 or 12 or 13 or 14:
                if cadet_rank == 0:
                    new = 'Cadet'
                elif cadet_rank == 1:
                    new = 'C/Amn'
                elif cadet_rank == 2:
                    new = 'C/A1C'
                elif cadet_rank == 3:
                    new = 'C/SrA'
                elif cadet_rank == 4:
                    new = 'C/SSgt'
                elif cadet_rank == 5:
                    new = 'C/TSgt'
                elif cadet_rank == 6:
                    new = 'C/MSgt'
                elif cadet_rank == 7:
                    new = 'C/SMSgt'
                elif cadet_rank == 8:
                    new = 'C/CMSgt'
                elif cadet_rank == 9:
                    new = 'C/2d Lt.'
                elif cadet_rank == 10:
                    new = 'C/1st Lt.'
                elif cadet_rank == 11:
                    new = 'C/Capt.'
                elif cadet_rank == 12:
                    new = 'C/Maj.'
                elif cadet_rank == 13:
                    new = 'C/Lt. Col.'
                elif cadet_rank == 14:
                    new = 'C/Col.'
                temp_file.write(name + '\n')
                temp_file.write(new + '\n')
                temp_file.write(LD + '\n')
                temp_file.write(PT + '\n')
                temp_file.write(AE + '\n')
                temp_file.write(CD + '\n')
                temp_file.write(SDA + '\n')
                temp_file.write(Board + '\n')
                temp_file.write(Drill + '\n')
                found = True
            else:
                found = False
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
# Rename and remove the file
    os.remove('roster.txt')
    os.rename('temp.txt', 'roster.txt')
    if found:
        print('Record has been updated')
    else:
        print('Record could not be found')

