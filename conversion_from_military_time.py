def to_12(time):
    minute = (time[2:])
    hour = int(time[:2])
    abrev = "AM" if hour < 12 else "PM"
    hour = hour % 12 or 12
       
      
        
    return f"{hour}:{minute} {abrev}"
