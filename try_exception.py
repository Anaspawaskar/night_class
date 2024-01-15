# 1 ) Write a Python program that takes user input for two numbers and performs division. Handle the ZeroDivisionError and ValueError exceptions appropriately.
# Example usage:
# number1 =  10
# number2 = 5
# custiom_devision(number1,number2)

def example():
    try:
        num1 = int(input("enter the number :"))
        num2 = int(input("enter the number :"))
        res = num1/num2
        return res
    
    except ZeroDivisionError as zero:
        return "zero value shld not be entereed"

    except ValueError as v_error:
        return "only number should be entered to do the division process"
    
  
        
result  = example()
print(result)

    



