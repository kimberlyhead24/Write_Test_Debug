def normalize_user(payload: dict) -> dict:
    """Validate and normalize a single user payload into a canonical dict."""
    # Ensure all required fields are present.
    for key in ("id", "name", "age", "active"):
        if key not in payload:
            raise ValueError(f"missing required field: {key}")

    # Convert id and age to integers.
    try:
        user_id = int(payload["id"])
        age = int(payload["age"])
    except ValueError:
        raise ValueError("id and age must be integers")

    # Normalize the active field to a boolean.
    is_active = normalize_active(payload["active"])

    # Build normalized dict without mutating the input payload.
    return {
        "id": user_id,
        "name": payload["name"].strip(),
        "age": age,
        "status": "active" if is_active else "inactive",
    }


def normalize_active(active_value):
    """Normalize various representations of 'active' to a boolean."""
    if isinstance(active_value, bool):
        return active_value

    if isinstance(active_value, str):
        val = active_value.strip().lower()
        truthy = {"true"}     # Extendable to {"true", "yes", "1"} if needed.
        falsy = {"false"}     # Extendable to {"false", "no", "0"} if needed.
        if val in truthy:
            return True
        if val in falsy:
            return False

    raise ValueError("invalid active value")




