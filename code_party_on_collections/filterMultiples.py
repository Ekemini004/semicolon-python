
numbers = [ number for number in range(1, 51)]

#print(numbers)

def divisible_by_3_5(any_list):
    
    return any_list % 3 == 0 and any_list % 5 == 0


new_list = filter(divisible_by_3_5, numbers)   


print(list(new_list))
