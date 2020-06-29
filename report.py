import smtplib
import os
import json
from logger import Logger


class Report():
    """docstring for Report"""

    def sudo_func():
        logger = Logger.create_logger(__name__, "INFO")

        logger.info("This is from another module")

    def Email(count, prev_count, update_time):

        logger = Logger.create_logger(__name__, "INFO")

        EMAILL_ADDRESS = os.environ.get('USER_EMAIL')
        EMAIL_PASSWARD = os.environ.get('USER_PASSWARD')

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAILL_ADDRESS, EMAIL_PASSWARD)
            subject = 'Tangail Report from Python bot'
            body = f"Present count {count}, previous count {prev_count}."
            body += "\nIncrease of {} person.".format(int(count) - int(prev_count))
            body += "\n\nAs per {}".format(update_time)
            msg = f"Subject: {subject}\n\n{body}"
            smtp.sendmail(EMAILL_ADDRESS, 'suhaib16@student.sust.edu', msg)
            logger.info("Email Sent")
            # print(msg)
