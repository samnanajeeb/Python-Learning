""" Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn 
Sample value of n is 5
Expected Result : 615 
Python int(x, base=10):
The function returns an integer object constructed from a number or string x, 
or return 0 if no arguments are given. If x is a number, return x.__int__(). 
For floating point numbers, this truncates towards zero.
5
55
555
----
615 """

n = int(input("Please enter the number:"))
n1 = int("%s" % n)
n2 = int("%s%s" % (n,n))
n3 = int("%s%s%s" % (n,n,n))
output = n1+n2+n3
print(output)



