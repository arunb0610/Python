def factorial(number):
    if number == 1:
        return 1
    else:
        return(number*factorial(number-1))
value = 7
print('The factorial of an integer',value,'is',factorial(value))
