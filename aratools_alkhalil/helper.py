# arabic-miracle-api/aratools_alkhalil/helper.py

def analyze_with_alkhalil(word: str) -> list[dict]:
    """
    LOCAL STUB: returns one fake hybrid parse so your UI never sees empty JSON.
    """
    return [{
        "source":           "hybrid_alkhalil",
        "segments":         [{"text": word, "type": "root"}],
        "pattern":          "فعل",
        "root_occurrences": 0,
        "example_verses":   []
    }]
