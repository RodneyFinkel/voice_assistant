from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def google_search(search_term):
    browser = webdriver.Chrome()
    browser.get('http://www.google.com')
    search = browser.find_element_by_name('q')
    search.send_keys(search_term)
    search.send_keys(Keys.RETURN)
    
google_search('Fender Stratocaster HSS')   