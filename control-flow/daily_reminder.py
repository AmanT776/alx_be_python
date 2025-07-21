task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
match priority:
    case 'high':
        if time_bound == 'yes':
            print(f"Reminder: '{task}' is a high priority task taht requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' i a high priority task that requires action")
    case 'medium':
        if time_bound == 'yes':
            print(f"Reminder: '{task}' is a medium priority task that requires action")
        else:
            print(f"Reminder: '{task}' is a medium priority task to take action when you have some time")
    case 'low':
        if time_bound == 'no':
            print(f"Reminder: '{task}' is a low priority task. Consider completing it when you have free time.")
        else:
            print(f"Reminder: '{task}' is a a low priority task that doesn't require and immediate action")