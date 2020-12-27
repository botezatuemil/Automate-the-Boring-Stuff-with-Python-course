from selenium import webdriver

browser = webdriver.Firefox()

browser.get('https://www.emag.ro/')
searchElem = browser.find_element_by_css_selector('#searchboxTrigger')
searchElem.send_keys('Iphone 11')
searchElem.submit()