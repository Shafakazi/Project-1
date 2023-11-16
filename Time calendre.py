def add_time(start_time, duration, start_day=None):
  # Convert start_time to 24-hour format
  start_time_split = start_time.split()
  time_parts = start_time_split[0].split(":")
  hours, minutes = int(time_parts[0]), int(time_parts[1])

  if start_time_split[1] == "PM" and hours != 12:
    hours += 12

  # Convert duration to hours and minutes
  duration_parts = duration.split(":")
  duration_hours, duration_minutes = int(duration_parts[0]), int(
      duration_parts[1])

  # Add duration to start_time
  new_hours = hours + duration_hours
  new_minutes = minutes + duration_minutes

  # Calculate days
  days_passed = new_hours // 24
  new_hours %= 24

  # Convert back to 12-hour format
  if new_hours > 12:
    new_hours -= 12
    period = "PM"
  elif new_hours == 12:
    period = "PM"
  else:
    period = "AM"

  # Format result
  new_time = f"{new_hours}:{new_minutes:02d} {period}"

  # Handle days and start_day
  if days_passed == 1:
    new_time += " (next day)"
  elif days_passed > 1:
    new_time += f" ({days_passed} days later)"

  # Handle start_day
  if start_day:
    start_day = start_day.lower().capitalize()
    days_of_week = [
        "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",
        "Sunday"
    ]
    start_day_index = (days_of_week.index(start_day) + days_passed) % 7
    new_time += f", {days_of_week[start_day_index]}"

  return new_time


# Test cases
print(add_time("3:00 PM", "3:10"))  # Returns: 6:10 PM
print(add_time("11:30 AM", "2:32", "Monday"))  # Returns: 2:02 PM, Monday
print(add_time("11:43 AM", "00:20"))  # Returns: 12:03 PM
print(add_time("10:10 PM", "3:30"))  # Returns: 1:40 AM (next day)
print(add_time("11:43 PM", "24:20",
               "tueSday"))  # Returns: 12:03 AM, Thursday (2 days later)
print(add_time("6:30 PM", "205:12"))  # Returns: 7:42 AM (9 days later)
