menu = f""" 

 Hey there! WElcome to Nokia 5510.

 ════════════════════════════════
           PHONE MAIN MENU
 ════════════════════════════════

          1. Phone book
          2. Messages
          3. Chats
          4. Call Register 
          5. Tones
          6. Settings                     
          7. Call Divert
          8. Music
          9. Games
          10. Calculator
          11. Reminderscd 
          12. Clock
          13. Profiles
          14. Services
          15. SIM services
          16. Exit


 ════════════════════════════════
please select an option by enetring a number, to proceed.

"""

running = True




def options_menu():

    print("You are now on the Options menu")
    stay_in_optionsMenu = True

    while(stay_in_optionsMenu):

        optionsMenu = """
        You are now on the Message Menu.
        Please enter a number
        to select an option.

        ════════════════════════════════
              OPTIONS MENU
        ════════════════════════════════

              1. Write Messages
              2. Inbox
              3. Received calls
              4. Dialed numbers
              5. Erase recent call list
              10. Back
              0. Home (main menu)

        ════════════════════════════════
        """

        optionsMenuChoice = int(input(f"{optionsMenu}"))

        match optionsMenuChoice:

            case 1:
                print("You are now on the Write messages menu")

            case 2:
                print("You are now on the Inbox menu")

            case 3:
                print("You are now on the Received Calls menu")

            case 4:
                print("You are now on the Dialed numbers menu")

            case 5:
                print("You are now on the Erase recent call lists menu")

            case 10:
                stay_in_optionsMenu = False
                return "back"

            case 0:
                stay_in_optionsMenu = False
                return "stop parent loop"


def show_call_duration_menu():

    stay_in_showCallDuration = True

    while (stay_in_showCallDuration):

        showCallDuration = """
        You are now on the Show call duration Menu.
        Please enter a number
        to select an option.

        ════════════════════════════════
           SHOW CALL DURATION MENU
        ════════════════════════════════

              1. Last Call Duration
              2. All calls Duration
              3. Received calls duration
              4. Dialed calls duration
              5. Clear timers
              10. Back
              0. Home (main menu)

        ════════════════════════════════
        """

        showCallDurationChoice = int(input(f"{showCallDuration}"))

        match showCallDurationChoice:

            case 1:
                print("You are now on the Last Call duration menu")

            case 2:
                print("You are now on all calls duration menu")

            case 3:
                print("You are now on the Received Calls duration menu")

            case 4:
                print("You are now on the Dialed calls duration menu")

            case 5:
                print("You are now on the clear timers menu")

            case 10:
                print("Going back to the previous menu...")
                stay_in_showCallDuration = False
                return "back"

            case 0:
                print("Going back to the main menu...")
                stay_in_showCallDuration = False
                return "stop parent loop"


def show_call_costs_menu():

    stay_in_showCallCosts = True

    while(stay_in_showCallCosts):

        showCallCosts = """
        You are now on the Show call costs Menu.
        Please enter a number
        to select an option.

        ════════════════════════════════
           SHOW CALL COSTS MENU
        ════════════════════════════════

              1. Last Call Cost
              2. All calls Cost
              3. Clear Counter
              10. Back
              0. Home (main menu)

        ════════════════════════════════
        """

        showCallCostChoice = int(input(f"{showCallCosts}"))

        match showCallCostChoice:

            case 1:
                print("You are now on the Last Call cost menu")

            case 2:
                print("You are now on all calls cost menu")

            case 3:
                print("You are now on the clear counters menu")

            case 10:
                print("Going back to the previous menu...")
                stay_in_showCallCosts = False
                return "back"

            case 0:
                print("Going back to the main menu...")
                stay_in_showCallCosts = False
                return "stop parent loop"


def show_call_cost_settings_menu():

    stay_in_showCallCostSettings = True

    while(stay_in_showCallCostSettings):

        showCallCostSettings = """
        You are now on the Show call cost settings Menu.
        Please enter a number
        to select an option.

        ════════════════════════════════
         SHOW CALL COSTS SETTINGS MENU
        ════════════════════════════════

              1. Last Call Cost
              2. All calls Cost
              3. Clear Counters
              10. Back
              0. Home (main menu)

        ════════════════════════════════
        """

        showCallCostSettingsChoice = int(input(f"{showCallCostSettings}"))

        match showCallCostSettingsChoice:

            case 1:
                print("You are now on the Last Call cost limit menu")

            case 2:
                print("You are now on show cost in menu")

            case 10:
                print("going back to previous menu...")
                stay_in_showCallCostSettings = False
                return "back"

            case 0:
                print("Going back to the main menu...")
                stay_in_showCallCostSettings = False
                return "stop parent loop"


