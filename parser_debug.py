def parse_user(line: str) -> dict:
    user = {}
    parts = line.strip().split(',')
    if len(parts) < 3:
        raise ValueError("Expected exactly 3 fields: id,name,status")
    id_str, name, status = parts

    user["name"] = name.strip()         # added .strip()
    user["status"] = status.strip()     # added .strip()
    user["id"] = int(id_str.strip())    # added .strip()

    return user

# Tests ran showed a failure on stripping whitespace, I need to add stripping for each part to ensure no whitespace
# Test passed after addition