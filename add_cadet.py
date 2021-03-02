# Function that prints the options for rank assignments
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

# Function that adds a cadet to the roster
def add_cadet():
    while True:
        found = False
        global rank
        cadet_roster = open('roster.txt','a')
# Enter the name of the cadet
        print('Enter the following data ')
        cadet_first_name = input("Enter the cadet's first name: ").upper()
        rent = input("Re-enter the cadet's first name: ").upper()
        if rent != cadet_first_name:
            found = True
        else:
            cadet_last_name = input("Enter the cadet's last name: ").upper()
            rent2 = input("Re-enter the cadet's last name: ").upper()
            if rent2 != cadet_last_name:
                found = True
            else:
# Enter the information for the cadet's promotion status
                cadet_name = cadet_last_name + ',' + cadet_first_name
                ranks()
                cadet_rank = int(input("Enter an option for the cadet's rank: "))
                if cadet_rank == 0:
                    rank = 'Cadet'
                elif cadet_rank == 1:
                    rank = 'C/Amn'
                elif cadet_rank == 2:
                    rank = 'C/A1C'
                elif cadet_rank == 3:
                    rank = 'C/SrA'
                elif cadet_rank == 4:
                    rank = 'C/SSgt'
                elif cadet_rank == 5:
                    rank = 'C/TSgt'
                elif cadet_rank == 6:
                    rank = 'C/MSgt'
                elif cadet_rank == 7:
                    rank = 'C/SMSgt'
                elif cadet_rank == 8:
                    rank = 'C/CMSgt'
                elif cadet_rank == 9:
                    rank = 'C/2d Lt.'
                elif cadet_rank == 10:
                    rank = 'C/1st Lt.'
                elif cadet_rank == 11:
                    rank = 'C/Capt.'
                elif cadet_rank == 12:
                    rank = 'C/Maj.'
                elif cadet_rank == 13:
                    rank = 'C/Lt. Col.'
                elif cadet_rank == 14:
                    rank = 'C/Col.'
                print("Enter 'YES','NO, or 'N/A' for whether or not it is completed")
                LD = input("Leadership Test: ").upper()
                PT = input("PT: ").upper()
                AE = input("Aerospace Test: ").upper()
                CD = input("Character Development: ").upper()
                SDA = input("SDA: ").upper()
                BOARD = input("Promotion Board: ").upper()
                DRILL = input('Drill Test: ').upper()
# Write the information to the roster
                cadet_roster.write(cadet_name + '\n')
                cadet_roster.write(rank + '\n')
                cadet_roster.write("Leadership:")
                cadet_roster.write(LD + '\n')
                cadet_roster.write("PT:")
                cadet_roster.write(PT + '\n')
                cadet_roster.write("Aerospace:")
                cadet_roster.write(AE + '\n')
                cadet_roster.write("CD:")
                cadet_roster.write( CD + '\n')
                cadet_roster.write("SDA:")
                cadet_roster.write(SDA + '\n')
                cadet_roster.write("Promotion Board:")
                cadet_roster.write(BOARD + '\n')
                cadet_roster.write('Drill:')
                cadet_roster.write(DRILL + '\n')
        if not found:
            return cadet_name
