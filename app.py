import json
import criteria
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/score_essay", methods=["POST"])
def score_essay():
    question = request.form.get('question')
    essay = request.form.get('essay')
    
    user_content = json.dumps({
        "question": question,
        "answer": essay
    })

    output = criteria.score(user_content)
    
    return jsonify(output)

if __name__ == "__main__":
    app.run(port=8092, debug=True)



