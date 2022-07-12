""" Prompt user for name, display user's name """
# name = input("Enter Name: ")

""" Prompt user for name, display “Hello [user]” """
# name = input("Enter Name: ")
# print("Hello", name)

""" Prompt user for first and last name, display user's full name in order of first, last """
# first_name = input("Enter First Name: ")
# last_name = input("Enter Last Name: ")
# print(first_name + last_name)
# print(first_name + " " + last_name)

""" Prompt user for first and last name, display user's full name in order of last, first """
# first_name = input("Enter First Name: ")
# last_name = input("Enter Last Name: ")
# print(last_name + " " + first_name)
# print(last_name + ", " + first_name)

""" Prompt user for first and last name, display “Goodbye, [first] [last]” """
# first_name = input("Enter First Name: ")
# last_name = input("Enter Last Name: ")
# # print(last_name + " " + first_name)
# print("Goodbye, " + first_name + " " + last_name)

""" Prompt user for pet's name, display pet's name, prompt user for pet's species, display “My [pet species]'s name is [pet name]” """
# pet_name = input("Enter Pet's Name: ")
# pet_species = input("Enter Pet's Species: ")
# print("My " + pet_species + "'s name is, " + pet_name)

""" Prompt user for pet's name and age in years, display “My pet's name is, [pet name] they are [age] years old” """
# pet_name = input("Enter Pet's Name: ")
# pet_age = input("Enter Pet's Age (In Years): ")
# print("My pet's name is, " + pet_name + " they are " + pet_age + " years old")



""" Math """
""" Prompt user for 2 numbers, display each number """
# num1 = input("Enter A Number: ")
# num2 = input("Enter Another Number: ")
# print(num1)
# print(num2)

""" Prompt user for 2 numbers, display sum of each number """
""" Result should be [val1][val2], this is introduction to variable types """
# num1 = input("Enter A Number: ")
# num2 = input("Enter Another Number: ")
# print(num1 + num2)
# print(int(num1 + num2))
# print(int(num1) + int(num2))

""" Prompt user for 2 numbers, display values subtracted """
# num1 = input("Enter A Number: ")
# num2 = input("Enter Another Number: ")
# print(int(num1) - int(num2))

""" Prompt user for 2 numbers, display values multiplied """
# num1 = input("Enter A Number: ")
# num2 = input("Enter Another Number: ")
# print(int(num1) * int(num2))

""" Prompt user for 2 numbers, display values divided """
# num1 = input("Enter A Number: ")
# num2 = input("Enter Another Number: ")
# print(int(num1) / int(num2))

""" Prompt user for a number, display value raised to the power of 2 """
# num = input("Enter A Number: ")
# print(int(num) * int(num))
# print(pow(int(num), 2))

""" Prompt user for 2 numbers, display “[val1] + [val2] = [sum]” """
# num1 = input("Enter A Number: ")
# num2 = input("Enter Another Number: ")
# # sum = int(num1) + int(num2)
# # print(num1 + " + " + num2 + " = " + str(sum))
# # total = int(num1) + int(num2)
# # print(num1 + " + " + num2 + " = " + str(total))
# print(num1 + " + " + num2 + " = " + str(int(num1) + int(num2)))

""" Prompt user for random word, display word 5 times back to back """
# word = input("Enter Word: ")
# print(word + word + word + word + word)
# i = 0
# while i < 5:
#   print(word)
#   print(word, end='')
#   i += 1
# print("")
# print(word*5)

""" Prompt user for how long it takes them to get ready in the morning in minutes, display how long it takes them to get ready in seconds """
# minutes = input("Enter How Long It Takes To Get Ready In The Morning (In Minutes): ")
# seconds = int(minutes) * 60
# print("It Takes You: " + str(seconds) + " Seconds To Get Ready In The Morning")
# print("It Takes You: " + str(int(minutes) * 60) + " Seconds To Get Ready In The Morning")

""" Prompt user for how long it takes them to get ready in the morning in minutes, display how long it takes them to get ready in hours """
# minutes = input("Enter How Long It Takes To Get Ready In The Morning (In Minutes): ")
# hours = int(minutes) / 60
# print("It Takes You: " + str(hours) + " hour(s) To Get Ready In The Morning")
# print("It Takes You: " + str(int(minutes) / 60) + " hour(s) To Get Ready In The Morning")

""" Challenge: """
# import math

# minutes = input("Enter How Long It Takes To Get Ready In The Morning (In Minutes): ")
# hours = int(minutes) / 60
# # print("It Takes You: " + str(round(hours, 2)) + " hour(s) To Get Ready In The Morning")
# print("It Takes You: " + str(hours - (hours % .01)) + " hour(s) To Get Ready In The Morning")

""" Prompt user for a number, display if the value is less than 100 """
# num = input("Enter A Number: ")
# if int(num) < 100:
#   print("Number Less Than 100")


######################################################################################################################################################
# https://www.w3resource.com/python-exercises/python-basic-exercises.php #
######################################################################################################################################################

######################################################################################################################################################
# Python basic (Part -I) [150 exercises with solution] #
######################################################################################################################################################
"""
1. Write a Python program to print the following string in a specific format (see the output). Go to the editor
Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are" Output :

Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are
"""
# print(
#   """
#   Twinkle, twinkle, little star,
#     How I wonder what you are!
#       Up above the world so high,
#       Like a diamond in the sky.
#   Twinkle, twinkle, little star,
#     How I wonder what you are
#   """
# )
# print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are")

# space = 0
# word = "Twinkle, twinkle, little star,"
# print((" "*space) + word)
# space = 4
# word = "How I wonder what you are!"
# print((" "*space) + word)
# space = 8
# word = "Up above the world so high,"
# print((" "*space) + word)
# word = "Like a diamond in the sky."
# print((" "*space) + word)
# space = 0
# word = "Twinkle, twinkle, little star,"
# print((" "*space) + word)
# space = 4
# word = "How I wonder what you are"
# print((" "*space) + word)

"""
2. Write a Python program to get the Python version you are using
"""
# import sys, platform

# print(sys.version)
# print(sys.version_info)
# print(platform.python_version())
# print(platform.python_version_tuple())
# print("Your Python Version Is: " + platform.python_version())

"""
3. Write a Python program to display the current date and time.
Sample Output :
Current date and time :
2014-07-05 14:34:14
"""
# import datetime

# print(datetime.datetime.now().strftime("%m/%d/%Y"))

"""
4. Write a Python program which accepts the radius of a circle from the user and compute the area.
Sample Output :
r = 1.1
Area = 3.8013271108436504
"""
import math

radius = input("Enter Radius: ")
print("Area is: " + str(math.pi * pow(int(radius), 2)))
