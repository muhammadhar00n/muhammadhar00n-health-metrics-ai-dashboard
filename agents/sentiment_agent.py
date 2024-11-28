from textblob import TextBlob

def analyze_sentiment(entries):
    sentiments = {"positive": 0, "negative": 0, "neutral": 0}
    
    for entry in entries:
        polarity = TextBlob(entry['entry']).sentiment.polarity
        if polarity > 0:
            sentiments['positive'] += 1
        elif polarity < 0:
            sentiments['negative'] += 1
        else:
            sentiments['neutral'] += 1
    
    total_entries = len(entries)
    return {
        "summary": {
            "positive": f"{(sentiments['positive'] / total_entries) * 100:.2f}%",
            "negative": f"{(sentiments['negative'] / total_entries) * 100:.2f}%",
            "neutral": f"{(sentiments['neutral'] / total_entries) * 100:.2f}%"
        }
    }
