#there are not many values that evaluate to False, except empty values, 
# such as (), [], {}, "", the number 0, and the value None. 
# And of course the value False evaluates to False.

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

#One more value, or object in this case, evaluates to False, 
# and that is if you have an object that is made from a class 
# with a __len__ function that returns 0 or False:

class my_obj():
        def _len_(self):
                return(0)

myobj = my_obj()
print(bool(myobj))

# Functions can Return a Boolean
def myFunction() :
  return True

print(myFunction())

# Print "YES!" if the function returns True, otherwise print "NO!":
def my_func():
  return(True)
if my_func():
  print("yes")
else :
	print("No")

# Python also has many built-in functions that return a boolean value, 
# like the isinstance() function, which can be used to determine 
# if an object is of a certain data type:

x = 200
print(isinstance(x, int))

#List
thislist = ["apple", "banana", "grapes"]
print(thislist)

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#To determine how many items a list has, use the len() function:
print(len(thislist))

#To print the type of list
mylist = ["apple", "Banana", "Grapes"]
print(type(mylist))

"""Python Collections (Arrays)
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members"""

thislist = ["apple", "orange", "Grapes"]
print(thislist[1])

"""Negative Indexing
Negative indexing means start from the end
-1 refers to the last item, -2 refers to the second last item etc."""

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#Range of Indexes
#You can specify a range of indexes by specifying where to start and where to end the range.
#When specifying a range, the return value will be a new list with the specified items.

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#Lists are used to store multiple items in a single variable.
#
thislist = ["apple", "banana", "grapes"]
print(thislist)

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#To determine how many items a list has, use the len() function:
print(len(thislist))

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#Check if Item Exists
thislist = ["apple", "banana", "cherry"]
if "orange" in thislist:
  print("yes, 'orange' in list")
  
#Change the second value by replacing it with two new values:
thislist1 = ["apple", "kiwi", "mango"]

#To insert a new list item, without replacing any of the existing values,
# we can use the insert() method.

thislist.insert(2, "kiwi")
print(thislist)

#append
thislist.append("broccoli")
print(thislist)

#Extend To append elements from another list to the current list, 
# use the extend() method.

vegetables = ["carrot", "corainder", "cauliflower"]
thislist.extend(vegetables)
print(thislist)

#remove
thislist.remove("corainder")
print(thislist)

#The pop() method removes the specified index.
thislist.pop(1)
print(thislist)

#If you do not specify the index, the pop() method removes the last item.
thislist.pop()
print(thislist)

#The del keyword also removes the specified index:
del thislist[0]
print(thislist)

# The clear() method empties the list.
# The list still remains, but it has no content.
thislist.clear()
print(thislist)

#Loop Through a List
#You can loop through the list items by using a for loop:
#Print all items in the list, one by one
thislist = ["samna", "sahad", "sajina", "shabina", "Shiban", "Shiblu"]
for x in thislist:
  print(x)

#Loop Through the Index Numbers
#You can also loop through the list items by referring to their index number.
#Use the range() and len() functions to create a suitable iterable.
#Print all items by referring to their index number:
for i in range(len(thislist)):
  print(thislist[i])

