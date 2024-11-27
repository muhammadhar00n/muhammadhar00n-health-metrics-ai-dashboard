from fastapi import FastAPI
import pandas as pd

app = FastAPI()

# Mock dataset
data = {
    "user_id": "12345",
    "metrics": [
        {"date": "2024-11-22", "steps": 8500, "heart_rate": 75, "sleep_hours": 6.5, "hrv": 45},
        {"date": "2024-11-21", "steps": 9500, "heart_rate": 72, "sleep_hours": 7.2, "hrv": 50}
    ]
}

@app.get("/normalize_data")
def normalize_data():
    # Convert metrics to DataFrame
    df = pd.DataFrame(data["metrics"])

    # Normalize heart rate (example scaling)
    df['normalized_heart_rate'] = (df['heart_rate'] - df['heart_rate'].min()) / (
            df['heart_rate'].max() - df['heart_rate'].min())

    # Add more normalization or calculations if needed
    response = df.to_dict(orient="records")
    
    return {"user_id": data["user_id"], "normalized_metrics": response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
