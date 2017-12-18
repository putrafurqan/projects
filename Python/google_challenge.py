"""
Return doublr numbers
"""

save_list = []
print_list = []
for i in range(10):
    usr_input = input('Enter Number: ')
    if usr_input == 'end':
        break
    if usr_input in save_list:
        print_list.append(usr_input)
    save_list.append(usr_input)
try:
    print(print_list[0])
except IndexError:
    print("None")
