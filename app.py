from flask import Flask, request, jsonify
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    prompt = data.get("prompt", "")
    
    if not prompt:
        return jsonify({"reply": "Te rog scrie o întrebare."})

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Ești un asistent educațional care explică clar concepte din informatică și răspunde elevilor într-un mod prietenos."},
                {"role": "user", "content": prompt}
            ]
        )
        reply = response["choices"][0]["message"]["content"]
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"reply": f"Eroare: {str(e)}"})
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render va furniza PORT
    app.run(host="0.0.0.0", port=port)
