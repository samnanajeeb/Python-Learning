#Using while loop
#You can loop through the list items by using a while loop.
#Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by refering to their indexes.
#Remember to increase the index by 1 after each iteration.

Kids = ["ayana", "ayaan", "Zara", "Nourin", "Safa", "Ryaan"]
i = 0
while i <len(Kids):
        print(Kids[i])
        i = i + 1

# Looping Using List Comprehension
# List Comprehension offers the shortest syntax for looping through lists:
[print (i) for i in Kids]

#List Comprehension
#List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
#Example:
#Based on a list of fruits, you want a new list, containing only the fruits 
#with the letter "a" in the name.
#Without list comprehension you will have to write a for statement with a
#conditional test inside:

fruits = ["apple", "orange", "Kiwi", "grapes"]
newlist = []
for x in fruits:
        if "a" in x:
                newlist.append(x)
print(newlist)

