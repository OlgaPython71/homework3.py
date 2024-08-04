calls = 0
def string_info(string):
    global calls
    calls += 1
    return (len(string), string.upper(), string.lower())

def is_contains(string, list_to_search):
    global calls
    calls += 1
    new_string = string.lower()
    new_list_to_search = [i.lower() for i in list_to_search]
    return new_string in new_list_to_search



print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
