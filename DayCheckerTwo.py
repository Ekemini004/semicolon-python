num_1 = int(input("enter a number"))

num_2 = int(input("enter a second number"))

num_3= int(input("enter a third number"))

num_4 = int(input("enter a fourth number"))

tempoHold = 0

   if(num_1 > num_2) :
        tempoHold = num1
        num_2 = num_1
        num_1 = tempoHold

    if(num_2 > num_3)
        tempoHold = num2
        num_2 = num_3
        num_3 = tempoHold

    if(num_3 > num_4)
        tempoHold = num3
        num_3 = num_4
        num_4 = tempoHold

    print (num_1, num_2, num_3, num_4)

