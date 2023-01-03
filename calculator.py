
# Function to perform the calculations
def calculate(num1, num2, operation):
  if operation == "+":
    return num1 + num2
  elif operation == "-":
    return num1 - num2
  elif operation == "*":
    return num1 * num2
  elif operation == "/":
    # Make sure the user is not trying to divide by 0
    if num2 == 0:
      print("Error! Cannot divide by 0")
      return
    return num1 / num2
  else:
    print("Invalid operator")
    return

# Main program
while True:
  # Prompt the user to choose an option and allow them to input - gives third choice to exit
  print("\nEnter '1' to enter two numbers and an operator\n \nEnter '2' to read equations from a file\n \nEnter '3' to Exit Program\n")
  choice = input("\nEnter your choice: \n")

  if choice == "1":
    # Get the numbers and operator from the user
    num1 = input("\nPlease enter the first number: \n")
    operation = input("Enter your operator (+, -, *, /): \n")
    num2 = input("Please enter another number: \n")

    # Convert the numbers to floats and handle any errors that may occur
    try:
      num1 = float(num1)
      num2 = float(num2)
    except ValueError:
      print("Invalid input: You must input a number")
      continue

    # Perform the calculation and display the result
    result = calculate(num1, num2, operation)
    #if result is not None:
      #print(f"Result: {result}")

    # Write the equation to a text file
    with open("equations.txt", "a") as f:
      f.write(f"{num1} {operation} {num2} = {result}")

  # code block for user choosing 2
  elif choice == "2":
    # Get the file name from the user
    file_name = input("\nPlease enter the name of the file you wish to read from: \n")

    # Read the equations from the file and handle any errors that may occur
    try:
      with open(file_name, "r") as f:
        lines = f.readlines()
    except IOError:
      print("Error: file not found")
      continue

    # Iterate through the lines in the file and perform the calculations
    for line in lines:
      # Split the line into the numbers and operator
      parts = line.split()
      num1 = float(parts[0])
      num2 = float(parts[2])
      operation = parts[1]

      # Perform the calculation and display the result
      result = calculate(num1, num2, operation)
      #if result is not None:
      #print(f"\n{num1} {operation} {num2} = {result}")
      #with open(file_name, 'r') as f: 
        #for line in f:
          #print(f)
          #break

  # choice for if they choose to exit
  elif choice == '3':
    break

  else:
    print("Invalid choice")

# prints the text file
  with open("equations.txt", "r") as f:
    for line in f:
      print(line)
