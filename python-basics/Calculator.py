#Your calculator should:

"""Take user input
Support:
      addition
      subtraction
      multiplication
      division
Keep running until user exits"""



while True:
    num_1 = float(input("Enter first number: "))
    op = input("Enter operator: ")
    num_2 = float(input("Enter second number: "))

    if num_2 == 0:
        print("Doesn't allow division by zero")
    elif op == "-":
        print(num_1 - num_2)
    elif op == "*":
        print(num_1 * num_2)
    elif op == "/":
        print(num_1 / num_2)
    elif op == "+":
        print(num_1 + num_2)
    else:
        print("Error!")

    again = input("Do you want to continue? (yes/no): ")
    if again.lower() != "yes":
        break




































