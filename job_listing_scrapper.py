import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

def jobScrapper():
    # url = "https://www.ghanajob.com/job-vacancies-search-ghana/?utm_source=site&utm_medium=link&utm_campaign=search_split&utm_term=all_jobs&f%5B0%5D=im_field_offre_metiers%3A31"
    # url = "https://www.jobsinghana.com/jobs/indexnew.php?device=d"
    # url = "https://www.jobberman.com.gh/jobs"
    url = "https://jobwebghana.com/jobs/"

    # try:
    response = requests.get(url)
    
    # except ChunkedEncodingError(e):
    #     return "HTTP error"

    soup = BeautifulSoup(response.text, 'html.parser')

    # tags = soup.find_all("a", class_="tw-w-full h-100 tw-absolute offer-link tw-z-10")
    # title = soup.find_all(id="job_4f4124b6ae711363").getText()
    workFrom = soup.find_all(id="titlo")


    print(workFrom)
    
    # job_dict = { }

    # for tag in tags:
    #     jobName = tag.get('title')
    #     jobLink = "https://jobgether.com"+tag.get('href')
    #     job_dict[jobName] = jobLink
        # print("https://jobgether.com/"+tag.get('href') + " Name of Job: " + tag.get('title'))

    # return job_dict

print(jobScrapper())