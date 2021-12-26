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

operation_function = {
  "+": add,
  "-": sub,
  "*": mul,
  "/": div,
}

def calculator():
  first_num = float(input('What\'s the first number?: \n'))
  for symbols in operation_function:
    print(symbols)
    
  flag = True
  while flag == True:
    operation = input('Pick an operation: \n')
    next_num = float(input('What\'s the next number?: \n'))
    function = operation_function[operation]
    result = function(first_num, next_num)

    print(f'{first_num} {operation} {next_num} = {result}')

  
    user_contin = input(f"Type 'y' to continue calculating with {result} or type 'n' to start over or type 'exit' to end.\n")
    if user_contin == 'y':
      first_num = result
    elif user_contin == 'exit':
      flag = False
    elif user_contin == 'n':
      calculator()
    else:
      print('Wrong input, revert back to last result.')
      first_num = result

calculator()
