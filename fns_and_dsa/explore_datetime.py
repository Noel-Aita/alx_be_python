from datetime import datetime, timedelta

''' The code below gave me the same results but the checker bounced it off '''
'''
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

'''
def display_current_datetime():
    current_date = datetime.now()
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S") )
    return current_date

def calculate_future_date(Ccurrent_date):
    try:
        number_of_days = int(input("Enter the number of days to add to the current date: "))
        future_date = current_date +  timedelta(days=number_of_days)
        print("Future date:", future_date.strftime("%Y-%m-%d"))
    except ValueError:
        print("Please enter a valid integer for the number of days.")

if __name__=="__main__":
    current_date = display_current_datetime()
    calculate_future_date(current_date)