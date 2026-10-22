def events_summary(events: list[dict]) -> list[dict]:
    for key in ("user_id", "type", "duration_ms"):
        if key not in events:
            raise ValueError(f"Missing {key}")
        
    total_duration = 0
    output = {}
    

