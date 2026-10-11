month_length = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

def is_leap_year(year: int) -> bool:
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

def days_remaining_in_month(date_string: str) -> int:
    
    day = int(date_string[8:])
    month = int(date_string[5:7])
    year = int(date_string[:4])

    # Find out how many days left in the month
    if month == 2 and is_leap_year(year):
        return 29 - day
    
    return month_length[month - 1] - day

def days_remaining_in_year(date_string: str) -> int:
    year = int(date_string[:4])
    month = int(date_string[5:7])

    # Find how many months left
    days = days_remaining_in_month(date_string)
    for month in range(month + 1, 13):
        if month == 2 and is_leap_year(year):
                days += 29 
        else:
            days += month_length[month - 1]
    return days
                 

def days_between(start_date: str, end_date: str) -> int:

    if start_date > end_date: 
        return days_between(end_date, start_date)

    start_year = int(start_date[:4]) 
    end_year = int(end_date[:4])

    days = days_remaining_in_year(start_date)

    for year in range(start_year + 1, end_year + 1):
            if is_leap_year(year):    
                days += 366
            else:
                days += 365
        
    days -= days_remaining_in_year(end_date)

    return days    
    

def moon_phase(date_string: str) -> str:
    phases = ("New", "Waxing", "Full", "Waning")
    amount_of_days = days_between("2000-01-06", date_string)
    phase_idx = (amount_of_days % 28) // 7
    
    return phases[phase_idx]
