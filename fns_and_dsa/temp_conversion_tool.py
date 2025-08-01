FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9 
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32 ) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{celsius}°F")
def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    print(f"{fahrenheit}°C")

temperature = float(input("Enter the temperature to convert: "))
type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

if type == "C" or type=="c":
    convert_to_fahrenheit(temperature)
elif type == "F" or type =="f":
    convert_to_celsius(temperature)
else:
    print("Invalid temperature. Please enter a numeric value.")