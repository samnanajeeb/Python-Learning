"""7. Write a Python program to accept a filename from the user 
and print the extension of that. Go to the editor
Sample filename : abc.java
Output : java """
# The repr() function returns a printable representation of the given object.

file_name = input ("please enter the file name: ")
file_extension = file_name.split(".")
print("The extension of the file is: " + repr(file_extension[-1]) ) 