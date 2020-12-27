from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://automatetheboringstuff.com')
# elem = browser.find_element_by_css_selector('.main > div:nth-child(1) > ul:nth-child(21) > li:nth-child(1) > a:nth-child(1)') only one thing matches

# elems = browser.find_elements_by_css_selector('p') find all paragraphs
# print(len(elems))

# browser.back()
# browser.forward()
# browser.refresh()
# browser.quit()

elem = browser.find_element_by_css_selector('.main > div:nth-child(1) > ul:nth-child(21) > li:nth-child(1) > a:nth-child(1)')
elem.click()
newElem = browser.find_element_by_css_selector('p.noindent:nth-child(3)')
print(newElem.text)

# newElem = browser.find_element_by_css_selector('html') copy all text
# print(newElem.text) print all text of the page

