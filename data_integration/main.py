# main.py

from fastapi import FastAPI
from agents.fitness_agent import analyze_fitness
from agents.sleep_agent import analyze_sleep
from agents.sentiment_agent import analyze_sentiment

app = FastAPI()

# Root route
@app.get("/")
async def read_root():
    return {"message": "Welcome to the Health Metrics API"}

# Mock dataset (you can replace this with API input)
mock_data = {
    "user_id": "12345",
    "metrics": [
        {"date": "2024-11-22", "steps": 8500, "heart_rate": 75, "sleep_hours": 6.5, "hrv": 45},
        {"date": "2024-11-21", "steps": 9500, "heart_rate": 72, "sleep_hours": 7.2, "hrv": 50}
    ],
    "journal_entries": [
        {"date": "2024-11-22", "entry": "I feel really anxious about the upcoming presentation."},
        {"date": "2024-11-21", "entry": "Had a great day today! Felt accomplished after all tasks."}
    ]
}

@app.get("/fitness")
async def get_fitness_insights():
    fitness_insights = analyze_fitness(mock_data['metrics'])
    return {"Fitness Insights": fitness_insights}

@app.get("/sleep")
async def get_sleep_insights():
    sleep_insights = analyze_sleep(mock_data['metrics'])
    return {"Sleep Insights": sleep_insights}

@app.get("/sentiment")
async def get_sentiment_insights():
    sentiment_insights = analyze_sentiment(mock_data['journal_entries'])
    return {"Sentiment Insights": sentiment_insights}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
