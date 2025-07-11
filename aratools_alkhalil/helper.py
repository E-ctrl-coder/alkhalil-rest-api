# aratools_alkhalil/helper.py

import requests

# Replace this with your actual Alkhalil‐REST service URL:
# e.g. "https://alkhalil-rest-api.onrender.com/analyze"
ALKHALIL_URL = "https://alkhalil-rest-api.onrender.com/analyze"

# (connect timeout, read timeout)
TIMEOUT = (5, 30)

def analyze_with_alkhalil(word: str) -> list[dict]:
    """
    Send `word` to the remote Alkhalil REST API and return all parses.
    If the request times out reading, returns an empty list.
    """
    try:
        # we use GET so we can smoke‐test in a browser
        resp = requests.get(ALKHALIL_URL, params={"word": word}, timeout=TIMEOUT)
        resp.raise_for_status()
        return resp.json()
    except requests.Timeout:
        # remote service took too long → skip hybrid
        return []
    except requests.RequestException:
        # for any other HTTP error, bubble up
        raise
