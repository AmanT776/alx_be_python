def perform_operation(num1,num2,operation):
    match operation:
        case 'add':
            print(num1+num2)
        case 'subtract':
            print(num1-num2)
        case 'multiply':
            print(num1*num2)
        case 'divide':
            if(num2 == 0):
                print("error: division by zero")
            else:
                print(num1/num2)

