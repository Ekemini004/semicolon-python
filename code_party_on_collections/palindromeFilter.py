
words = [ 'level','world', 'madam', 'python']

#print(numbers)

def is_palindrome(any_list):
    
    return any_list[0] == any_list[len(any_list)-1]


new_list = filter(is_palindrome, words)   


print(list(new_list))
