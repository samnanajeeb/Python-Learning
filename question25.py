"""25. Write a Python program to check whether a specified value 
is contained in a group of values. 
Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False"""

def check_value(n):
	group_of_values = [1,5,8,3]
	if n in group_of_values:
		print("True")
	else:
		print("False")

if __name__ == '__main__':
        check_value(3)
        check_value(-1)