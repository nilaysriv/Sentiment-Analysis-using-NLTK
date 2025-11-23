import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import statistics
import random

try:
    nltk.data.find('sentiment/vader_lexicon.zip')
except LookupError:
    nltk.download('vader_lexicon', quiet=True)

analyzer = SentimentIntensityAnalyzer()

negative_responses = [
    "I'm sorry to hear that. I'll make sure your concern is addressed.",
    "That sounds frustrating. How can I help?",
    "I apologize for the inconvenience."
]

positive_responses = [
    "That's great to hear!",
    "I'm glad you're having a good experience.",
    "Thanks for the positive feedback!"
]

neutral_responses = [
    "I see. Please tell me more.",
    "Interesting. Go on.",
    "Could you elaborate on that?"
]

def get_sentiment_label(score):
    if score >= 0.05:
        return "Positive"
    elif score <= -0.05:
        return "Negative"
    else:
        return "Neutral"

def main():
    print("Sentiment Chatbot (Type 'exit' to stop)")
    
    conversation_scores = []

    while True:
        user_text = input("User: ").strip()

        if user_text.lower() in ['exit', 'quit', 'bye']:
            break
        
        if not user_text:
            continue
        
        score = analyzer.polarity_scores(user_text)['compound']
        label = get_sentiment_label(score)

        print(f"→ Sentiment: {label}")
        
        conversation_scores.append(score)

        if label == "Negative":
            bot_reply = random.choice(negative_responses)
        elif label == "Positive":
            bot_reply = random.choice(positive_responses)
        else:
            bot_reply = random.choice(neutral_responses)

        print(f"Chatbot: \"{bot_reply}\"")
        print("-" * 20)

    print("\n=== FINAL RESULTS ===")
    
    if len(conversation_scores) > 0:
        average_score = statistics.mean(conversation_scores)
        overall_label = get_sentiment_label(average_score)
        print(f"Overall Conversation Sentiment: {overall_label}")

        first_msg = conversation_scores[0]
        last_msg = conversation_scores[-1]
        diff = last_msg - first_msg

        if diff > 0.2:
            print("Trend: Mood Improved.")
        elif diff < -0.2:
            print("Trend: Mood Worsened.")
        else:
            print("Trend: Mood Stable.")
    else:
        print("No messages were analyzed.")

if __name__ == "__main__":
    main()