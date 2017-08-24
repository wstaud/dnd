"""DnD Pathfinder GUI"""
from Dice import Dice

# Ask user to open ports/sockets to start game
def main_menu():
    print "Welcome to Pathfinder Capstone DM Console\nSelect from the menu below:"
    start_game = raw_input("1: Init Game\n2: Exit Program\n")
    
    if start_game == "1":
        init_game()
        # TODO create sockets
    elif start_game == "2":
        exit()
    else:
        print "Invalid selection, please choose from below"
        main_menu()

# Display connected players and GUI for DM
def init_game():
    # TODO recycle connected players

    # TODO Display GUI choices
    print "Select from the menu below:"
    dm_selection = raw_input("1: Call roll init\n2: Dice Roll Menu\n3: Send instructions\n4: Help Menu\n0: Kill Server\n")

    if dm_selection == "1":
        roll_call()
    elif dm_selection == "2":
        dice_menu()
    elif dm_selection == "3":
        instruction()
    elif dm_selection == "4":
        pass
    elif dm_selection == "0":
        exit()
    else:
        command = dm_selection.split(' ', 1)[0]
        if command == "health":
            pass
        elif command == "kick":
            pass
        elif command == "pm":
            pass
        elif command == "ban":
            pass
        else:
            print "Invalid command, reference menu below and select 4 if additonal commands are needed"
            init_game()



def roll_call():
    pass

# Roll a dice with a specific number of sides
def dice_menu():
    sides = raw_input('Input number of sides or input "menu" to return to menu\n')

    if sides == "menu":
        init_game()
    else:
        rolls = raw_input('Number of rolls? (Default = 1)\n')
        # See if input is a number, throw error and have user try again if not
        try:
            if rolls == '':
                dice = Dice(sides)
            else:
                dice = Dice(sides, rolls)
            roll_result = dice.roll()
        except:
            print "Invalid User Input,\n"
            dice_menu()

        print "Result of {}d{}: {}".format(rolls, sides, roll_result)
        dice_menu()

# Send Players Instructions    
def instruction():
    print "### INSTRUCTION PROMPT ###"
    prompt = raw_input('Enter your instructions, input "menu" to return to main menu\n')
    
    # DO MAGIC

    if prompt == "menu":
        init_game()
    else:
        print "Message sent: {}".format(prompt)
    
    # Repeat instruction
    instruction()




# Open Main Menu on launch
main_menu()
