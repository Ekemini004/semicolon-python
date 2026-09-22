running = True

while running:

    menu = f""" 

     Hey there! WElcome to Nokia 5510.

     ════════════════════════════════
               PHONE MENU
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
              11. Reminders
              12. Clock
              13. Profiles
              14. Services
              15. SIM services
              16. Exit


     ════════════════════════════════
    please select an option by enetring a number, to proceed.

    """

    user_choice = int(input(f"{menu}"))

    match user_choice:

        case 1: 
          
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
                  10. Back

            ════════════════════════════════

                """

            stayinPhonebook = True

            while stayinPhonebook:

                phoneBookMenuChoice = int(input(f"{phoneBookMenu}")) 

                match phoneBookMenuChoice:

                    case 1: 
                        print("You are now on the search menu")

                    case 2:
                        print("You are now on the Service Nos menu")

                    case 3:
                        print("You are now on the Add name  menu")

                    case 4:
                        print("You are now on the Erase menu")

                    case 5:
                        print("You are now on the Copy menu")

                    case 6:
                        print("You are now on the Assign tone menu")

                    case 7:
                        print("You are now on the Send b'card menu")

                    case 8:
                        print("You are now on the Options menu")

                    case 10:
                        stayinPhonebook = False


        case 2:

            stayinMessageMenu = True

            while stayinMessageMenu:

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
                          10. Back

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


                    case 7:

                        showCallCosts = """
                            You are now on the Show call duration Menu.
                            Please enter a number
                            to select an option.

                            ════════════════════════════════
                               SHOW CALL COSTS MENU
                            ════════════════════════════════

                                  1. Last Call Cost
                                  2. All calls Cost
                                  3. Clear Counters

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


                    case 8:

                        showCallCostSettings = """
                            You are now on the Show call duration Menu.
                            Please enter a number
                            to select an option.

                            ════════════════════════════════
                             SHOW CALL COSTS SETTINGS MENU
                            ════════════════════════════════

                                  1. Last Call Cost
                                  2. All calls Cost
                                  3. Clear Counters

                            ════════════════════════════════
                        """

                        showCallCostSettingsChoice = int(input(f"{showCallCostSettings}"))

                        match showCallCostSettingsChoice:

                            case 1:
                                print("You are now on the Last Call cost limit menu")

                            case 2:
                                print("You are now on show cost in menu")


                    case 9:
                        print("You are now on Prepaid cost menu")

                    case 10:
                        stayinMessageMenu = False


        case 3:

            stayinChatMenu = True

            while stayinChatMenu:

                print("You are now on the Chat menu")

                print("To go back, press 10")

                chatMenuChoice = int(input())

                match chatMenuChoice:

                    case 10:
                        stayinChatMenu = False


        case 4:

            stayinCallRegister = True

            while stayinCallRegister:

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
                        stayinCallRegister = False


        case 5:

            stayinTonesMenu = True

            while stayinTonesMenu:

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

                    case 6:
                        print("You are now on the Keypad tones menu")

                    case 7:
                        print("You are now on the Vibrating alert menu")

                    case 8:
                        print("You are now on the Screen saver menu")

                    case 10:
                        stayinTonesMenu = False


        case 6:

            stayinSettingsMenu = True

            while stayinSettingsMenu:

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


                    case 2:

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

                        ════════════════════════════════
                    """

                        phoneSettingsMenuChoice = int(input(f"{phoneSettingsMenu}"))

                        match phoneSettingsMenuChoice:

                            case 1:
                                print("You are now on the Language Menu")

                            case 2:
                                print("You are now on the Cell Info display menu")

                            case 3:
                                print("You are now on the WElcome note  menu")

                            case 4:
                                print("You are now on the Network selection  menu")

                            case 6:
                                print("You are now on the Confirm sim service actions Menu")


                    case 3:

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

                        ════════════════════════════════
                    """

                        securitySettingsMenuChoice = int(input(f"{securitySettingsMenu}"))

                        match securitySettingsMenuChoice:

                            case 1:
                                print("You are now on the PIN code request Menu")

                            case 2:
                                print("You are now on the call barring service menu")

                            case 3:
                                print("You are now on the fixed dialing  menu")

                            case 4:
                                print("You are now on the closed user group menu")

                            case 6:
                                print("You are now on the security level Menu")

                            case 7:
                                print("You are now on the change access codes Menu")


                    case 4:
                        print("You are now on the Restore Factory Settings menu")

                    case 10:
                        stayinSettingsMenu = False


        case 7:

            stayinCallDivertMenu = True

            while stayinCallDivertMenu:

                print("You are now on the Call Divert menu")

                print("To go back, press 10")

                callDivertChoice = int(input())

                match callDivertChoice:

                    case 10:
                        stayinCallDivertMenu = False


        case 8:

            stayinMusicMenu = True

            while stayinMusicMenu:

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
                        print("You are now on the Recorder  menu")

                    case 4:
                        print("You are now on the Track List  menu")

                    case 10:
                        stayinMusicMenu = False


        case 9:

            stayinGamesMenu = True

            while stayinGamesMenu:

                print("You are now on the Games")

                print("To go back, press 10")

                gamesMenuChoice = int(input())

                match gamesMenuChoice:

                    case 10:
                        stayinGamesMenu = False


        case 10:

            stayinCalculatorMenu = True

            while stayinCalculatorMenu:

                print("You are now on the Calculator")

                print("To go back, press 10")

                calculatorMenuChoice = int(input())

                match calculatorMenuChoice:

                    case 10:
                        stayinCalculatorMenu = False


        case 11:

            stayinRemindersMenu = True

            while stayinRemindersMenu:

                print("You are now on the Reminders")

                print("To go back, press 10")

                remindersMenuChoice = int(input())

                match remindersMenuChoice:

                    case 10:
                        stayinRemindersMenu = False


        case 12:

            stayinClockMenu = True

            while stayinClockMenu:

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
                      10. Back

                ════════════════════════════════
            """

                clockMenuChoice = int(input(f"{clockMenu}"))

                match clockMenuChoice:

                    case 1:
                        print("You are now on the Alarm Clock Menu")

                    case 2:
                        print("You are now on the Clock settings menu")

                    case 3:
                        print("You are now on the Date Settings  menu")

                    case 4:
                        print("You are now on the Stopwatch menu")

                    case 5:
                        print("You are now on the Countdown timer menu")

                    case 6:
                        print("You are now on the Auto update of date and time menu")

                    case 10:
                        stayinClockMenu = False


        case 13:

            stayinProfilesMenu = True

            while stayinProfilesMenu:

                print("You are now on the Profiles Menu")

                print("To go back, press 10")

                profilesMenuChoice = int(input())

                match profilesMenuChoice:

                    case 10:
                        stayinProfilesMenu = False


        case 14:

            stayinServicesMenu = True

            while stayinServicesMenu:

                print("You are now on the Services Menu")

                print("To go back, press 10")

                servicesMenuChoice = int(input())

                match servicesMenuChoice:

                    case 10:
                        stayinServicesMenu = False


        case 15:

            stayinSimServicesMenu = True

            while stayinSimServicesMenu:

                print("You are now on the Sim Services Menu")

                print("To go back, press 10")

                simServicesMenuChoice = int(input())

                match simServicesMenuChoice:

                    case 10:
                        stayinSimServicesMenu = False


        case 16:
            running = False
