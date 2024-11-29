from fastapi import FastAPI
import requests

# Initialize FastAPI app
app = FastAPI()

# Example agent URLs (replace with actual running APIs)
sentiment_url = 'http://127.0.0.1:8000/sentiment'
sleep_url = 'http://127.0.0.1:8000/sleep'
fitness_url = 'http://127.0.0.1:8000/fitness'

# Fetch data from the APIs
def fetch_agent_data(url):
    try:
        response = requests.get(url, timeout=30)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Failed to fetch data from {url} (status code: {response.status_code})"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Error fetching data from {url}: {e}"}

# Aggregate insights
def aggregate_insights(sentiment, sleep, fitness):
    combined_feedback = []

    if float(sentiment['Sentiment Insights']['summary']['negative'].replace('%', '')) > 50:
        combined_feedback.append("Your sentiment is more negative. Try focusing on positivity.")
    
    if sleep['Sleep Insights']['avg_sleep_hours'] < 7:
        combined_feedback.append(f"Your average sleep is {sleep['Sleep Insights']['avg_sleep_hours']} hours. Aim for at least 7-8 hours to improve health.")

    if fitness['Fitness Insights']['avg_steps'] < 10000:
        combined_feedback.append(f"Your average daily steps are {fitness['Fitness Insights']['avg_steps']}. Consider increasing by 10% for better health.")
    
    combined_feedback.append(sleep['Sleep Insights']['suggestion'])
    combined_feedback.append(fitness['Fitness Insights']['suggestion'])
    
    return {"Personalized Insights": "\n".join(combined_feedback)}

@app.get("/aggregate")
async def get_aggregated_insights():
    # Fetch data from all agents
    sentiment_data = fetch_agent_data(sentiment_url)
    sleep_data = fetch_agent_data(sleep_url)
    fitness_data = fetch_agent_data(fitness_url)

    # Validate responses
    if "error" in sentiment_data or "error" in sleep_data or "error" in fitness_data:
        return {"error": "Failed to fetch data from one or more agents."}

    # Aggregate and return insights
    return aggregate_insights(sentiment_data, sleep_data, fitness_data)

# Run using: uvicorn aggregate_insights:app --reload
