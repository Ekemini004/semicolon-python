words =  ['cat','elephant', 'tiger', 'lion']

def longer_than_five(any_list):

    new_words = [ item for item in any_list if len(item) > 5]

    return new_words





print(longer_than_five(words))
