# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

age = 37
name = 'Brad'
# Concatenate
# print('Hello I am ' + name + ' and I am ' + str(age))

# String Formatting

# Arguments by position
# print('{}, {}, {}'.format('a', 'b', 'c'))
# print('{1}, {2}, {0}'.format('a', 'b', 'c'))

# Arguments by name
# print('My name is {name} and I am {age}'.format(name=name, age=age))

# F-Strings (only in 3.6+)
print(f'My name is {name} and I am {age}')

# String Methods
