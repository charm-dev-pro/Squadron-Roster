# Program: Civil Air Patrol Cadet Roster

# Import modules
import add_cadet
import CheckProgress
import RemoveCadet
import PrintRoster
import SignOffRequirements
import CadetRank

# Option assignments
Add_cadet = 1
Remove_cadet = 2
Check_Progress = 3
Sign_Off_requirements = 4
Cadet_rank = 5
Print_Roster = 6
Quit_Choice = 7

# Display menu function
def menu():
    print('             MENU')
    print('1) Add a cadet to the roster')
    print('2) Remove a cadet from the roster')
    print('3) Check the progress of a cadet')
    print('4) Sign off on promotion requirements')
    print("5) Change a cadet's rank")
    print('6) Print the cadet roster')
    print('7) Quit')


# Create the main function
def main():
        choice = 0
# Keep track of possible user errors
# Go through the menu options and perform the options
        try:
            while choice != Quit_Choice:
                menu()
                choice = int(input('Enter your choice: '))
                if choice == Add_cadet:
                    print('Cadet has been added to the roster',add_cadet.add_cadet())
                elif choice == Remove_cadet:
                    RemoveCadet.remove()
                elif choice == Check_Progress:
                    CheckProgress.check_progress()
                elif choice == Sign_Off_requirements:
                    SignOffRequirements.sign_off()
                elif choice == Cadet_rank:
                    CadetRank.change_rank()
                elif choice == Print_Roster:
                    PrintRoster.print_roster()
                elif choice == Quit_Choice:
                    print('Quiting the program...')
                    print('Program quit.')
                else:
                    print('Error: Invalid selection.')
        except ValueError:
            print('ERROR: Choice entered was not a number, or was not one of the number choices.')
        except:
            print('ERROR: An error has occurred')
# Call the main function
main()