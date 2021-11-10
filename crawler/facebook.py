from common import write_to_file, get_js_soup, remove_script, process_text

# Change here
# company name
company_name = 'facebook'

# Base url of job description page
description_base_url = ''

# Base url of job directory page (where jobs are listed)
listing_base_url = ''


""" Scrape the job listings page

driver: chrome webdriver
num_pages: number of pages to scrape.
"""
def scrape_dir_page(driver, num_pages = 5):
    """Implement this"""
    pass

""" Scrape the job description page

job_description_url: url of the job description page
driver: chrome webdriver
"""
def scrape_job_page(job_description_url, driver):
    """Implement this"""
    pass
