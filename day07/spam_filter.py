import re
def is_spam(number: str) -> bool:
 
    # Pattern to match basic structure and group only the digits
    pattern = r"\+(0[0-9]?)\s\((\d{3})\)\s(\d{3})-(\d{4})"
    match = re.fullmatch(pattern, number)
    
    if not match:
        return True

    # giving the groups names
    country_code, area_code, local_front, local_back = match.groups()

    # Find out if area code is below or above the range
    area_code_num = int(area_code)
   
    if not 200 <= area_code_num <= 900:
        return True
    
    # Checking sum in start of local number is not in end of local number
    sum_local_front = sum(int(digit) for digit in local_front)
    if str(sum_local_front) in local_back:
        return True

    digit_string = country_code + area_code + local_front + local_back

    count = 1
    
    for  previous, current in zip(digit_string, digit_string[1:]):
        if current == previous:
            count += 1
            if count >= 4:
                return True
        else:
            count = 1
    
    return False
