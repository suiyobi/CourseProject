from common import write_to_file, get_js_soup, remove_script, process_text

# Change here
# company name
company_name = 'apple'

# Base url of job description page
description_base_url = 'https://jobs.apple.com'

# Base url of job directory page (where jobs are listed)
listing_base_url = 'https://jobs.apple.com/en-us/search?location=united-states-USA&page='


""" Scrape the job listings page

driver: chrome webdriver
num_pages: number of pages to scrape.
"""


def scrape_dir_page(driver, num_pages=2):
    job_links = []

    for page_number in range(1, num_pages):
        print('-'*20, 'Scraping job listing page number {}'.format(page_number), '-'*20)

        # execute js on webpage to load job listings on webpage and get ready to parse the loaded HTML
        soup = get_js_soup(listing_base_url + str(page_number), driver)
        # print(listing_base_url + str(page_number))
        # get list of all <div> of class 'name'
        # , class_='table--advanced-search__title'):
        for link_holder in soup.find_all('a', class_="table--advanced-search__title"):
            # print(link_holder)
            # exit()
            rel_link = link_holder['href']  # get url
            # url returned is relative, so we need to add base url

            job_links.append(description_base_url + rel_link)

    print('-'*20, 'Found {} job urls'.format(len(job_links)), '-'*20)
    return job_links


""" Scrape the job description page

job_description_url: url of the job description page
driver: chrome webdriver
"""


def scrape_job_page(job_description_url, driver):

    job_description_soup = get_js_soup(job_description_url, driver)
    print(job_description_url)
    job_description_soup = remove_script(
        job_description_soup).find('main', class_='main page-job-details')
    job_description = ''
    for span in job_description_soup.findAll("span"):
        job_description += span.text + ' '
    job_description = process_text(job_description)
    # job_description = process_text(
    #     job_description_soup.get_text(separator=' '))

    return job_description_url, job_description
