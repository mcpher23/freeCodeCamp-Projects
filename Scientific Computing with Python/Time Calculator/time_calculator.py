
def add_time(time, duration, day='False'):

    # Break up the input into the time and the ampm describtion. The break up the time into hours and minutes.
    numbers = time.split()[0]
    start_hour = int(numbers.split(':')[0])
    start_minute = int(numbers.split(':')[1])
    ampm = time.split()[1]
    duration_hours = int(duration.split(':')[0])
    duration_minutes = int(duration.split(':')[1])
    
    # Intiate a counter for days later
    days = 0
    
    # Add the duration of minutes to the start time. If this goes over 60 then add an hour to the duration and reset minutes by subtracting 60
    end_minutes = start_minute + duration_minutes
    
    if end_minutes >= 60:
        end_minutes = end_minutes % 60
        duration_hours += 1
            
    # Calculate how many half days will pass in the duration of hours and add the left over hours to the start time    
    halfdays = (duration_hours // 12)
    end_hour = (start_hour + duration_hours) % 12
    
    # Add the duration of hours to the start time. If this goes over 12 then add 1 to the halfdays counter and reset hours by subtracting 12
    if (start_hour + duration_hours % 12) >= 12:
        halfdays += 1
    if end_hour == 0:
        end_hour = 12
    
    # If the minute is under 10 cocantonate the number with a 0 before for formatting
    end_hour = str(end_hour)
    end_minutes = str(end_minutes) if end_minutes > 10 else '0' + str(end_minutes)
    
    # Calculate the number of full days past
    days = (duration_hours // 24)
    
    # If the time starts in the PM and half a day has past count this as a day as its gone past midnight
    if ampm == 'PM':
        if halfdays % 2 != 0:
            end_ampm = 'AM'
            days += 1
        else: end_ampm = ampm      
    elif ampm == 'AM':
        if halfdays % 2 != 0:
            end_ampm = 'PM'
        else: end_ampm = ampm
    
    # Depending on whether days have passed change the output string
    new_time = end_hour + ':' + end_minutes + ' ' + end_ampm 
    weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    
    day = day.lower()
    if day in weekdays:
        location = weekdays.index(day)    
        new_location = days + location  
        end_day = weekdays[(new_location % 7)]  
        end_day = end_day.capitalize()
        new_time += f", {end_day}"
              
    if days == 1:
        return new_time + ' (next day)'             
    elif days > 1:
        return new_time + f' ({days} days later)'  
    
    return new_time           

# Test Case
result = add_time("8:16 PM", "466:02", "tuesday")


# Test Response Expected "6:18 AM, Monday (20 days later)"
print(result)