import os
import time
from seleniumbase import SB


def open_list(url):
    with SB(headed=True) as driver:
        driver.open(url)
        driver.type("//label[@class='input-layout-input-layout-_HVr_ input-layout-size-s-COZ10 input-layout-text-"
                     "align-left-U2OZJ width-width-12-_MkqF input-layout-stick-after-fLNbQ styles-root-Pmtd3']/"
                     "input[@data-marker='price/from']", "100000")
        driver.type("//label[contains(@class, 'input-layout-input-layout') and contains(@class, 'input-layout-size-s-"
                    "COZ10') and contains(@class, 'input-layout-text-align-left-U2OZJ') and contains(@class, "
                    "'width-width-12-_MkqF') and contains(@class, 'input-layout-stick-both-horizontal-Jx38b') "
                    "and contains(@class, 'styles-root-Pmtd3')]/input[@data-marker='price/to']", "200000")
        driver.click("//button[@data-marker='search-filters/submit-button']")
        time.sleep(5)
        current_url = driver.get_current_url()

        return current_url


city = 'staryy_oskol'
radius = 200
url = f'https://www.avito.ru/{city}/avtomobili?cd=1&localPriority=0&radius={radius}'


filter_url = open_list(url)

file_path = "filter.txt"

with open(file_path, 'w') as file:
    file.write(filter_url)

