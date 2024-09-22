import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

class JobScrapperClass:

    def __init__(self, job_dict = {},
                  filterWords = ['php', 'laravel', 'python', 'linux', 'remote'],
                  jobtogether_url = "https://jobgether.com/search-offers?utm_source=google&utm_medium=cpc&utm_campaign={campaign_name}&utm_id=21173927261&utm_term=find+jobs&utm_content=162302493033&gad_source=1&gclid=CjwKCAjwrcKxBhBMEiwAIVF8rGxAkXgplQ-RoZIdBlLUMCHY7HieeBW1OSxBQOldWflnim-lEQ2TTRoCc1UQAvD_BwE&jobReferences=62312ebc1cccbfccd84b40f9&locations=622a659af0bac38678ed1388",
                  dice_url = "https://www.dice.com/jobs?q=php%20developer&countryCode=US&radius=30&radiusUnit=mi&page=1&pageSize=20&filters.isRemote=true&language=en&eid=6957"):
        self.job_dict = job_dict
        self.filterWords = filterWords
        self.jobtogether_url = jobtogether_url
        self.dice_url = dice_url

    def scrapJobsfromJobtogether(self):
        url = self.jobtogether_url

        # try:
        response = requests.get(url)
        
        # except ChunkedEncodingError(e):
        #     return "HTTP error"

        soup = BeautifulSoup(response.text, 'html.parser')

        tags = soup.find_all("a", class_="tw-w-full h-100 tw-absolute offer-link tw-z-10")

        # print(type(tags))

        for tag in tags:
            jobName = tag.get('title')
            if tag.get('href') == '/#':
                continue
            
            jobLink = "https://jobgether.com"+tag.get('href')
            forwardJob = self.jobFilters(jobLink)

            if forwardJob == True:
                self.job_dict[jobName] = jobLink

        return self.job_dict 
    


    def scrapJobsfromDice(self):
        url = "https://www.businessghana.com/site/jobs"

        # try:
        response = requests.get(url)
        
        # except ChunkedEncodingError(e):
        #     return "HTTP error"

        soup = BeautifulSoup(response.text, 'html.parser')

        tags = soup.find_all("a", class_="disabled ember-view job-card-container__link job-card-list__title job-card-list__title--link")
        title = soup.find_all("title")
        product_elements = soup.select("a.card-title-link normal viewed")
        href = soup.find_all("h3", "listing-title")
        idfind = soup.find_all(id="ember131")


        return print(href)

        for tag in tags:
            jobName = tag.get('title')
            if tag.get('href') == '/#':
                continue
            
            jobLink = "https://jobgether.com"+tag.get('href')
            forwardJob = self.jobFilters(jobLink)

            if forwardJob == True:
                self.job_dict[jobName] = jobLink

        return self.job_dict 

    
    def jobFilters(self, jobUrl):
        forwardJob = False

        response = requests.get(jobUrl)


        soup = BeautifulSoup(response.text, 'html.parser')
        workFrom = soup.find(class_="text-decoration-underline").getText().lower()
        # print(jobUrl)
        jobDesc = soup.find(id="description_container").getText().lower()
        # return jobDesc
        count = 0

        if workFrom == 'anywhere':
            for filter in self.filterWords:
                if jobDesc.find(filter) > 0:
                    count += 1

        if count >= 0:
            forwardJob = True
            # print(jobUrl)

        return forwardJob

# job = JobScrapperClass()
# print(job.jobFilters('https://jobgether.com/offer/6604742a14f0e6c32ee0c183-backend-engineer-acceptance---remote-estonia-hungary-or-romania'))
# print(job.scrapJobs())