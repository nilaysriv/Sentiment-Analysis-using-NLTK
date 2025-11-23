# Sentiment Analysis Chatbot

A lightweight, procedural Python chatbot that performs sentiment analysis on user interactions. This project implements **Conversation-Level Analysis**, **Statement-Level Analysis**, and the **Mood Trend**.

## How to Run

### Prerequisites

  * Python 3.x
  * `nltk` library

### Setup & Execution (Linux/Fedora)

1.  **Install Python:**

    ```bash
    sudo dnf install python3-pip python3-virtualenv git

    ```

2.  **Clone the Repository**

    ```bash
    https://github.com/nilaysriv/Sentiment-Analysis-using-NLTK
    cd Sentiment-Analysis-using-NLTK
    ```
3.  **Install Dependencies:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate.fish
    pip install -r requirements.txt
    ```
4.  **Run the script:**

    ```bash
    python bot.py
    ```

-----

## Tech Stack

  * **Language:** Python 3 (Script-based approach).
  * **Library:** `NLTK` (Natural Language Toolkit).
  * **Model:** **VADER** (Valence Aware Dictionary and sEntiment Reasoner) : Rule-based model optimized for social media and conversational text. It is efficient, requires no training data, and handles emoticons/capitalization natively.

-----

## Sentiment Logic

The chatbot uses a linear procedural approach to process input in real-time.

### 1\. Scoring (Statement-Level)

Every user message is passed to the VADER analyzer, which returns a **Compound Score** between `-1.0` (Negative) and `1.0` (Positive).

  * **Positive:** Score \> 0.05
  * **Negative:** Score \< -0.05
  * **Neutral:** Between -0.05 and 0.05

### 2\. Overall Sentiment

All sentiment scores are stored in a list (`conversation_scores`). When the conversation ends, the script calculates the **mathematical mean (average)** of all scores to determine the overall tone of the session.

### 3\. Mood Trend 

The bot detects the shift in mood by comparing the **First Message** against the **Last Message**:

  * **Improvement:** If (Last Score - First Score) \> 0.2
  * **Worsening:** If (Last Score - First Score) \< -0.2
  * **Stable:** If the difference is negligible.

-----

## Status of Implementation

**Status: COMPLETED**

  * Calculates the average sentiment upon exit.
  * Displays `→ Sentiment: [Label]` immediately after every input.
  * Successfully identifies if the user's mood improved or worsened from the start of the chat.
