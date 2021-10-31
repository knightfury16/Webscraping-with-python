# Webscraping-with-python

Scraping the corona virus data of Bangladesh from the web and finding the result of a particular district and sending email to the user.
# Description

Used the ``BeautifulSoup`` library of python to scrape the web to get the *Corona Virus* data published by Bangladesh Government daily. Parsed through the data and find a particular district data and compare it to the previous day data. If there is a change in the data, the user gets notified by email.

Ran the script in [``Heroku``](https://www.heroku.com/platform) and the script execute daily at a particular time.

### Python library used in the script:

[``BeautifulSoup``](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
[``smtplib``](https://docs.python.org/3/library/smtplib.html)
[``datetime``](https://docs.python.org/3/library/datetime.html)
[``Logger``](https://docs.python.org/3/library/logging.html)
[``schedule``](https://schedule.readthedocs.io/en/stable/)
