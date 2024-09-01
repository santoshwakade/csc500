
# Enter the current time
current_hours = int(input("Enter the current hours (0-23): "))
current_minutes = int(input("Enter the current minutes (0-59): "))

# Enter the number of hours and minutes to wait for the alarm
wait_hours = int(input("Enter the number of hours to wait for the alarm: "))
wait_minutes = int(input("Enter the number of minutes to wait for the alarm: "))

# Calculate the alarm minutes when the alarm will go off
total_minutes = current_minutes + wait_minutes
alarm_minutes = total_minutes % 60

# Get the additional hours from minutes
extra_hours = total_minutes // 60

# Calculate the new hours
total_hours = current_hours + wait_hours + extra_hours
alarm_hours = total_hours % 24  # Ensure the time is within a 24-hour format

print(f"The alarm will go off at {alarm_hours:02d}:{alarm_minutes:02d} on a 24-hour clock.")
