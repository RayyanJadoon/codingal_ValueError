try:
    num =int(input("Enter a number:  "))
    print("The Number you entered is:", num)
except ValueError as ex:
    print("Exception occoured: ", ex) 