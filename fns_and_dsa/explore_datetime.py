import datetime
from datetime import timedelta
def display_current_datetime():
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {current_date}")

def calculate_future_date():
    display_current_datetime()
    days = int(input("Enter the number of days to add to the current date: "))
    now = datetime.datetime.now()
    future_date = now + timedelta(days=days)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")
calculate_future_date()