try:
    num1, num2 = eval(input("Enter two numbers seperated by a comma:  "))
    result = num1 / num2
    print("The result after the division is: ", result)
except ZeroDivisionError as zed:
    print("Division by zero is not allowed: ", zed)
except SyntaxError as se:
    print("Syntax error occured: ", se)
except:
    print("Wrong input, please two numbers seperated by a comma like this: 1, 2")
else:
    print("No exceptions occored")

finally:
    print("This will execute no matter what")