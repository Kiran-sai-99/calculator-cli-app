def addition(number1,number2):
    return number1 + number2

def substraction(number1,number2):
    return number1 - number2 

def multiplication(number1,number2):
    return number1 * number2 

def division(number1,number2):
    if number2 == 0:
        return "Division by Zero Error...."
    return number1 / number2


while True:
    print("Select operation to perform the task")
    print("1. ADD\n2. SUBSTRACT\n3. MULTIPLICATION\n4. DIVISION\n5. EXIT\n\n")
    
    option = int(input("Enter choice from 1 to 5: "))
    
    if option == 5:
        print("Thank you....Use the calculator again!!!\n\n\n\n")
        break 
    
    
    firstNum = float(input("\nEnter First Number: "))
    secondNum = float(input("Enter Second Number: "))
    
    if option == 1:
        print("\nResult of Addition:",addition(firstNum,secondNum),"\n\n")
    elif option == 2:
        print("\nResult of Substraction:",substraction(firstNum,secondNum),"\n\n")
    elif option == 3:
        print("\nResult of Multiplication:",multiplication(firstNum,secondNum),"\n\n")
    elif option == 4:
        print("\nResult of Division:",division(firstNum,secondNum),"\n\n")
    else:
        print("\nInvalid Input...Please choose option from 1 to 5 only....","\n\n")
        
        
    
    