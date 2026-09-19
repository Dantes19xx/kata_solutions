def format_duration(seconds: int) -> str:
    if seconds == 0:
        return "now"

    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    years, days = divmod(days, 365)

    def format_unit(value: int, unit: str) -> str:
        if value == 0:
            return ""

        suffix = "" if value == 1 else "s"
        return f"{value} {unit}{suffix}"

    parts = [
        format_unit(years, "year"),
        format_unit(days, "day"),
        format_unit(hours, "hour"),
        format_unit(minutes, "minute"),
        format_unit(seconds, "second"),
    ]

    parts = [part for part in parts if part]

    if len(parts) == 1:
        return parts[0]

    return ", ".join(parts[:-1]) + " and " + parts[-1]