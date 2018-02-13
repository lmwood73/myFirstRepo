def add(num1, num2):
    """Returns num1 + num2"""
    return num1 + num2


def subtract(num1, num2):
    """Returns num1 - num2"""
    return num1 - num2


def multiply(num1, num2):
    """Returns num1 * num2"""
    return num1 * num2


def divide(num1, num2):
    """Returns num1 / num2"""
    return num1 / num2


def options():
    """Returns list of possible functions to call"""
    print("addition \n subtraction \n multiplication \n division")


def choice(myChoice):
    """Calls a math function or displays options"""



def main():
    myName = input("What is your name? \n")
    print("OK", myName+',', "What calculator function would you like to perform?")
    print("Type \"options\" to see available functions")
    print("If you know the function, call it now")
    option = input("Make selection now...\n")
    choice(option)


main()