def call_settings_menu():

    stay_in_callSettings = True

    while(stay_in_callSettings):

        callSettings = """
        You are now on the Call Settings Menu.
        Please enter a number
        to select an option.

        ════════════════════════════════
              CALL SETTINGS MENU
        ════════════════════════════════

              1. Automatic redial
              2. Speed dialing
              3. Call waiting options
              4. Own number sending
              5. Phone line in use
              6. Automatic answer
              10.Back
              0. Home (main menu)

        ════════════════════════════════
        """

        callSettingsMenuChoice = int(input(f"{callSettings}"))

        match callSettingsMenuChoice:

            case 1:
                print("You are now on the Automatic redial Menu")

            case 2:
                print("You are now on the speed dialing menu")

            case 3:
                print("You are now on the call own number sending menu")

            case 4:
                print("You are now on the phone line in use menu")

            case 6:
                print("You are now on the Keypad tones Menu")

            case 10:
                print("Going back to the previous menu...")
                stay_in_callSettings = False
                return "back"

            case 0:
                print("Going back to the main menu...")
                stay_in_callSettings = False
                return "stop parent loop"


def phone_settings_menu():

    stay_in_phoneSettingsMenu = True

    while(stay_in_phoneSettingsMenu):

        phoneSettingsMenu = """
        You are now on the phone Settings Menu.
        Please enter a number 
        to select an option.

        ════════════════════════════════
              PHONE SETTINGS MENU
        ════════════════════════════════

              1. Language
              2. Cell Info display
              3. Welcome note
              4. Network Selection
              5. Confirm SIM service actions
              10. Back 
              0. Home (main menu)

        ════════════════════════════════
        """

        phoneSettingsMenuChoice = int(input(f"{phoneSettingsMenu}"))

        match phoneSettingsMenuChoice:

            case 1:
                print("You are now on the Language Menu")

            case 2:
                print("You are now on the Cell Info display menu")

            case 3:
                print("You are now on the WElcome note menu")

            case 4:
                print("You are now on the Network selection menu")

            case 6:
                print("You are now on the Confirm sim service actions Menu")

            case 10:
                print("going back to previous menu...")
                stay_in_phoneSettingsMenu = False
                return "back"

            case 0:
                print("going back to main menu...")
                stay_in_phoneSettingsMenu = False
                return "stop parent loop"


def security_settings_menu():

    stay_in_securitySettingsMenu = True

    while(stay_in_securitySettingsMenu):

        securitySettingsMenu = """
        You are now on the security Settings Menu.
        Please enter a number
        to select an option.

        ════════════════════════════════
             SECURITY SETTINGS MENU
        ════════════════════════════════

              1. PINcode request
              2. Call barring service
              3. Fixed dialing
              4. Closed user group
              5. Security level
              6. Change access codes
              10. Back
              0. Home (main menu)

        ════════════════════════════════
        """

        securitySettingsMenuChoice = int(input(f"{securitySettingsMenu}"))

        match securitySettingsMenuChoice:

            case 1:
                print("You are now on the PIN code request Menu")

            case 2:
                print("You are now on the call barring service menu")

            case 3:
                print("You are now on the fixed dialing menu")

            case 4:
                print("You are now on the closed user group menu")

            case 6:
                print("You are now on the security level Menu")

            case 7:
                print("You are now on the change access codes Menu")

            case 10:
                print("Going back to the previous menu...")
                stay_in_securitySettingsMenu = False
                return "back"

            case 0:
                print("Going back to the main menu...")
                stay_in_securitySettingsMenu = False
                return "stop parent loop"



# PARENT MENUS (menus that have children)


def search_menu():

    print("You are now on the search menu")
    stay_in_searchMenu = True

    while(stay_in_searchMenu):

        searchMenu = """
        You are now on the Search Menu.
        Please enter a number
        to select an option.

        ════════════════════════════════
                 SEARCH MENU
        ════════════════════════════════

              1. Find name and do sth
              2. Find number and do something
              10. Back
              0. Home (main menu)

        ════════════════════════════════
        """

        searchMenuChoice = int(input(f"{searchMenu}"))

        match searchMenuChoice:

            case 1:
                print("You are now on the Find name menu")

            case 2:
                print("You are now on the Find number menu")

            case 10:
                print("Going back to the phone book...")
                stay_in_searchMenu = False
                #return "back"

            case 0:
                print("Going back to the main menu...")
                stay_in_searchMenu = False
                return "stop parent loop"


