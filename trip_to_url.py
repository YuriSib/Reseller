import time
from seleniumbase import SB
from bs4 import BeautifulSoup


def save_in_txt(list_):
    with open("id_list.txt", "w") as file:
        for item in list_:
            file.write(str(item) + "\n")


def trip(filter_url):
    with SB(headed=True) as driver:
        driver.open(filter_url)
        html_content = driver.get_page_source()
        soup = BeautifulSoup(html_content, 'lxml')
        list_advertisement = soup.find_all('div', {'data-marker': 'item'})
        item_id_list = []
        for advertisement in list_advertisement:
            item_id = advertisement['data-item-id']
            item_id_list.append(item_id)

        with open("id_list.txt", "r") as file:
            document = file.read()

        set(item_id_list) - set(document)
        save_in_txt(item_id_list)

    return list_advertisement


url = 'https://www.avito.ru/staryy_oskol/avtomobili?cd=1&f=ASgCAgECAUXGmgwbeyJmcm9tIjoxMDAwMDAsInRvIjoyMDAwMDB9' \
      '&radius=200&searchRadius=200'
trip(url)





