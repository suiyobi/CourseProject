import google
import facebook
from common import get_driver

def scrape(scraper):
    print('Scraping {}...'.format(scraper.company_name))
    
    driver = get_driver()

    # Scrape the job directory page
    job_links = scraper.scrape_dir_page(driver)

    # Scrape each job description of all urls
    job_description_urls, job_descriptions = [], []
    tot_urls = len(job_links)

    for i,link in enumerate(job_links):
        print ('-'*20,'Scraping job url {}/{}'.format(i+1,tot_urls),'-'*20)
        
        job_description_url, job_description = scraper.scrape_job_page(link, driver)

        if job_description.strip() != '' and job_description_url.strip() != '':
            job_description_urls.append(job_description_url.strip())
            job_descriptions.append(job_description)

    driver.close()

    write_to_file(scraper.company_name, job_description_urls, job_descriptions)

    print('Scraping {} finished.'.format(scraper.company_name))

if __name__ == "__main__":
    scrape(google)
    scrape(facebook)
