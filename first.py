import random

secret_number_ = random.randint(1,10)
guess = int(input("guess the number"))
match guess:
    case secret_number_:
        print("Congratulations, you guessed it!")
    case <secret_number_:
        print("Nope, your guess is a bit low")
    case range(secret_number_,10):
        print("Oops,your guess is a bit high. Try again")

