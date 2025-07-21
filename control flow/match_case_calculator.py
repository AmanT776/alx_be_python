num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose the operation (+,-,*,/): ")

match operation:
    case '+':
        sum = num1 + num2
        print(f"The result is {sum}")
    case '-':
        difference = num1-num2
        print(f"The result is {difference}")
    case '*':
        product = num1 * num2
        print(f"The result is {product}")
    case '/':
        if num2==0: 
            print("Cannot divide by zero")
        division = num1 / num2
        print(f"The result is {division}")

    