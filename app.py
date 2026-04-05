# Enhanced Gradio app with ALL features
def enhanced_predict(review):
    """Enhanced prediction for Gradio"""
    if not review or review.strip() == "":
        return "⚠️ Please enter a review!"
    
    # Get prediction
    sentiment, confidence, processed = predict_sentiment(review)
    
    # Create detailed output
    result = f"""## {sentiment}

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

# Create enhanced interface
enhanced_iface = gr.Interface(
    fn=enhanced_predict,
    inputs=gr.Textbox(
        lines=3,
        placeholder="Enter your movie review here...",
        label="📝 Your Movie Review"
    ),
    outputs=gr.Markdown(label="🎯 Sentiment Analysis Results"),
    title="🎬 Advanced Movie Sentiment Classifier",
    description="""
    ### 🤖 Complete NLP Pipeline with Machine Learning
    
    **This app demonstrates:**
    - ✅ NLP Preprocessing (Tokenization, Stopwords, Lemmatization)
    - ✅ Text Vectorization (TF-IDF)
    - ✅ Machine Learning Classification (Logistic Regression)
    - ✅ Model Evaluation Metrics
    
    **Try these examples:**
    - "I absolutely loved this film! The acting was superb."
    - "Terrible movie, complete waste of time and money."
    - "Good but not great, some scenes were too long."
    """,
    examples=[
        ["This movie was absolutely fantastic! I loved every moment."],
        ["Terrible acting and boring storyline. Complete waste of time."],
        ["Amazing visual effects and great performances from the cast!"],
        ["Not worth watching. Poor direction and weak script."]
    ],
    theme="soft"
)

print("\n" + "="*60)
print("🚀 LAUNCHING COMPLETE NLP APPLICATION")
print("="*60)
print("\n📱 Features included:")
print("   ✅ Tokenization")
print("   ✅ Stopword Removal")
print("   ✅ Lemmatization")
print("   ✅ TF-IDF Vectorization")
print("   ✅ ML Classification")
print("   ✅ Performance Metrics")
print("\n🌐 Generating public link...")

enhanced_iface.launch(share=True)
