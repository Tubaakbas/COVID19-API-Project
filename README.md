## Proje Adı:

COVID-19 API PROJECT

## Açıklama:

Bu proje, COVID-19 istatistiklerini çekmek için Rapid API kullanılarak oluşturulmuştur.

## Kurulum:

1. Rapid API sitesinde üye olun ve API anahtarınızı alın. Bunun için https://rapidapi.com/hub linke tıklayabilirsin.

2. Search for APIs arama butonuna tıklayarak COVID-19 yazabilirsin. https://rapidapi.com/api-sports/api/covid-193

3. Searh endpoints->Statistics'e tıklayarak tüm ülkeler için tüm güncel istatistiklerin getirilmesi için açılan kod penceresinden python->http.client 'e tıklayabilirsin.Python kodunu al ve kendi projene entegre et.

4. Gerekli kütüphaneleri yüklemek için:
   import http.client (https://docs.python.org/3/library/http.client.html)
   import json
   import pandas as pd

5. Python kodunu çalıştırarak COVID-19 istatistiklerini çekebilirsiniz.

6. Python 3.10.8 sürümü kullanılmıştır.

## Kullanım:

1. API anahtarınızı script içinde belirtin.
2. HTTP bağlantısını oluşturun ve isteği gönderin.
3. Alınan JSON yanıtını analiz edin ve istediğiniz verilere erişin.
4. Elde ettiğiniz verilerle istediğiniz işlemleri gerçekleştirin.

## Örnek Kod:

import http.client

import json

conn = http.client.HTTPSConnection("covid-193.p.rapidapi.com")

headers = {
'X-RapidAPI-Key': "\*\*\*\*",
'X-RapidAPI-Host': "covid-193.p.rapidapi.com"
}

conn.request("GET", "/statistics", headers=headers)

res = conn.getresponse()

data = res.read().decode("utf-8")

covid19_data = json.loads(data)

covid19_data

Bu adımları gerçekleştirdiğinde json formatında bir kod göreceksin :)

## Sonuçlar:

- API Key kullanılarak JSON formatında veri çekildi.

- 'Continent', 'Country', 'Population', 'Total_Cases','Total_Tests', 'Total_Deaths', 'Cases_Active', 'Cases_Critical', 'Cases_Recovered': sütun bilgilerini içeren covid19_df isimli bir veri seti oluşturuldu.

- Oluşturulan veri setinde eksik veriler dolduruldu.

- Pandas ayarlarını kullanarak bilimsel gösterimi kapatıldı.

- Veri Analizinin daha güzel sonuçlar getirebilmesi için filtreleme işlemleri yapıldı.

- Veri Analizi gerçekleştirildi.

## İletişim:

Soruların veya önerilerin için bana mail adresimden ulaşabilirsin -> tubakbass0@gmail.com
