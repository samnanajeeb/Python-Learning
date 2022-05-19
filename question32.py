"""32. Write a Python program to get the least common multiple (LCM) 
of two positive integers.
"""

def new(x , y):
        if x > y:
                z = x
        elif y > x:
                z = y
        while(True):
                if((z % x == 0) and (z % y == 0)):
                        lcm = z
                        break
                z += 1
        return lcm
if __name__ == "__main__":
	print(new(4, 6))
	print(new(15, 17))	