"""21. Write a Python program to find whether a given number (accept from the user)
is even or odd, print out an appropriate message to the user. """

def number_even_or_odd(n):
        m = n%2 
        if m == 0:
                print("n is even")
        else:
                print("n is odd")
  
if __name__ == '__main__':
        n = int(input("Please enter a number you want to check even or odd: "))
        number_even_or_odd(n)