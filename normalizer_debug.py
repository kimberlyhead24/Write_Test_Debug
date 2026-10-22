def normalize_user(payload: dict) -> dict:
    """Validate and normalize a single user payload into a canonical dict."""
    
    # Ensure all required fields are present.
    for key in ("id", "name", "age", "active"):
        if key not in payload:
            raise ValueError(f"missing {key}")
     
    # Convert id and age to integers; fail fast on invalid values.
    try:
        user_id = int(payload["id"])
    except Exception:
        raise ValueError("User id cannot be converted to integer")

    try:
        user_age = int(payload["age"])
    except Exception:
        raise ValueError("User age cannot be converted to integer")

    active_val = None

    # Normalize the 'active' field to a boolean from either bool or string input.
    if isinstance(payload["active"], bool):
        active_val = payload["active"]
    elif isinstance(payload["active"], str):
        val = payload["active"].lower().strip()
        if val == "true":
            active_val = True
        elif val == "false":
            active_val = False
        else:
            raise ValueError("Incorrect active value type")


    else:
        raise ValueError("Incorrect active value type")
    
     # Build normalized dict without mutating the input payload.
    return {
        "id": user_id,
        "name": payload["name"].strip(),
        "age": user_age,
        "status": "active" if active_val == True else "inactive",
    }
