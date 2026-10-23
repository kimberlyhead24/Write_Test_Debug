def parse_user(line: str) -> dict:
    user = {}
    parts = line.strip().split(',')
    if len(parts) != 3:
        raise ValueError("Expected exactly 3 fields: id,name,status")
    id_str,name,status = parts   
    
    user["name"] = name.strip()
    user["status"] = status.strip()
    try:
        user["id"] = int(id_str.strip())
    except ValueError:
        raise ValueError("id must be a number")
    
    return user