# --- Constants ---
MINUTES_PER_HOUR = 60
HOURS_PER_DAY = 24
HOURS_IN_12H_CLOCK = 12
WEEK_DAYS = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

# -----------------------------------------------


def add_time(start, duration, start_day=''):
    """
    Calculates the resulting time after adding a duration without using any time libraries

    Args:
        start(str): The start time in 'H:MM AM/PM' format.
        duration(str): The duration to add in 'H:MM' format.
        start_day(str, optional): The starting day of the week (case-insensitive). Defaults to ''.

    Returns:
        str: The resulting time and day string.
    """


    # -------------------------------------------
    # --- Parse Initial Inputs ---

    # Separate the start time from the AM/PM period
    start_time, period = start.split()

    # Split the time and duration into hours and minutes, converting them to integers.
    start_hours, start_minutes = map(int, start_time.split(':'))
    duration_hours, duration_minutes = map(int, duration.split(':'))


    # -------------------------------------------
    # --- Calculate Total Hours and Minutes ---

    # Temporarily converting to 24-hour format for easier day calculations.
    if period == 'PM':
        start_hours += HOURS_IN_12H_CLOCK

    # Add the hours and minutes from the start and duration times.
    total_hours = start_hours + duration_hours
    total_minutes = start_minutes + duration_minutes

    # If minutes exceeds 59, carry over the excess to hours.
    total_hours += total_minutes // MINUTES_PER_HOUR
    final_minutes = total_minutes % MINUTES_PER_HOUR


    # -------------------------------------------
    # --- Determine Days Passed and Format the Final Time String ---

    # Calculate the number of full days that have passed.
    days_passed = total_hours // HOURS_PER_DAY

    # Get the final hour for the resulting day in a 24-hour format.
    final_hour_24h = total_hours % HOURS_PER_DAY

    # Format the final time in a 12-hour format.
    if final_hour_24h >= HOURS_IN_12H_CLOCK:
        final_period = 'PM'
        final_hour_12h = final_hour_24h - HOURS_IN_12H_CLOCK
    else:
        final_period = 'AM'
        final_hour_12h = final_hour_24h

    # Convert special cases for the 12-hour clock (12 AM/PM)
    if final_hour_12h == 0:
        final_hour_12h = 12  # 00:XX becomes 12:XX

    # Assemble the final time string.
    final_time = f'{final_hour_12h}:{final_minutes:02d} {final_period}'


    # -------------------------------------------
    # --- Add Day of the Week (if provided) ---

    if start_day:
        start_day_index = WEEK_DAYS.index(start_day.title())

        # Calculate the final day's index.
        final_day_index = (start_day_index + days_passed) % len(WEEK_DAYS)
        final_day = WEEK_DAYS[final_day_index]
        final_time += f', {final_day}'


    # -------------------------------------------
    # --- Add "Days Later" Text ---

    if days_passed == 1:
        final_time += ' (next day)'
    elif days_passed > 1:
        final_time += f' ({days_passed} days later)'


    # -------------------------------------------

    return final_time

# -----------------------------------------------

# --- Example Usage ---

print(add_time('3:00 PM', '3:10'))
# 6:10 PM

print(add_time('11:30 AM', '2:32', 'Monday'))
# 2:02 PM, Monday

print(add_time('11:43 AM', '00:20'))
# 12:03 PM

print(add_time('10:10 PM', '3:30'))
# 1:40 AM (next day)

print(add_time('11:43 PM', '24:20', 'tueSday'))
# 12:03 AM, Thursday (2 days later)

print(add_time('6:30 PM', '205:12'))
# 7:42 AM (9 days later)
