import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

def jobScrapper():
    url = "https://www.indeed.com/jobs?q=php+developer&l=Remote&from=searchOnHP&vjk=4f4124b6ae711363"

    # try:
    response = requests.get(url)
    
    # except ChunkedEncodingError(e):
    #     return "HTTP error"

    soup = BeautifulSoup(response.text, 'html.parser')

    # tags = soup.find_all("a", class_="tw-w-full h-100 tw-absolute offer-link tw-z-10")
    title = soup.find_all(id="job_4f4124b6ae711363").getText()


    print(type(title))
    
    # job_dict = { }

    # for tag in tags:
    #     jobName = tag.get('title')
    #     jobLink = "https://jobgether.com"+tag.get('href')
    #     job_dict[jobName] = jobLink
        # print("https://jobgether.com/"+tag.get('href') + " Name of Job: " + tag.get('title'))

    # return job_dict

print(jobScrapper())