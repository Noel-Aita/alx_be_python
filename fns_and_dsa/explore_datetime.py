import datetime

def display_current_datetime():
    current_date = datetime.datetime.now()
    print(f"Current date and time: {current_date}")


def calculate_future_date():
    current_date = datetime.date.today()
    date = datetime.timedelta(days=int(input("Enter the number of days: ")))
    future_date = date + current_date
    print(future_date)

display_current_datetime()
calculate_future_date()
    



