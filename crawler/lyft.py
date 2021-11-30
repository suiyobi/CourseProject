from common import write_to_file, get_js_soup, remove_script, process_text
from bs4 import BeautifulSoup
import time

# Change here
# company name
company_name = 'lyft'

# Base url of job description page
description_base_url = ''

# Base url of job directory page (where jobs are listed)
listing_base_url = 'https://www.lyft.com/careers'


""" Scrape the job listings page

driver: chrome webdriver
num_pages: number of pages to scrape.
"""
def scrape_dir_page(driver, num_pages = 5):
    job_links = []

    print ('-'*20,'Scraping job listing', '-'*20)

    driver.get(listing_base_url)
    time.sleep(1)

    # Something special we do for lyft: need to click to expand the accordion
    button = driver.find_element_by_css_selector('#openings > div > div > div.q480ss-0.eqWJQH > div:nth-child(28) > button')
    button.click()

    soup = BeautifulSoup(driver.execute_script('return document.body.innerHTML'), 'html.parser')
    link_holders = soup.findAll('a', title='Opens in a new tab.')

    for link_holder in link_holders: #get list of all <div> of class 'name'
        rel_link = link_holder['href'] #get url
        #url returned is relative, so we need to add base url
        job_links.append(description_base_url + rel_link)

    print ('-'*20,'Found {} job urls'.format(len(job_links)),'-'*20)
    return job_links

""" Scrape the job description page

job_description_url: url of the job description page
driver: chrome webdriver
"""
def scrape_job_page(job_description_url, driver):

    job_description_soup = get_js_soup(job_description_url, driver)
    job_description_soup = remove_script(job_description_soup).find('div', id='content')
    job_description = ''

    job_description = process_text(job_description_soup.get_text(separator=' '))

    return job_description_url, job_description
