import pandas as pd
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load CSV data
df = pd.read_csv("clothing_data.csv")


# Function to get chatbot response
def get_bot_response(user_text):
    user_text = user_text.lower()

    # 👋 Goodbye handling
    if user_text in ["quit", "bye", "goodbye"]:
        return "Goodbye! Nice to have been of service to you."

    found_answer = False
    response = "Sorry, i don't know that one, Try asking for something else."

    # Loop through CSV
    for index, row in df.iterrows():

        keywords_list = str(row["Keyword"]).split(',')

        for word in keywords_list:
            clean_word = word.strip().lower()

            if clean_word in user_text:
                response = row["Response"]
                found_answer = True
                break

        if found_answer:
            break

    return response


# 🌐 Chat API endpoint
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_text = data.get("message", "").lower()

    # 👋 Greeting handling
    if user_text in ["hi", "hello", "hey"]:
        return jsonify({
            "reply": "Hello there 👋 I am your Yeezy clothing assistant bot. Ask me anything!"
        })

    reply = get_bot_response(user_text)

    return jsonify({"reply": reply})


# 🚀 Run server
if __name__ == "__main__":
    print("Yzybot API is running...")
    app.run(debug=True)