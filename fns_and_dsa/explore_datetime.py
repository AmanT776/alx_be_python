import datetime
from datetime import timedelta
def display_current_datetime():
    current_date = datetime.datetime.now()
    print(f"Current date and time: {current_date}")

def calculate_future_date():
    display_current_datetime()
    days = int(input("Enter the number of days to add to the current: "))
    now = datetime.datetime.now()
    future_date = now + timedelta(days=days)
    print(f"Future date: {future_date.date()}")
calculate_future_date()