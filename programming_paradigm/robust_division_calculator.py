def safe_divide(numerator,denominator):
    try:
        return f"The result of division is {numerator/denominator}"
    except ZeroDivisionError as e:
        return " Error: Cannot divide by zero."
