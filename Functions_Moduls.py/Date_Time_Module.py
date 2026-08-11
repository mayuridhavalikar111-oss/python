from datetime import datetime

# Display the current date and time
current_datetime = datetime.now()
print("Current Date and Time:", current_datetime)

# Compute the difference between two dates
date1 = datetime(2025, 1, 1)
date2 = datetime(2026, 6, 20)

difference = date2 - date1
print("Difference between dates:", difference)