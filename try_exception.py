# 1 ) Write a Python program that takes user input for two numbers and performs division. Handle the ZeroDivisionError and ValueError exceptions appropriately.
# Example usage:
# number1 =  10
# number2 = 5
# custiom_devision(number1,number2)

"""def example():
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
print(result)"""


#2.Write a Python function that takes a list of numbers as input and calculates the average. Handle the ZeroDivisionError and any other exceptions that may occur.
# Example usage:
#numbers_list = [1, 2, 3, 4, 5]
#calculate_average(numbers_list)

def list_number():
    try:
        listin = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
        total = sum(listin)
        avg = total / len(listin)
        return avg


    except ZeroDivisionError as z_value:
        print("zero number should not be added in the list to get the average :")

    except ValueError as v_error:
        print("only numbers should be added in the list ")
    
    except Exception as error :
        print("error something is invalid here ")

example = list_number()
print(example)
        
    



