"""DnD Pathfinder GUI"""
from Dice import Dice

### Ask user to open ports/sockets to start game
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

### Open sockets and start server... Display connected players and GUI for DM
def init_game():
    # TODO recycle connected players
    print ("\n\n***Player Information Example***\n"
           "player 1 | H:20/25 | Sp:N/A |\n"
           "player 2 | H:30/30 | Sp:5/5 |\n"
           "player 3 | H:20/20 | Sp:N/A |\n")

    # TODO Display GUI choices
    print ("\n\n###### Main Menu ######\n"
           "Select from the menu below:"
          )
    dm_selection = raw_input("1: Call roll init\n2: Dice Roll Menu\n3: Send instructions\n4: Help Menu\n0: Kill Server\n")

    if dm_selection == "1":
        roll_call()
    elif dm_selection == "2":
        dice_menu()
    elif dm_selection == "3":
        instruction()
    elif dm_selection == "4":
        help_menu()
    elif dm_selection == "0":
        #kill server
        print "Killing server...\n"

        #server killed
        print "Server killed. Exiting!"
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

### Init roll call to all players
def roll_call():
    print "This is a roll call"
    init_game()

### Roll a dice with a specific number of sides
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

### Send Players Instructions    
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

### Command Help Menu
def help_menu():
    print ("\n\n ====== Help Menu ======\n"
           "Please select a command to learn more about it, type menu to return to menu.\n"
           "1: health\n"
           "2: kick\n"
           "3: ban\n"
           "4: PM\n"
           )
    prompt = raw_input()

    if prompt == "1":
        print ("\n\nBelow is an example of the health removal command:\n"
               "health playerName mod ##  | Ex: health player1 remove 5\n"
               "Additional mod arguments:\n"
               "add 5 (add 5 health)\n"
               "fill (fill health)\n"
               "ko (bring to zero)\n"
               "kill (bring to death value)\n"
              )
        init_game()
    elif prompt == "2":
        print ("\n\nBelow is an example of the kick player command:\n"
               "kick player2 (kicks player 2 from the game)\n"
              )
        init_game()
    elif prompt == "3":
        print ("\n\nBelow is an example of the ban player command:\n"
               "ban player3 (bans player 3 from the server)\n"
              )
        init_game()
    elif prompt == "4":
        print ("\n\nBelow is an example of the PM player command:\n"
               "pm player1 (inits personal message with player 1)\n"
               "Message: hello player 1! (sends 'hello player 1' to player1)"
              )
        init_game()
    else:
        print "Invalid command, try again or type 'menu' to return to menu"
        help_menu()
             




### Open Main Menu on launch
main_menu()
