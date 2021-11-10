
import json
from common import write_to_file, get_js_soup, remove_script, process_text, get_driver

# Change here
# company name
company_name = 'google'

# Base url of job description page
base_url = 'https://careers.google.com'

# Base url of job directory page (where jobs are listed)
dir_url = 'https://careers.google.com/jobs/results/'


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


#extracts all job description page urls from the Directory Listing Page
def scrape_dir_page(dir_url, driver):
    print ('-'*20,'Scraping directory page','-'*20)
    
    job_links = []

    #execute js on webpage to load job listings on webpage and get ready to parse the loaded HTML 
    soup = get_js_soup(dir_url, driver)

    # Change here
    for link_holder in soup.find_all('a',class_='gc-card'): #get list of all <div> of class 'name'
        rel_link = link_holder['href'] #get url
        #url returned is relative, so we need to add base url
        job_links.append(base_url+rel_link) 
    print ('-'*20,'Found {} job urls'.format(len(job_links)),'-'*20)
    return job_links


def scrape_job_page(job_description_url, driver):
    
    job_description_soup = get_js_soup(job_description_url, driver)
    job_description_soup = remove_script(job_description_soup).find('div', class_='gc-card__content')
    job_description = ''

    job_description = process_text(job_description_soup.get_text(separator=' '))

    return job_description_url, job_description
