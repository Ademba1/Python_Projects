logo = """
 _____________________
|  _________________  |
| | Ademba1      0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


def add(n1, n2):
    """ Adds n1 to n2"""
    return n1 + n2

def subtract(n1, n2):
    """Substract n2 from n1"""
    return n1 - n2

def divide(n1, n2):
    """ Divide n1 with n2"""
    return n1 / n2

def multiply(n1, n2):
    """Multiply n1 and n2"""
    return n1 * n2


operations ={
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply,
}

def calculator():
    print(logo)
    num1 = float(input("What is the First Number?: "))

    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:

        oper_symbol = input("Pick an operation: ")

        num2 = float(input("What is the next Number?: "))
        calculation_function = operations[oper_symbol]
        answer = calculation_function(num1,num2)


        print(f"{num1}{oper_symbol}{num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer} or type 'n' to exit: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()
calculator()

