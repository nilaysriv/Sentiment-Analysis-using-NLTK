import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import statistics

try:
    nltk.data.find('sentiment/vader_lexicon.zip')
except LookupError:
    nltk.download('vader_lexicon', quiet=True)
analyzer = SentimentIntensityAnalyzer()

def get_sentiment_label(score):
    if score >= 0.05:
        return "Positive"
    elif score <= -0.05:
        return "Negative"
    else:
        return "Neutral"

def main():
    print("Simple Sentiment Chatbot (Type 'exit' to stop)")
    conversation_scores = []
    while True:
        user_text = input("User: ").strip()
        if user_text.lower() in ['exit', 'quit', 'bye']:
            break
        score = analyzer.polarity_scores(user_text)['compound']
        label = get_sentiment_label(score)
        print(f"→ Sentiment: {label} (Score: {score})")
        conversation_scores.append(score)
        print("Chatbot: I see. Please continue.")
        print("-" * 20)

    print("\n=== FINAL RESULTS ===")
    if len(conversation_scores) > 0:
        average_score = statistics.mean(conversation_scores)
        overall_label = get_sentiment_label(average_score)
        print(f"Overall Sentiment: {overall_label} (Average: {average_score:.2f})")

        first_msg_score = conversation_scores[0]
        last_msg_score = conversation_scores[-1]        
        diff = last_msg_score - first_msg_score
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
