# printing variables
print("Hello")
print('Hello')

#Assigning string to Variables
a = "Hello"
print(a)

#You can assign a multiline string to a variable by using three quotes:
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)


#three single quotes:
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#Slicing
#Get the characters from position 2 to position 5 (not included):
b = "Hello, World!"
print(b[2:5])

#Slice From the Start
#Get the characters from the start to position 5 (not included):
b = "Hello, World!"
print(b[:5])

#Python Modify String
#The upper() method returns the string in upper case
a = "Hello, World!"
print(a.upper())

#The lower() method returns the string in lower case:
a = "Hello, World!"
print(a.lower())

#Remove Whitespace
#Whitespace is the space before and/or after the actual text, and very often you want to remove this space.
#The strip() method removes any whitespace from the beginning or the end:

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"