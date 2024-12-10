#exceptions can be user defined or system defined
#they control how 

a = 10 
b = 0 

# try block containts the code which should handled 
try:
    if  not type(a) is int:
        raise TypeError("Only interger numbers are allowed")
    elif a < 11: 
        raise Exception("Please enter an number larger then 11")
    



except ZeroDivisionError:
    print("You cannot divide by zero")
except TypeError:
    print("You must convert string to float or interger before dividing")    
except NameError:
    print("A variable you are trying to use does not exist")
except (ZeroDivisionError, TypeError):
    # You can club multiple exceptions together 
    print("This division is impossible")
except Exception as x: 
    # Handle all remaining exception which are not handled above 
    print("You cannot divide by zero")
    print(x)
    print(x.with_traceback)
    