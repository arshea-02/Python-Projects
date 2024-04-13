#Was not supposed to use any Liberaries
def add_time(start, duration, weekday=''):
    
    hours = []
    minutes = []
    index = 0
    size = 0
    daysOfWeek = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

    #Splitting the start time into hours, minutes and meridiem
    split_start_time = start.split(':')
    split_min_and_meridiem = split_start_time[1].split(' ')

    hours.append(int(split_start_time[0]))
    minutes.append(int(split_min_and_meridiem[0]))
    meridiem = split_min_and_meridiem[1] 

    #Splitting duration into hours and minutes
    split_duration = duration.split(':')

    hours.append(int(split_duration[0]))
    minutes.append(int(split_duration[1]))

    hour = hours[0] + hours[1]
    minute = minutes[0] + minutes[1]

    #handling case where minute is greater than or equal to 60
 
    if minute == 60:
        hour += 1
        minute = 0
    elif minute > 60:
        minute -= 60
        hour += 1
    count=0

    #handling case where hour is greater than or equal to 12
    while hour >= 12:
        hour -= 12
        if meridiem == 'AM':
            meridiem = 'PM' 
        elif meridiem == 'PM':
            meridiem = 'AM'
            count += 1
            
    

    if hour == 0:
            hour = 12
    new_time = f"{str(hour)}:{str(minute).zfill(2)} {meridiem}"

    if weekday:
        index = daysOfWeek.index(weekday.capitalize())
        size = len(daysOfWeek)

    if count == 0:
        if weekday.capitalize():
            new_time += f", {weekday}"
        else:
            pass
    elif count == 1:
        if weekday:
            new_time += f", {daysOfWeek[(index+1)%size]} (next day)" 
        else:
            new_time += f" (next day)"
    elif count > 1:
        if weekday:
            new_time += f", {daysOfWeek[(index+count)%size]} ({count} days later)"
        else:    
            new_time += f" ({count} days later)"


    print(new_time)
    return new_time

add_time('3:30 PM', '2:12')
add_time('11:55 AM', '3:12')
add_time('2:59 AM', '24:00')
add_time('11:59 PM', '24:05')
add_time('8:16 PM', '466:02')
add_time('3:30 PM', '2:12', 'Monday')
add_time('2:59 AM', '24:00', 'saturDay')
add_time('11:59 PM', '24:05', 'Wednesday')
add_time('8:16 PM', '466:02', 'tuesday') 
