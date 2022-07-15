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

cookies = {
    'ab2_90': 'ab2_90old90',
    'ab2_33': 'ab2_33new33',
    'ab2_50': '44',
    'ab3_75': 'ab3_75old75',
    'ab3_33': 'ab3_33new17',
    'ab3_20': 'ab3_20_20_0',
    'cc': '0',
    'is_old_search': '1',
    '_gcl_au': '1.1.2129306232.1654437970',
    '_ym_d': '1654437970',
    '_ym_uid': '1654437970510842893',
    'tmr_lvid': 'c09afe69ba488637600bbf3363cee223',
    'tmr_lvidTS': '1654437970173',
    '_ga': 'GA1.2.1680235733.1654437971',
    'auid': '74468972-5ecb-4835-a2a1-a208ec7ffe34',
    '_gaexp': 'GAX1.2.rF6aGfQwQPiBEWNbZr-EZQ.19193.1!8MwGXf_UQwWf1g2n0sBLCw.19243.x337',
    'advcake_track_id': '833615a9-3207-0076-77a3-b4716ce4c21d',
    'advcake_session_id': '62e49c38-1500-8291-7ead-51be97d5be6b',
    'uid': 'X6NyEmLQJFgtPbewBHz5Ag==',
    '_ym_isad': '2',
    '_ym_visorc': 'w',
    '_sp_ses.2b21': '*',
    '_gid': 'GA1.2.2087499773.1657807964',
    'JSESSIONID': '773db537-ea19-4953-a365-e201cbc6ed7b',
    'detmir-cart': '04041287-6d11-4b00-84ac-fead1299875c',
    'srv_id': 'cubic-front02-prod',
    'dm_s': 'L-773db537-ea19-4953-a365-e201cbc6ed7b|kH04041287-6d11-4b00-84ac-fead1299875c|Vj74468972-5ecb-4835-a2a1-a208ec7ffe34|gqcubic-front02-prod|qacb8ef79e-3cdc-48f6-835d-559da3d5a8e5|RK1657807964053#dTJXs5XiUfElLyzn1ZTFplzFwssLUn5N6SXxTz4ZhYI',
    'qrator_msid': '1657809165.096.d8m4T9lseUawtHbG-kg0n93orvf6hrh49ra4cocqor11nlhai',
    '_gat': '1',
    '_gat_test': '1',
    'geoCityDMCode': '7700000000000',
    'geoCityDMIso': 'RU-MOW',
    'geoCityDM': '%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%20%D0%B8%20%D0%9C%D0%BE%D1%81%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%B0%D1%8F%20%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C',
    'mindboxDeviceUUID': 'e8cf9185-1134-4557-86a7-5e4f7bd8d3a3',
    'directCrm-session': '%7B%22deviceGuid%22%3A%22e8cf9185-1134-4557-86a7-5e4f7bd8d3a3%22%7D',
    'cto_bundle': 'xpe9nV80TGMlMkJ5N0FRTUduMTdpVTZubnJFQlRvcUR6ZFdsQzFqRDIlMkIyZHhKTnZNdSUyRmhzbnVtU0lhR3ozN0wyTk1JU2F0Vjk4b1FsYW5YM1UzJTJGc3kwRjZTTW01dVNYQ3RPVTlxZGZCSTRJOFFReTJoUExacUtqWkE1aHFKUEJ4ZktWaFZLSXFXaEN1eHg0UExiVVEyVTkzdXdRQSUzRCUzRA',
    '_sp_id.2b21': '345d9887-e83b-4dc9-8d46-beba14bed849.1654437971.18.1657809273.1657103406.f8baa0f5-e2d5-47b7-b729-3e9b544afee1',
    'tmr_reqNum': '153',
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
    response = requests.get(url= url, cookies=cookies, headers=headers, proxies=proxies,timeout=30)
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
        data_product.to_csv('itog.csv', mode = 'a', index=False,encoding='utf-16', sep = '|')
    



        
    

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


