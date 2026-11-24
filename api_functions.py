import os

import requests

# The course API, which makes the draws
BASE_URL = "http://165.22.92.178:8080"


def get_draw(week):
    """Gets the draw of one week from the endpoint /getrand. The week is the seed."""
    url = BASE_URL + "/getrand"
    # THE WEEK MUST BE SENT AS THE SEED OF THE DRAW. WHICH QUERY PARAMETER DOES /getrand READ?
    params = {}
    # THE API WANTS THE KEY FROM .env IN A HEADER. ADD IT HERE
    headers = {}
    response = requests.get(url, params=params, headers=headers)
    # THE BODY OF THE RESPONSE IS JSON. TURN IT INTO A DICTIONARY BEFORE IT IS RETURNED
    draw = response
    return draw
