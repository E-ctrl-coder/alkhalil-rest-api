from flask import Flask, request, jsonify

app = Flask(__name__)

def stub_parse(word: str) -> list[dict]:
    """
    Temporary stub that returns one fake hybrid parse.
    """
    return [{
        "source":           "hybrid_alkhalil",
        "segments":         [{"text": word, "type": "root"}],
        "pattern":          "فعل",
        "root_occurrences": 0,
        "example_verses":   []
    }]

@app.route('/analyze', methods=['GET', 'POST'])
def analyze():
    # accept GET for quick smoke tests
    if request.method == 'GET':
        w = request.args.get('word', '').strip()
    else:
        w = (request.get_json(silent=True) or {}).get('word', '').strip()

    if not w:
        return jsonify(error="Empty word"), 400

    # <<< STUBBED RESPONSE >>>
    return jsonify(stub_parse(w)), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
