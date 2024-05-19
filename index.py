from auto_mail import send_email
import jobScrapperClass
import json
import schedule
import time


def runJobListingAppAuto():
    job = jobScrapperClass.JobScrapperClass()
    jobListings = job.scrapJobs()
    message = json.dumps(jobListings)

    # print(message)

    send_email(text_message=message)
    # return "success!"

runJobListingAppAuto()

# schedule.every(5).minutes.do(runJobListingAppAuto)
# while True:
 
#     # Checks whether a scheduled task 
#     # is pending to run or not
#     schedule.run_pending()
#     time.sleep(1)