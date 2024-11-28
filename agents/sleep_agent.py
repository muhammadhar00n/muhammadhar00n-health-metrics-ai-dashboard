def analyze_sleep(data):
    avg_sleep_hours = sum(day['sleep_hours'] for day in data) / len(data)
    
    if avg_sleep_hours < 7:
        return {
            "suggestion": "Consider a consistent bedtime to improve sleep quality.",
            "avg_sleep_hours": avg_sleep_hours
        }
    return {
        "suggestion": "Sleep patterns are healthy.",
        "avg_sleep_hours": avg_sleep_hours
    }
