import requests

def translate_text(text):
    url = "https://translate.googleapis.com/translate_a/single"
    
    params = {
        "client": "gtx",
        "sl": "es",
        "tl": "en",
        "dt": "t",
        "q": text
    }

    response = requests.get(url, params=params)
    result = response.json()
    
    return result[0][0][0]