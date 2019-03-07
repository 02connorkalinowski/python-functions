# 4.13.3: Greetings
# Connor
#2.5.19

name = input("What is your name:  ")

def greeting():
    print ("Hi there " + name + "!")
    print("Nice to meet you")

greeting()


#4.13.4: Functions and Variables
# Connor
#2.11.19

x = 10

def print_something():
    x = 3
    print('\r\n', x)

print('\r\n', x)
print_something()





# 4.13.6: Functions and variable, Part 3
# Connor
#2.18.19

def print_number(x):
	print('\n', x)

print_number(13)
print_number(23)


# 4.14.4: Name and Age
# Connor
# 2.18.19

def name_and_age(name, age):
	print('Hi, my name is', name, 'and i am', age, 'years old!')

name_and_age('Mike', 33)
name_and_age('Zane', 18)

# 4.14.5: Default Parameter Values
# Connor
# 2.19.19

def print_two_numbers(x, y = 20):
	print('First number: ', x)
	print('Second number: ' + str(y))


print_two_numbers(34, 45)
print_two_numbers(78)


# 4.14.6: Print sum
# Connor
# 2.19.19

def print_sum(x, y):
	print(x + y)

print_sum(48, 2345)



# 4.14.7: Print Multiple Times
# Connor
# 2.19.19

def print_multiple_times(string, times):
	for i in range(times):
		print(string)


print_multiple_times('Hey there Computer Scientist' ,10)



# 4.14.4: Name and Age
# Connor
# 2.18.19

def name_and_age(name, age):
	print('Hi, my name is', name, 'and i am', age, 'years old!')

name_and_age('Mike', 33)
name_and_age('Zane', 18)



# 4.14.5: Default Parameter values
# Connor
# 2.19.19

def print_two_numbers(x, y = 20):
	print('First number: ', x)
	print('Second number: ' + str(y))


# 4.16.4: Enter Name & Age using the Try & Except Rule
# Connor
# 2.20.19

# name = input('Enter your name: ')
#
# age = -1
#
# try:
# 	age = int(input('Enter your age: '))
# except ValueError:
# 	print('\n''That was not an Integer for your age')
#
# print('Name: ', name)
# print('Age:', age)