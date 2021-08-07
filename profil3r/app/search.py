import requests

# If a request takes more than 5 seconds to respond, it raises an error
TIMEOUT = 5

# GET request
def search_get(url):
    try:
        r = requests.get(url, timeout=TIMEOUT, allow_redirects=True)
    except Exception as e:
        return
    return r

# POST request
def search_post(url):
    try:
        r = requests.post(url, timeout=TIMEOUT, allow_redirects=True)
    except Exception as e:
        return
    return r

# HEAD request
def search_head(url):
    try:
        r = requests.head(url, timeout=TIMEOUT, allow_redirects=True)
    except Exception as e:
        return
    return r