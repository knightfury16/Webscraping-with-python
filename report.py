import smtplib
import os
import json
from logger import Logger


class Report():
    """docstring for Report"""

    def sudo_func():
        logger = Logger.create_logger(__name__, "INFO")

        logger.info("This is from another module")

    def Email(reported_data):
        logger = Logger.create_logger(__name__, "INFO")

        # BD
        last_day_pos = reported_data['positive'][0]['last24']
        tot_pos = reported_data['positive'][0]['total']
        last_day_death = reported_data['death'][0]['last24']
        tot_death = reported_data['death'][0]['total']
        updated_time_BD = reported_data['updated_time_BD']

        # District/Tangail
        tan_td = reported_data['district'][0]['count']
        tan_prev = reported_data['district'][0]['prev_count']
        updated_time_dist = reported_data['district'][0]['updated_on']

        EMAILL_ADDRESS = os.environ.get('USER_EMAIL')
        EMAIL_PASSWARD = os.environ.get('USER_PASSWARD')

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAILL_ADDRESS, EMAIL_PASSWARD)
            subject = 'Report from Python bot'
            body = f"Positive, today {int(last_day_pos):,}, total positive {int(tot_pos):,}."
            body += f"\nDeath, today {last_day_death}, total death {int(tot_death):,}."
            body += f"\nAs per {updated_time_BD}"
            if reported_data['district'][0]['flag'] == 'yes':
                body += f"\n\nIn Tangail today's positive {tan_td}, previous day {tan_prev}."
                body += f"\nIncrease of {int(tan_td)-int(tan_prev)}."
            else:
                body += f"\n\nNo change in Tangail data today, present count {tan_td}"
            body += f"\nAs per {updated_time_dist}"
            msg = f"Subject: {subject}\n\n{body}"
            smtp.sendmail(EMAILL_ADDRESS, 'suhaib16@student.sust.edu', msg)
            logger.info("Email Sent")
            # print(msg)
