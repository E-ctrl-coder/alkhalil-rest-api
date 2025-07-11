from flask import Flask, request, jsonify
from aratools_alkhalil.helper import analyze_with_alkhalil

app = Flask(__name__)

@app.route('/analyze', methods=['GET', 'POST'])
def analyze():
    # accept GET for quick smoke tests
    if request.method == 'GET':
        w = request.args.get('word', '').strip()
    else:
        j = request.get_json(silent=True) or {}
        w = j.get('word', '').strip()

    if not w:
        return jsonify(error="Empty word"), 400

    try:
        # call into your helper’s logic
        parses = analyze_with_alkhalil(w)
        return jsonify(parses), 200
    except Exception as e:
        return jsonify(error=str(e)), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
