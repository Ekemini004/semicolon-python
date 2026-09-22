temp_celsius = float(input("Enter a number"))

if(temp_celsius < 273) :

    temp_Farenheit = (temp_celsius * 1.8) + 32

print(temp_Farenheit)

index = 1 

while(index <= 4) :

    temp_celsius = temp_celsius + index
  
    if(temp_celsius < 273) :

        temp_Farenheit = (temp_celsius * 1.8) + 32

    print(temp_Farenheit)

    index = index + 1
        
        


