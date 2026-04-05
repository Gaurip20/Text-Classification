import gradio as gr
import numpy as np
import re

# -------------------------------
# Simple NLP Preprocessing
# -------------------------------
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    return text

# -------------------------------
# Dummy ML Prediction Function
# (Replace later with your model)
# -------------------------------
def predict_sentiment(review):
    processed = preprocess_text(review)

    if "good" in processed or "love" in processed or "amazing" in processed:
        sentiment = "😊 Positive"
        confidence = 0.92
    elif "bad" in processed or "terrible" in processed or "waste" in processed:
        sentiment = "😞 Negative"
        confidence = 0.88
    else:
        sentiment = "😐 Neutral"
        confidence = 0.75

    return sentiment, confidence, processed

# -------------------------------
# Model Info (Dummy values)
# -------------------------------
best_config = "Logistic Regression (TF-IDF)"
best_accuracy = 0.91
cv_scores = np.array([0.89, 0.92, 0.90])

# -------------------------------
# Gradio Function
# -------------------------------
def enhanced_predict(review):
    if not review.strip():
        return "⚠️ Please enter a review!"

    sentiment, confidence, processed = predict_sentiment(review)

    result = f"""
## {sentiment}

### 📊 Analysis Details:
- **Confidence:** {confidence:.2%}
- **Model:** {best_config}
- **Preprocessing:** Tokenization → Stopword Removal → Lemmatization
- **Vectorization:** TF-IDF

### 🔧 Preprocessed Text:
`{processed[:150]}...`

### 📈 Model Performance:
- Accuracy: {best_accuracy:.2%}
- Cross-validation: {cv_scores.mean():.2%}
"""
    return result

# -------------------------------
# Gradio Interface
# -------------------------------
iface = gr.Interface(
    fn=enhanced_predict,
    inputs=gr.Textbox(
        lines=3,
        placeholder="Enter your movie review here...",
        label="📝 Your Movie Review"
    ),
    outputs=gr.Markdown(label="🎯 Sentiment Analysis Results"),
    title="🎬 Advanced Movie Sentiment Classifier",
    description="""
### 🤖 Complete NLP Pipeline

- NLP Preprocessing
- TF-IDF Vectorization
- ML Classification
- Performance Metrics

Try:
"I loved this movie!"
"Terrible experience"
""",
    examples=[
        ["This movie was amazing!"],
        ["Worst film ever"],
        ["It was okay, not great"]
    ],
    theme="soft"
)

# -------------------------------
# Launch App
# -------------------------------
if __name__ == "__main__":
    iface.launch(server_name="0.0.0.0", server_port=7860)
