""" 22. Write a Python program to count the number 4 in a given list."""

def counter(new_list):
        count = 0
        n = 4
        for n in new_list:
                if n == 4:
                        count = count + 1
        return count       
 
if __name__ == '__main__':
        print(counter([1,2,3,4,5,6]))
        print(counter([1, 4, 6, 4, 7, 4]))
        