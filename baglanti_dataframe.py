import pandas as pd
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
    covid19_json = json.loads(data)
    return covid19_json

def get_data(covid19_json):
    #öncelikle boş bir liste oluşturuyoruz
    data_list=[]
    for response in covid19_json['response']:
        df={
            "Continent"   : response['continent'],
            "Country"     : response['country'],
            "Population"  : response['population'],
            "Total_Cases" : response['cases']['total'],
            "Total_Tests" : response['tests']['total'],
            "Total_Deaths": response['deaths']['total'],
            "Cases_Active": response['cases']['active'],
            "Cases_Critical":response['cases']['critical'],
            "Cases_Recovered": response['cases']['recovered']
            
        }
        #Liste üzerine sözlüğü ekleme
        data_list.append(df)    

    #DataFrame oluştur
    covid19_df=pd.DataFrame(data_list)
    return covid19_df

if __name__ == "__main__":
    get_json()
    covid19_json=get_json()
    get_data(covid19_json)
