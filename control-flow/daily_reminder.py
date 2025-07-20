# daily_reminder.py

# Prompt for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Use match-case to handle priority
match priority:
    case "high":
        priority_text = "high priority"
    case "medium":
        priority_text = "medium priority"
    case "low":
        priority_text = "low priority"
    case _:
        priority_text = "unknown priority level"

# Handle time sensitivity
if time_bound == "yes":
    time_text = "that requires immediate attention today!"
else:
    time_text = "Consider completing it when you have free time."

# ✅ Final combined print
print(f"Reminder: '{task}' is a {priority_text} task {time_text}")
