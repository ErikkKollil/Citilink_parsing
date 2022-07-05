from bs4 import BeautifulSoup
import requests
import json
import lxml
# import pprint


def main():
    search = 'https://www.citilink.ru/catalog/videokarty/?pf=available.all%2Cdiscount.any%2Crating.any%2C9368_29nvidiad1d1geforced1rtxd13060ti&f=available.all%2Cdiscount.any%2Crating.any%2C9368_29nvidiad1d1geforced1rtxd13060ti%2C9368_29nvidiad1d1geforced1rtxd13060'
    resp = requests.get(search)
    soup = BeautifulSoup(resp.text, 'lxml')

    with open('1_all_html.html', 'w', encoding="utf-8") as f:
        f.write(soup.prettify())

    info(soup)


def info(soup):
    info_vc = []

    item_names = soup.find_all('div', class_='product_data__gtm-js product_data__pageevents-js ProductCardHorizontal js--ProductCardInListing js--ProductCardInWishlist')
    for item in item_names:
        info_vc.append(json.loads(item['data-params']))
    # with open('3_infovc.json', 'w') as file:
    #     json.dump(info_vc, file, indent=4, ensure_ascii=False)

    for el in info_vc:
        print('Код товара: ', el.get('id'),
              '| Наименование: ', el.get('shortName'),
              # ' | Бренд: ', el.get('brandName'),
              ' | Старая цена: ', el.get('price') if el.get('oldPrice') == 0 else el.get('oldPrice'),
              ' | Новая цена: ', el.get('price'),
              ' | Клубная цена: ', el.get('clubPrice'),
              ' | Скидка: ', 'нет' if el.get('oldPrice') == 0 else str(round(100 - (el.get('price')/(el.get('oldPrice'))*100), 1))+'%',
              sep='', end='\n')

    return print('\nThe process has been completed successfully!')  # pprint.pprint(info_vc)



if __name__ == '__main__':
    print('------------------Информация по видеокартам в Ситилинк (Воронеж) в наличии и под заказ------------------')
    main()
