from transformers import pipeline
import torch

# Initialize the pipeline once, using CPU to avoid MPS issues
classifier = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english",
    device="cpu"  # Explicitly use CPU
)
def analyze_sentiment(text):
    classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
    result = classifier(text)[0]
    label = result['label']
    print(label)
    score = result['score']
    response = {
        'POSITIVE': f"You seem happy! 😊 What's making your day great? (Confidence: {score:.1%})",
        'NEGATIVE': f"Sounds like you're feeling down. 😔 Want to share more? (Confidence: {score:.1%})"
    }.get(label, "Hmm, neutral vibes! What's on your mind?")
    return {'label': label, 'score': score, 'response': response}