from flask import Flask, render_template, request
from model import analyze_sentiment

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    sentiment_result = None
    input_text = ""
    if request.method == "POST":
        input_text = request.form.get("text")
        if input_text:
            sentiment_result = analyze_sentiment(input_text)
    return render_template("index.html", sentiment=sentiment_result, text=input_text)

if __name__ == "__main__":
    app.run(debug=True)
