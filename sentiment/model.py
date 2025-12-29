from transformers import pipeline

# Load Hugging Face pipeline
classifier = pipeline("sentiment-analysis")

def analyze_sentiment(text):
    result = classifier(text)[0]
    label = result['label']
    score = round(result['score'], 2)
    return {"sentiment": label, "confidence": score}
