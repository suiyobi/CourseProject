from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import re 
import time


""" Returns a chrome web driver

create a webdriver object and set options for headless browsing
"""
def get_driver():
    options = Options()
    options.headless = False
    options.add_argument('--log-level=1')
    options.add_argument('enable-javascript')
    return webdriver.Chrome('../chromedriver.exe', options=options)


""" Write to file 

Write link and text to a file
"""
def write_to_file(company_name, description_urls, descriptions):
    description_urls_file = '{}_description_urls.txt'.format(company_name)
    descriptions_file = '{}_descriptions.txt'.format(company_name)

    write_lst(description_urls, description_urls_file)
    write_lst(descriptions, descriptions_file)


"""Write to file in line separated style

Write content to line separated files
"""
def write_lst(lst, file_):
    with open(file_,'w') as f:
        for l in lst:
            f.write(l)
            f.write('\n')

""" Returns a soup object

uses webdriver object to execute javascript code and get dynamically loaded webcontent
"""
def get_js_soup(url, driver):

    driver.get(url)
    """"Dumb way to wait for page to load. We should look into using wait and expected_conditions"""
    time.sleep(1)
    res_html = driver.execute_script('return document.body.innerHTML')

    # beautiful soup object to be used for parsing html content
    soup = BeautifulSoup(res_html,'html.parser') 
    return soup


""" Removes script from html

Sometimes the text extracted HTML webpage may contain javascript code and some style elements. 
This function removes script and style tags from HTML so that extracted text does not contain them.
"""
def remove_script(soup):
    for script in soup(["script", "style"]):
        script.decompose()
    return soup


""" Process text by converting encoding and strip whitespaces
"""
def process_text(text):
    # removes non-ascii characters
    text = text.encode('ascii',errors='ignore').decode('utf-8')      
    # repalces repeated whitespace characters with single space
    text = re.sub('\s+',' ',text)       
    return text

