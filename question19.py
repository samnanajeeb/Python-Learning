""" Write a Python program to get a string which is n (non-negative integer) 
copies of a given string
1. get a string value
2. print copies of the string.
"""

def math_learing (str, n):
        result = ""
        for i in range(n):
                result = result + str
        return result
print(math_learing('samna' , 5))
                
        