
import json
from common import write_to_file, get_js_soup, remove_script, process_text, get_driver

# Change here
# company name
company_name = 'google'

# Base url of job description page
base_url = 'https://careers.google.com'

# Base url of job directory page (where jobs are listed)
dir_url = 'https://careers.google.com/jobs/results/?page='


def scrape():
    print('Scraping {}...'.format(company_name))
    
    driver = get_driver()

    # Scrape the job directory page
    job_links = scrape_dir_page(dir_url, driver)

    # Scrape each job description of all urls
    job_description_urls, job_descriptions = [], []
    tot_urls = len(job_links)

    for i,link in enumerate(job_links):
        print ('-'*20,'Scraping job url {}/{}'.format(i+1,tot_urls),'-'*20)
        
        job_description_url, job_description = scrape_job_page(link, driver)

        if job_description.strip() != '' and job_description_url.strip() != '':
            job_description_urls.append(job_description_url.strip())
            job_descriptions.append(job_description)

    driver.close()

    write_to_file(company_name, job_description_urls, job_descriptions)

    print('Scraping {} finished.'.format(company_name))


""" Scrape the job listings page

dir_url: url of the job listings page
driver: chrome webdriver
num_pages: number of pages to scrape.
"""
def scrape_dir_page(dir_url, driver, num_pages = 5):
    job_links = []

    for page_number in range(1, num_pages):
        print ('-'*20,'Scraping directory page number {}'.format(page_number),'-'*20)
    
        # execute js on webpage to load job listings on webpage and get ready to parse the loaded HTML 
        soup = get_js_soup(dir_url + str(page_number), driver)

        for link_holder in soup.find_all('a',class_='gc-card'): #get list of all <div> of class 'name'
            rel_link = link_holder['href'] #get url
            #url returned is relative, so we need to add base url
            job_links.append(base_url + rel_link)

    print ('-'*20,'Found {} job urls'.format(len(job_links)),'-'*20)
    return job_links

""" Scrape the job description page

dir_url: url of the job description page
driver: chrome webdriver
"""
def scrape_job_page(job_description_url, driver):
    
    job_description_soup = get_js_soup(job_description_url, driver)
    job_description_soup = remove_script(job_description_soup).find('div', class_='gc-card__content')
    job_description = ''

    job_description = process_text(job_description_soup.get_text(separator=' '))

    return job_description_url, job_description
