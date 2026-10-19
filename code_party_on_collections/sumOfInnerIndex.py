
numbers =  [ [2, 3, 4], [1, 5, 7], [4, 6, 8] ]

new_numbers = [  ]

def sum_of_inner_list( users_list):

    sum_of_index = 0

    for index in range(0, len(users_list)):

   
        
            for indexTwo in range(0, len(users_list[index])):

                sum_of_index += users_list[indexTwo][index] 
   
                if(indexTwo == len(users_list[index])-1):
                    new_numbers.append(sum_of_index)
                    sum_of_index = 0
                    
               
    return new_numbers


print(sum_of_inner_list(numbers))