def phone_book_menu():

    stay_in_phoneBookMenu = True

    while(stay_in_phoneBookMenu):

        phoneBookMenu = """ 
        You are now on the phone book
        Menu, please enter a number 
        to select an option.

        ════════════════════════════════
               PHONE BOOK MENU
        ════════════════════════════════

              1. Search
              2. Service Nos.
              3. Add name
              4. Erase
              5. Edit
              6. Copy                     
              7. Assign tone
              8. Send b'card
              9. Options
              10. Back to main menu

        ════════════════════════════════

        """

        phoneBookMenuChoice = int(input(f"{phoneBookMenu}"))

        match phoneBookMenuChoice:

            case 1:
                result = search_menu()
                if result == "stop parent loop":
                    stay_in_phoneBookMenu = False

            case 2:
                print("You are now on the Service Nos menu")

            case 3:
                print("You are now on the Add name menu")

            case 4:
                print("You are now on the Erase menu")

            case 5:
                print("You are now on the Edit menu")

            case 6:
                print("You are now on the Copy menu")

            case 7:
                print("You are now on the Assign tone menu")

            case 8:
                print("You are now on the Send b'card menu")

            case 9:
                result = options_menu()
                if result == "stop parent loop":
                    stay_in_phoneBookMenu = False

            case 10:
                print("Going back to the main menu")
                stay_in_phoneBookMenu = False


def message_menu():

    stay_in_messageMenu = True

    while (stay_in_messageMenu):

        messageMenu = """

        You are now on the Message Menu.
        Please enter a number
        to select an option.

        ════════════════════════════════
              MESSAGE MENU
        ════════════════════════════════

              1. Write Messages
              2. Inbox
              3. Received calls
              4. Dialed numbers
              5. Erase recent call lists
              6. Show call duration
              7. Show call costs
              8. Call cost settings
              9. Prepaid credit
              10. Back(main menu)

        ════════════════════════════════
        """

        messageMenuChoice = int(input(f"{messageMenu}"))

        match messageMenuChoice:

            case 1:
                print("You are now on the Write messages menu")

            case 2:
                print("You are now on the Inbox menu")

            case 3:
                print("You are now on the Received Calls menu")

            case 4:
                print("You are now on the Dialed numbers menu")

            case 5:
                print("You are now on the Erase recent call lists menu")

            case 6:
                result = show_call_duration_menu()
                if result == "stop parent loop":
                    stay_in_messageMenu = False

            case 7:
                result = show_call_costs_menu()
                if result == "stop parent loop":
                    stay_in_messageMenu = False

            case 8:
                result = show_call_cost_settings_menu()
                if result == "stop parent loop":
                    stay_in_messageMenu = False

            case 9:
                print("You are now on Prepaid cost menu")

            case 10:
                print("Going back to the main menu")
                stay_in_messageMenu = False


def settings_menu():

    stay_in_settingsMenu = True

    while(stay_in_settingsMenu):

        settingsMenu = """
        You are now on the Settings Menu.
        Please enter a number
        to select an option.

        ════════════════════════════════
                SETTINGS MENU
        ════════════════════════════════

              1. Call Settings
              2. Phone Settings
              3. Security Settings
              4. Restore factory settings
              10. Back

        ════════════════════════════════
        """

        settingsMenuChoice = int(input(f"{settingsMenu}"))

        match settingsMenuChoice:

            case 1:
                result = call_settings_menu()
                if result == "stop parent loop":
                    stay_in_settingsMenu = False

            case 2:
                result = phone_settings_menu()
                if result == "stop parent loop":
                    stay_in_settingsMenu = False

            case 3:
                result = security_settings_menu()
                if result == "stop parent loop":
                    stay_in_settingsMenu = False

            case 4:
                print("You are now on the Restore Factory Settings menu")

            case 10:
                print("Going back to the main menu")
                stay_in_settingsMenu = False



# menus that have no children, straught up stuff


def call_register_menu():

    stay_in_showCallRegister = True

    while(stay_in_showCallRegister):

        showCallRegister = """
        You are now on the Call Register Menu.
        Please enter a number
        to select an option.

        ════════════════════════════════
            SHOW CALL REGISTER MENU
        ════════════════════════════════

              1. Missed Calls
              10. Back

        ════════════════════════════════
        """

        showCallRegisterChoice = int(input(f"{showCallRegister}"))

        match showCallRegisterChoice:

            case 1:
                print("You are now on the Missed Call menu")

            case 10:
                print("Going back to the main menu")
                stay_in_showCallRegister = False


