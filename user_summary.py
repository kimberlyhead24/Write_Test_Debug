def events_summary(events: list[dict]) -> list[dict]:
    summary = {}
    for event in events:
        for key in ("user_id", "type", "duration_ms"):
            if key not in event:
                raise ValueError(f"Missing {key}")
        user_id = event["user_id"]
        duration = event["duration_ms"]
        if not isinstance(user_id, int) or isinstance(user_id, bool):
            raise ValueError("user_id must be an integer")
        if not isinstance(duration, int) or isinstance(duration, bool):
            raise ValueError("duration_ms must be an integer")

        entry = summary.setdefault(
            user_id,
            {"user_id": user_id, "total_duration_ms": 0, "event_counts": {}},
        )
        entry["total_duration_ms"] += duration
        counts = entry["event_counts"]
        counts[event["type"]] = counts.get(event["type"], 0) + 1

    return [summary[uid] for uid in sorted(summary)]
    

