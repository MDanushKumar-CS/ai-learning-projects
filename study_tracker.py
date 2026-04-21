# Cambridge A Levels Study Progress Tracker
# Created by M. Danush Kumar

subjects = {
    "Mathematics": 0,
    "Physics": 0,
    "Computer Science": 0
}

print("=== Cambridge A Levels Study Progress Tracker ===\n")

for subject in subjects:
    hours = float(input(f"How many hours did you study {subject} today? "))
    subjects[subject] += hours

print("\nToday's Progress:")
for subject, hours in subjects.items():
    print(f"• {subject}: {hours} hours")

print("\nKeep going! You are preparing for a bright future in Computer Science & AI.")
