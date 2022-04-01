# Calculator challenge
from art import logo

# Add
def add(n1, n2):
  return n1 + n2

# Subtract
def subtract(n1, n2):
  return n1 - n2

# Multiply
def multiply(n1, n2):
  return n1 * n2

# Divide
def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)
  num1 = float(input("What's the first number?: "))
    
  for symbol in operations:
    operation = ""
    operation += symbol
    print(operation)
    
  # While loops, Flags, and Recursion
  should_continue = True
  
  while should_continue:
   operation_symbol = input("Pick an operation: ") 
   num2 = float(input("What's the next number?: "))
  
    # ===============================================
    # If operation method
    # answer = 0
    
    # if operation_symbol == "+":
    #   answer = add(num1, num2)
    # elif operation_symbol == "-":
    #   answer = subtract(num1, num2)
    # elif operation_symbol == "*":
    #   answer = multiply(num1, num2)
    # elif operation_symbol == "/":
    #   answer = divide(num1, num2)
    # else:
    #   print("Invalid operation symbol. Try again")
    # ================================================
    
    # using a function method
   functional_operator = operations[operation_symbol]
   answer = functional_operator(num1, num2)
    
   print(f"{num1} {operation_symbol} {num2} = {answer}")
  
   if input(f"Type 'y' to continue calculating with {answer}, or 'n' to start a new calculation: ") == "y":
      num1 = answer
   else:
      should_continue = False
      calculator()

calculator()