# Calculator
#import calculator

#calculator()

"""
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def power(n1, power_times):
    return n1 ** power_times

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "**": power,
    #"=": finish
    }

#print(operations["*"])
number1 = float(input("What's the first number?: "))
for symbol in operations:
    print(symbol)
operation_symbol = input("Pick an operation from the line above: ")
number2 = float(input("What's the next number?: "))

operation_function = operations[operation_symbol]
answer = operation_function(number1, number2)

print(f"{number1} {operation_symbol} {number2} = {answer}")"""

# Calculator

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def power(n1, power_times):
    return n1 ** power_times

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "**": power,
    #"=": finish
    }

#print(operations["*"])
number1 = float(input("What's the first number?: "))
for symbol in operations:
    print(symbol)
operation_symbol = input("Pick an operation from the line above: ")
number2 = float(input("What's the next number?: "))

operation_function = operations[operation_symbol]
answer = operation_function(number1, number2)

print(f"{number1} {operation_symbol} {number2} = {answer}")

decide_continue_calculating = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ")
if decide_continue_calculating == 'y':
	continue_calculating = True
else:
	continue_calculating = False
new_answer = 0
answer2 = None
while continue_calculating:
    operation_symbol = input("Pick an operation: ")
    number3 = float(input("What's the next number?: "))
    operation_function = operations[operation_symbol]
      
    if answer2 is None:
      answer2 = operation_function(answer, number3)
      print(f"{answer} {operation_symbol} {number3} = {answer2}")
    else:
      new_answer = answer2
      answer2 = operation_function(new_answer, number3)
      print(f"{new_answer} {operation_symbol} {number3} = {answer2}")
	#answer = operation_function(operation_function(number1, number2), number3)
    decide_continue_calculating = input(f"Type 'y' to continue calculating with {answer2}, or type 'n' to exit.: ")
    if decide_continue_calculating == 'n':
      continue_calculating = False