import re
def is_spam(number):
    spam = False

    # Pattern to match basic structure
    full_pattern = r"\+0[0-9]?\s\(\d{3}\)\s\d{3}-\d{4}"

    if not re.fullmatch(full_pattern, number):
        spam = True
        return spam

    # Section out the number except we are done with couuntry code
    parts = number.split()

    area_code = parts[1] 
    local_number = parts[2]

    # Find out if area code is below or above the range
    area_num = int(area_code[1:-1])
    if area_num < 200 or area_num > 900:
        spam = True
        return spam

    # Turning local number into two parts
    first_part, last_part = local_number.split("-")
    
    # Checking sum in start of local number is not in end of local number
    first_part_sum = sum(int(digit) for digit in first_part)
    if str(first_part_sum) in last_part:
        spam = True
        return spam

    digit_string = re.sub(r"\D", "", number)

    count = 1
    
    for idx, char in enumerate(digit_string):
        if idx == 0:
            continue

        if char == digit_string[idx - 1]:
            count += 1
            if count >= 4:
                return True
        else:
            count = 1
    
    return spam
