calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    length = len(string)
    upper_string = string.upper()
    lower_string = string.lower()
    return (length, upper_string, lower_string)

def is_contains(string, list_to_search):
    count_calls()
    search_string = string.lower()
    for item in list_to_search:
        if search_string == item.lower():
            return True
    return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)