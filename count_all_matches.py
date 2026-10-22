import re
def count(text, parameter):
    pattern = f"(?=({re.escape(parameter)}))"
    found_list = re.findall(pattern, text)
    count = len(found_list)



    return count
