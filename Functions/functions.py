## why functions? (interview Questions)
# 1. to make code more readable
# 2. to make code more efficient
# 3. to make code more maintainable
# 4. to make code more reusable
# 5. to make code more extensible


#function

def welcome(msg)->str:
    """
    Description: this fucntion will return show a welcome message 

    Return: this function will return  the welcome message
    """


    return msg


msg=welcome("welcome all")
print(msg+ ", Please check my code")

## funtion to add even and odds numbers 

def even_odd_sum(lst):
    """
    Description: This function returns the sum of even and odd numbers in a list.

    Return: This function will return the sum of even and odd numbers in a list.
    """
    even_sum = 0
    odd_sum = 0

    for i in lst:
        if i % 2 == 0:
            even_sum += i  # Use += to add the value to the sum
        else:
            odd_sum += i  # Use += to add the value to the sum

    return even_sum, odd_sum

sum1,sum2= even_odd_sum([1,2,3,8,8,9,2,45,5,3,2,34])
print(sum1,sum2)