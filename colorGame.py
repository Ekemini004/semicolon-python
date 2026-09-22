favorite_color = "blue"

index = 1

while(index <= 3) :

    user_color = input(("enter a color\n"))

    if(user_color == favorite_color) :

        print("correct")

        break

    elif (user_color == "green") :

        print("close!")

    else:

      print("wrong!")
        
      index = index + 1

    if (index > 3) :

        print("Your 3 tries are used up!")
