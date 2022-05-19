"""33. Write a Python program to sum of three given integers. 
However, if two values are equal sum will be zero."""

def sum (x, y, z):
        if x == y or x == z or z ==y :
                result = 0
                print(result)
        else:
                result = x + y + z
                print(result)


if __name__ == "__main__":
        sum(2,3,4)
        sum(2,3,3)