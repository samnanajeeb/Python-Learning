print("Hello")
print('Hello')

#Assigning string to Variables
text_example = "Hello"
print(text_example)

#You can assign a multiline string to a variable by using three quotes:
a2 = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a2)


#three single quotes:
a3 = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a3)

#Slicing
#Get the characters from position 2 to position 5 (not included):
b1 = "Hello, World!"
print(b1[2:5])

#Slice From the Start
#Get the characters from the start to position 5 (not included):
b2 = "Hello, World!"
print(b2[:5])

#Python Modify String
#The upper() method returns the string in upper case
a4 = "Hello, World!"
print(a4.upper())

#The lower() method returns the string in lower case:
a5 = "Hello, World!"
print(a5.lower())

#Remove Whitespace
#Whitespace is the space before and/or after the actual text, and very often you want to remove this space.
#The strip() method removes any whitespace from the beginning or the end:

a6 = " Hello, World! "
print(a6.strip()) # returns "Hello, World!"

#Replace String
# The replace() method replaces a string with another string:
replace_example = "Hello, World!"
print(replace_example.replace("H", "J"))

#Split String
#The split() method splits the string into substrings if it finds instances of the separator:
a7new = "Hello, World!"
print(a7new.split(",")) 
# returns ['Hello', ' World!']

#String Concatenation
#To concatenate, or combine, two strings you can use the + operator
a = "Hello"
b = "World"
c = a + b
print(c)

#To add a space between them, add a " ":
a = "Hello"
b  = "World"
c = a + " " + b
print (c)

#Python - Format - Strings
#Combine string with number
age = 36
txt = "I am {}"
print(txt.format(age))


#The format() method takes unlimited number of arguments, and are placed into the respective placeholders:
number_of_piece = 5
nos = 567
amount = 50
myorder = "I need {} piece of item number{} for {} dollar"
print(myorder.format(number_of_piece, nos, amount))

#Escape Character
#To insert characters that are illegal in a string, use an escape character.
#An escape character is a backslash \ followed by the character you want to insert.
#An example of an illegal character is a double quote inside a string that is surrounded by double quotes:

txt = "We are the so-called \"Vikings\" from the north."
print(txt)

#Python String capitalize() Method
txt = "I am good"
print(txt.capitalize())

#The capitalize() method returns a string where the first character is upper case, and the rest is lower case.
capital = "This is FUN"
print(capital.capitalize())

#Python String count() Method
#Return the number of times the value "apple" appears in the string:
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)

#Python Booleans
#Booleans represent one of two values: True or False.
print(10 > 9)
print(10 < 9)
print(10 == 9)

#When you run a condition in an if statement, Python returns True or False:
new1 = 100
new2 = 200

if(new1 > new2):
        print("new1 is greater than new2")
else:
	print("new2 is greater than new1")

#The bool() function allows you to evaluate any value, and give you True or False in return,
print(bool("Hello"))
print(bool(15))