def tones_menu():

    stay_in_showTonesMenu = True

    while(stay_in_showTonesMenu):

        showTonesMenu = """
        You are now on the Call Register Menu.
        Please enter a number
        to select an option.

        ════════════════════════════════
                SHOW TONES MENU
        ════════════════════════════════

              1. Ringing tone
              2. Ringing volume
              3. Incoming call alert
              4. Message alert tone
              5. Keypad tones
              10. Back

        ════════════════════════════════
        """

        showTonesMenuChoice = int(input(f"{showTonesMenu}"))

        match showTonesMenuChoice:

            case 1:
                print("You are now on the Ringing tone Menu")

            case 2:
                print("You are now on the Ringing volume menu")

            case 3:
                print("You are now on the Incoming call alert menu")

            case 4:
                print("You are now on the Message alert tone menu")

            case 5:
                print("You are now on the Keypad tones menu")

            case 10:
                print("Going back to the main menu")
                stay_in_showTonesMenu = False


def music_menu():

    stay_in_musicMenu = True

    while(stay_in_musicMenu):

        musicMenu = """
        You are now on the Music Settings Menu.
        Please enter a number
        to select an option.

        ════════════════════════════════
             MUSIC SETTINGS MENU
        ════════════════════════════════

              1. Music player
              2. Radio
              3. Recorder
              4. Track list
              10. Back

        ════════════════════════════════
        """

        musicMenuChoice = int(input(f"{musicMenu}"))

        match musicMenuChoice:

            case 1:
                print("You are now on the Music Player Menu")

            case 2:
                print("You are now on the Radio menu")

            case 3:
                print("You are now on the Recorder menu")

            case 4:
                print("You are now on the Track List menu")

            case 10:
                print("Going back to the main menu")
                stay_in_musicMenu = False


def games_menu():

    print("You are now on the Games Menu")
    stay_in_gamesMenu = True

    while(stay_in_gamesMenu):

        gamesMenu = """
        You are now on the Games Menu.
        Please enter a number to select an option

        ════════════════════════════════
             GAMES MENU
        ════════════════════════════════

              1. Main Menu
              10. Back(previous menu)

        ════════════════════════════════
        """

        gamesMenuChoice = int(input(f"{gamesMenu}"))

        match gamesMenuChoice:

            case 1:
                print("Going back to the Main menu")
                #stay_in_gamesMenu = False

            case 10:
                print("Going back to the previous menu")
                stay_in_gamesMenu = False


def print_calculator_menu():

    print("You are now on the Calculator")
    stay_in_calculatorMenu = True

    while(stay_in_calculatorMenu):

        calculatorMenu = """
        You are now on the calculator Menu.
        Please enter a number to select an option

        ════════════════════════════════
             CALCULATOR MENU
        ════════════════════════════════

              1. Back to Main Menu


        ════════════════════════════════
        """

        calculatorMenuChoice = int(input(f"{calculatorMenu}"))

        match calculatorMenuChoice:

            case 1:
                print("Going back to the Main menu...")
                stay_in_calculatorMenu = False


def clock_menu():

    stayinClockMenu = True

    while(stayinClockMenu):

        clockMenu = """
        You are now on the Music Settings Menu.
        Please enter a number
        to select an option.

        ════════════════════════════════
             CLOCK SETTINGS MENU
        ════════════════════════════════

              1. Alarm Clock
              2. Clock Settings
              3. Date Settings
              4. Stop watch
              5. Countdown Timer
              6. Auto update of date and time
              10. Back(to main menu)

        ════════════════════════════════
        """

        clockMenuChoice = int(input(f"{clockMenu} "))

        match clockMenuChoice:

            case 1:
                print("You are now on the Alarm Clock Menu")

            case 2:
                print("You are now on the Clock settings menu")

            case 3:
                print("You are now on the Date Settings menu")

            case 4:
                print("You are now on the Stopwatch menu")

            case 5:
                print("You are now on the Countdown timer menu")

            case 6:
                print("You are now on the Auto update of date and time menu")

            case 10:
                stayinClockMenu = False



#main menu, that has all the cases involved 
# so after any menu closes, this loop shows the main menu again.


while (running):

    user_choice = int(input(f"{menu}"))

    match user_choice:

        case 1:
            phone_book_menu()

        case 2:
            message_menu()

        case 3:
            print("You are now on the Chat menu")

        case 4:
            call_register_menu()

        case 5:
            tones_menu()

        case 6:
            settings_menu()

        case 7:
            print("You are now on the Call Divert menu")

        case 8:
            music_menu()

        case 9:
            games_menu()

        case 10:
            print_calculator_menu()

        case 11:
            print("You are now on the Reminders")

        case 12:
            clock_menu()

        case 13:
            print("You are now on the Profiles Menu")

        case 14:
            print("You are now on the Services Menu")

        case 15:
            print("You are now on the Sim Services Menu")

        case 16:
            print("Exiting Nokia...")
            running = False
