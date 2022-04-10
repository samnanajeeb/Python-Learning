#there are not many values that evaluate to False, except empty values, 
# such as (), [], {}, "", the number 0, and the value None. 
# And of course the value False evaluates to False.

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

#One more value, or object in this case, evaluates to False, 
# and that is if you have an object that is made from a class 
# with a __len__ function that returns 0 or False:

class my_obj():
        def _len_(self):
                return(0)

myobj = my_obj()
print(bool(myobj))

