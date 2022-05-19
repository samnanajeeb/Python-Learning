"""27. Write a Python program to concatenate all elements in a list 
into a string and return it."""

def concatenate_string(list):
        result = ""
        for i in list:
                result += str(i)
        print(result)

if __name__ == '__main__':
        concatenate_string(['s', 'a', 'm', 'n', 'a'])