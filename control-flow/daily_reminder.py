<<<<<<< HEAD
# daily_reminder.py

# Prompt for the task details
task = input("Enter your task for today: ")
priority = input("Enter the priority of the task (high, medium, low): ").lower()
time_bound = input("Is the task time-bound? (yes or no): ").lower()

# Ensure valid priority input using a loop
while priority not in ["high", "medium", "low"]:
    print("Invalid priority. Please enter high, medium, or low.")
    priority = input("Enter the priority of the task (high, medium, low): ").lower()

# Use match-case for priority
match priority:
    case "high":
        message = f"🔴 High priority task: '{task}'."
    case "medium":
        message = f"🟡 Medium priority task: '{task}'."
    case "low":
        message = f"🟢 Low priority task: '{task}'."
    case _:
        message = f"Task: '{task}'."  # Default, though won't occur due to validation

# Add extra urgency if the task is time-bound
if time_bound == "yes":
    message += " This is time-sensitive and requires immediate attention today!"
elif time_bound == "no":
    message += " Consider completing it when you have free time."

# Display the reminder
print("\nYour Daily Reminder:")
print(message)
=======
# daily_reminder.py

# Prompt for the task details
task = input("Enter your task for today: ")
priority = input("Enter the priority of the task (high, medium, low): ").lower()
time_bound = input("Is the task time-bound? (yes or no): ").lower()

# Ensure valid priority input using a loop
while priority not in ["high", "medium", "low"]:
    print("Invalid priority. Please enter high, medium, or low.")
    priority = input("Enter the priority of the task (high, medium, low): ").lower()

# Use match-case for priority
match priority:
    case "high":
        message = f"🔴 High priority task: '{task}'."
    case "medium":
        message = f"🟡 Medium priority task: '{task}'."
    case "low":
        message = f"🟢 Low priority task: '{task}'."
    case _:
        message = f"Task: '{task}'."  # Default, though won't occur due to validation

# Add extra urgency if the task is time-bound
if time_bound == "yes":
    message += " This is time-sensitive and requires immediate attention today!"
elif time_bound == "no":
    message += " Consider completing it when you have free time."

# Display the reminder
print("\nYour Daily Reminder:")
print(message)
>>>>>>> c12935383a58d7cb7028c7ab31ae47f303f24622
