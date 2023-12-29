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

def fill_missing_data(df):
    # Popülation sütununda eksik değerleri medyan ile doldurma
    df['Population'].fillna(df['Population'].median(), inplace=True)
    
    # Total_Tests, Total_Deaths, 
    # Cases_Active, Cases_Critical, Cases_Recovered 
    # sütununda eksik değerleri ortalama ile doldurma
    df['Total_Tests'].fillna(df['Total_Tests'].mean(), inplace=True)
    df['Total_Deaths'].fillna(df['Total_Deaths'].mean(), inplace=True)
    df['Cases_Active'].fillna(df['Cases_Active'].mean(), inplace=True)
    df['Cases_Critical'].fillna(df['Cases_Critical'].mean(), inplace=True)
    df['Cases_Recovered'].fillna(df['Cases_Recovered'].mean(), inplace=True)
    return df
    

def delete_row(df):
    #Continent sütün için 'None' ve 'NotAvailable' değerleri içeren satırları sil
    df[(pd.notna(df['Continent'])) & (df['Continent'] != 'NotAvailable')]
    return df

if __name__ == "__main__":
    get_json()
    
    covid19_json=get_json()
    df=get_data(covid19_json)
    
    fill_missing_data(df)
    
