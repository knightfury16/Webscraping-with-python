from bs4 import BeautifulSoup
import requests
import datetime
import pytz
import json
from report import Report
import schedule
import time
from logger import Logger

# Creating a logger handler
logger = Logger.create_logger(__name__, 'INFO')

def job():

    logger.info("......STARTING DISTRICT DATA SYNC.....")

    try:
        # Requesting the site
        source = requests.get("https://corona-bd.herokuapp.com/district")

        # Creating a beautifulsoup object
        soup = BeautifulSoup(source.content, "lxml")

        # Finding the paragraph in soup object
        p = soup.find('p').text

        # Loads it in json
        data = json.loads(p)

        # Converting updated time string to datetime UTC+6
        str_dt = data['updated_on']

        dt = datetime.datetime.strptime(str_dt, "%a, %d %b %Y %H:%M:%S %Z")  # String to date

        utc_tz = pytz.timezone("UTC")  # UTC timezone

        dt = utc_tz.localize(dt)  # Localizing dt to UTC time

        dt_dhk = dt.astimezone(pytz.timezone("Asia/Dhaka"))  # Converting dt to dhaka time

        updated_time = dt_dhk.strftime("%a, %d %b %Y %I:%M:%S %p %Z")  # Converting to interested string

        # Searching through data to find Tangail
        for data in data["data"]:
            if data['name'] == "Tangail":
                # If present count is greater than prev_count send email
                if data['count'] > data['prev_count']:
                    Report.Email(data['count'], data['prev_count'], updated_time)
                else:
                    logger.info("No change in data of Tangail.")

    except Exception as e:
        logger.info("Could not connect...Check internet")


# def job():
#     logger.info("......STARTING DISTRICT DATA SYNC.....")
#     if get_data():

#         if old_data():
#             # Order matter
#             write_tday_data_json()
#             write_tday_data_csv()
#             Report.Email(F_PATH)
#         else:
#             logger.info("No new data")


# # schedule.every(2).hours.do(job)
schedule.every(1).minutes.do(job)
# # schedule.every().hour.do(job)
# # schedule.every().day.at("10:30").do(job)
# # schedule.every(5).to(10).minutes.do(job)
# # schedule.every().monday.do(job)
# # schedule.every().wednesday.at("13:15").do(job)
# # schedule.every().minute.at(":17").do(job)

# print("STARTING...")

while True:
    schedule.run_pending()
    time.sleep(1)

# job()
