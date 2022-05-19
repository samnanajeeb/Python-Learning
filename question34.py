"""34. Write a Python program to sum of two given integers. 
However, if the sum is between 15 to 20 it will return 20."""

def sum(x , y):
        result = x + y
        if result >= 15 and result <=20:
                print(20)
        else:
                print(result)

if __name__ == "__main__":
        sum(15, 2)
        sum(100, 200) 