from art import logo
print(logo)

def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mul(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1 / n2

calculator = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

calc = True

while calc:
    num1 = float(input("Enter your first number: "))

    cont_with_result = True
    while cont_with_result:
        operator = input("Enter your operator:\n+\n-\n*\n/\n")
        num2 = float(input("Enter your second number: "))

        if operator in calculator.keys():
            result = calculator[operator](num1, num2)
            print(f"{num1} {operator} {num2} = {result}")

            cont = input(
                f"Continue calculating with {result}? Type 'y' to continue, 'n' to start over, or 'exit' to quit: ").lower()
            if cont == "y":
                num1 = result
            elif cont == "n":
                cont_with_result = False
            elif cont == "exit":
                calc = False

        else:
            print("Invalid operator.")













