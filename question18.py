"""Write a Python program to calculate the sum of three given numbers, 
if the values are equal then return three times of their sum"""

def sum_of_numbers(n1, n2, n3):
        n = n1 + n2 + n3
        if n1 == n2 == n3:
                n = n * 3
        return n
                
 
print(sum_of_numbers(10, 20, 30))
print(sum_of_numbers(10, 10, 10))
        