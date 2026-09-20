menu = f""" 

 Hey there! WElcome to Nokia 5510.

 ════════════════════════════════
           📱 PHONE MENU
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


 ════════════════════════════════
please select an option by enetring a number, to proceed.

"""

user_choice = int(input(f"{menu}"))

match user_choice :

    case 1: 
      
            phoneBookMenu = """ 
                You are now on the phone book
                Menu, please enter a number 
                to select an option.

                ════════════════════════════════
                       📱 PHONE BOOK MENU
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

                ════════════════════════════════

                    """

            phoneBookMenuChoice = int(input(f"{phoneBookMenu}"))


    case 2:
        print("Tuesday")

    case 3:
        print("Wednesday")

    case 4:
        print("Thursday")

    case 5:
        print("Friday")

    case 6:
        print("Saturday")

    case 7:
        print("Sunday")

    case 0:
        print("Not a valid day of the week, dont stress me!")

