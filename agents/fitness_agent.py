def analyze_fitness(data):
    total_steps = sum(day['steps'] for day in data)
    avg_steps = total_steps / len(data)
    
    if avg_steps < 10000:
        return {
            "suggestion": "Increase daily steps by 10% to improve health.",
            "avg_steps": avg_steps
        }
    return {
        "suggestion": "Maintain current activity level.",
        "avg_steps": avg_steps
    }
