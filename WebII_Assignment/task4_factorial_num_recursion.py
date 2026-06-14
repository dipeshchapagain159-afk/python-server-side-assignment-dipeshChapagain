#Taking input form user
number = int(input("Enter the number: "))

def fact(num):
    if num<0:
        return "Factorial is not defined for negative number."
    elif num==0 or num==1:
        return 1
    else:
        return num* fact(num-1)
    
print(f"The factorial of {number} is {fact(number)}")