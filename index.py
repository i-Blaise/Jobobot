from auto_mail import send_email
import jobScrapperClass
import json
import schedule
import time


def runJobListingAppAuto():
    job = jobScrapperClass.JobScrapperClass()
    jobListings = job.scrapJobs()


    html_content = "<html> <body> <ul>"
    for key, value in jobListings.items():
        html_content += f"<li>{key}: {value}</li>"
    html_content += "</ul> </body> </html>"
    # print(type(jobListings))

    send_email(html=True, html_message=html_content)

runJobListingAppAuto()

# schedule.every().day.at("10:30").do(runJobListingAppAuto)
# schedule.every(5).minutes.do(runJobListingAppAuto)
# while True:
    # Checks whether a scheduled task 
    # is pending to run or not
    # schedule.run_pending()
    # time.sleep(1)