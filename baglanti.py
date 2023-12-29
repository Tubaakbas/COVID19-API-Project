import http.client
import json
from config import COVID19_API_KEY 

def get_json():
    #HTTP bağlantısı oluşutrma
    conn = http.client.HTTPSConnection("covid-193.p.rapidapi.com")

    #HTPP isteğinin başlıklarını belirleme
    headers = {
        'X-RapidAPI-Key': COVID19_API_KEY,
        'X-RapidAPI-Host': "covid-193.p.rapidapi.com"
    }

    # İlk isteği gönder
    conn.request("GET", "/statistics", headers=headers)

    # Yanıtı al
    res = conn.getresponse()

    #HTTP yanıtını okuma ve Unicode formatına çevirme
    data = res.read().decode("utf-8")

    #JSON formatına çevirme
    covid19_data = json.loads(data)
    return covid19_data

if __name__ == "__main__":
    get_json()
