"""35. Write a Python program that will return true 
if the two given integer values are equal or their sum or difference is 5."""

def sum(x, y):
        if (x == y) or ((x + y) == 5) or ((x - y) == 5):
                return True
        else:
                return False

if __name__ == "__main__":
        print(sum(20, 50))
        print(sum(66, 97))