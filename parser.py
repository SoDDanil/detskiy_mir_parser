import json
import requests
import pandas
import time


proxies = {
 'https':'http://29ChNA:PPdJJQ@176.53.143.215:8000',
 'https':'http://29ChNA:PPdJJQ@45.10.81.141:8000',
 'https':'http://29ChNA:PPdJJQ@45.10.80.242:8000',
 'https':'http://GEVJdh:5xmztz@45.144.170.206:8000'
}


headers = {
    'authority': 'api.detmir.ru',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://www.detmir.ru',
    'referer': 'https://www.detmir.ru/',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'x-requested-with': 'detmir-ui',
}


def get_data(url): #функция для отправки запроса и получения json файла
    response = requests.get(url= url, headers=headers, proxies=proxies,timeout=30)
    if (response.status_code == 200):
        data = response.json()
    else:
        print('Bad requests')
    return data

def collect_data(data_page): #функция для отбора нужных данных из json файла и сохранения их в csv файл
    products_data = data_page['items']
    for products in products_data:
        product_id = products['id']
        product_name = products['title']
        if (products['promo']==True):
            product_promo_price = products['price']['price']
            product_price= products['old_price']['price']
        else:
            product_promo_price='None'
            product_price = products['price']['price']
        product_url = products['link']['web_url']
        data_city = products['available']['offline']['region_iso_codes']
        product_city = ' '
        for city in data_city:
            if (city == 'RU-MOW'):
                product_city = 'Moscow '
            if (city == 'RU-SPE'):
                product_city+= ' Spb '
        if (product_city == ' '):
            product_city = 'None'
        data_product = pandas.DataFrame([[product_id,product_name,product_price,product_city,product_promo_price,product_url]])
        data_product.to_csv('itog.csv', mode = 'a', index=False,header = False,encoding='utf-16', sep = '|')
    



        
    

def main():
    
    data_product = pandas.DataFrame([], columns=['id_product','name','price','city','promo_price','URL'])
    data_product.to_csv('itog.csv', mode = 'w', index=False,encoding='utf-16', sep = '|')
    url = 'https://api.detmir.ru/v2/products?filter=categories[].alias:myagkie_igrushki;promo:false;withregion:RU-MOW&expand=meta.facet.ages.adults,meta.facet.gender.adults,webp&meta=*&limit=30&offset=0&sort=popularity:desc'
    data = get_data(url)
    count_products = data['meta']['length']
    print(count_products)
    for offset in range(0,count_products,30):
        print('-----------------------------------------------')
        print(offset)
        url_itog = f'https://api.detmir.ru/v2/products?filter=categories[].alias:myagkie_igrushki;promo:false;withregion:RU-MOW&expand=meta.facet.ages.adults,meta.facet.gender.adults,webp&meta=*&limit=30&offset={offset}&sort=popularity:desc'
        data_page = get_data(url_itog)
        collect_data(data_page)
        

if __name__=='__main__':
    main()


