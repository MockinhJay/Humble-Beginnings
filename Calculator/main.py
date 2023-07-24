from artlogo import logo
from clearFunction import clear

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

print(logo)

def calculator():
  continue_calculation = True
  
  num1 = int(input("Enter first number: "))
  for symbol in operations:
    print(symbol)
  
  while continue_calculation:
    operation_symbol = input("Pick an operation: ")
    calculation_function = operations[operation_symbol]
    num2 = int(input("Enter number: "))
    answer = calculation_function(num1, num2)
    
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    
    should_continue = input(f"Type 'y' to continue calculation with {answer}, or type 'n' to start a new calculation: ")
  
    if should_continue == "y":
      num1 = answer
    else:
      continue_calculation = False
      clear()
      print(logo)
      calculator()

calculator()