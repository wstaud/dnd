"""DnD Pathfinder GUI"""
import random

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

def dice_menu():
    dice = raw_input('Select Dice:\nd4\nd6\nd8\nd10\nd12\nd20\nor input "menu" to return to menu\n')
    print dice
    if dice == "d4":
        print "Result: {}".format(random.randint(1, 4)) 
        init_game()
    elif dice == "d6":
        print "Result: {}".format(random.randint(1, 6))   
        init_game() 
    elif dice == "d8":
        print "Result: {}".format(random.randint(1, 8)) 
        init_game()
    elif dice == "d10":
        print "Result: {}".format(random.randint(1, 10)) 
        init_game()
    elif dice == "d12":
        print "Result: {}".format(random.randint(1, 12)) 
        init_game()
    elif dice == "d20":
        print "Result: {}".format(random.randint(1, 20))
        init_game()
    elif dice == "menu":
        init_game() 

    else:
        print "Invalid selection, reference menu below\n"
        dice_menu()





def instruction():
    print "### INSTRUCTION PROMPT ###"
    prompt = raw_input('Enter your instructions, input "exit" to return to main menu\n')
    
    # DO MAGIC

    if prompt == "exit":
        init_game()
    else:
        print "Message sent: {}".format(prompt)
    instruction()




# Open Main Menu on launch
main_menu()
