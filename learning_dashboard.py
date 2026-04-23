# Personal AI Learning Dashboard
# Created by M. Danush Kumar
# Simple tracker for Cambridge A Levels + AI learning

import datetime

# Sample topics you are studying
topics = {
    "Mathematics": 0,
    "Physics": 0,
    "Computer Science": 0,
    "Prompt Engineering": 0,
    "AI Concepts": 0
}

print("=== Personal AI Learning Dashboard ===\n")
print(f"Date: {datetime.date.today()}\n")

# Log today's learning
print("Log your learning hours today:\n")

for topic in topics:
    hours = float(input(f"How many hours did you study {topic} today? "))
    topics[topic] += hours

# Show summary
print("\n=== Today's Learning Summary ===")
total_hours = 0
for topic, hours in topics.items():
    print(f"• {topic}: {hours} hours")
    total_hours += hours

print(f"\nTotal hours studied today: {total_hours} hours")

# Simple suggestion for next topic
print("\nSuggestion for tomorrow:")
if topics["Mathematics"] < 2:
    print("→ Focus more on Mathematics tomorrow.")
elif topics["Physics"] < 2:
    print("→ Focus more on Physics tomorrow.")
else:
    print("→ Good balance! Try deepening AI Concepts or Prompt Engineering tomorrow.")

print("\nI am building a strong foundation for my University of London degree, Cambridge A Levels, and future AI goals.")
print("Keep consistent! Small daily progress leads to big results.")
