user_name = input("Enter your name\n")

product_name = input("enter a product name\n")

product_quantity = int(input("enter quantity of" + " " + product_name +  "\n"))

product_price = int(input("enter price of" + " " + product_name +  "\n"))

user_option = input("add another product, enter yes or no\n")

product_price_sum = 0 + (product_price * product_quantity)

while(user_option == "yes") :
        
        product_name = input("enter a product name\n")

        product_quantity = int(input("enter quantity of" + " " + product_name +  "\n"))

        product_price = int(input("enter price of " + product_name + "\n"))

        user_option = input("add another product, enter yes or no\n")

        product_priceSum = product_price_sum + (product_price * product_quantity)


print("Hi"+ " " + user_name + " " + "your total bill is ", product_priceSum)



