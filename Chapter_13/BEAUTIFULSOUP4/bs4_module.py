import bs4
import requests

'''
res = requests.get('https://www.emag.ro/telefon-mobil-apple-iphone-11-64gb-black-mwlt2rm-a/pd/D89ZX6BBM/?ref=others_also_viewed_1_4&provider=rec&recid=rec_43_59010a848a131ddd5cd5b25dba1d375967aabd2044e56e26f102fe0b95a926dd_1605378777&scenario_ID=43')
soup = bs4.BeautifulSoup(res.text, 'html.parser') # the code for parsing html
elems = soup.select('#page-skin > div.container > div > div:nth-child(2) > div.col-sm-5.col-md-7.col-lg-7 > div > div > div.col-sm-12.col-md-6.col-lg-5 > form > div.product-highlight.product-page-pricing > div:nth-child(1) > div > div.w-50.mrg-rgt-xs > p.product-new-price')
print(elems[0].text.strip()) # show only price
'''

def getPrice(productURL):
    res = requests.get(productURL)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#page-skin > div.container > div > div:nth-child(2) > div.col-sm-5.col-md-7.col-lg-7 > div > div > div.col-sm-12.col-md-6.col-lg-5 > form > div.product-highlight.product-page-pricing > div:nth-child(1) > div > div.w-50.mrg-rgt-xs > p.product-new-price')
    return elems[0].text.strip()

price = getPrice('https://www.emag.ro/telefon-mobil-apple-iphone-11-64gb-black-mwlt2rm-a/pd/D89ZX6BBM/?ref=others_also_viewed_1_4&provider=rec&recid=rec_43_59010a848a131ddd5cd5b25dba1d375967aabd2044e56e26f102fe0b95a926dd_1605378777&scenario_ID=43')
print('The price is ' + price)




