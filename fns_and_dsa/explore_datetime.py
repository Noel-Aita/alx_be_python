import datetime

def display_current_datetime():
    current_date = datetime.datetime.now()
    print(f"Current date and time: {current_date}")


def calculate_future_date():
    current_date = datetime.date.today()
    date = datetime.timedelta(days=int(input("Enter the number of days to add to current date: ")))
    future_date = date + current_date
    print(f"Future date: {future_date}")

display_current_datetime()
calculate_future_date()
    



