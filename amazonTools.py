import requests
from bs4 import BeautifulSoup
import smtplib

url = 'https://www.amazon.in/Apple-iPad-11-inch-Wi-Fi-64GB/dp/B07KKRPWCF/ref=sr_1_1?keywords=ipad+pro&qid=1567737963&s=computers&sr=1-1'
headers = {"User-Agent" : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
 

def amazon_scrapper():
    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

   # title = soup.find(id="productTitle").get_text().strip()
    price = soup.find(id="priceblock_ourprice").get_text().strip()

    converted_price = float(price[2:8].replace(',', ""))

    if converted_price<=70000:
        send_email()

def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('vaibhavanand1591@gmail.com', 'xzwvwzhdjvrkqamt')

    subject = 'Amazon price Notification'
    body = "check out the amazon link : {}".format(url)

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'vaibhavanand1591@gmail.com',
        'vaibhav@bookgosee.com',
        msg
    )
    print('send email')
    server.quit() 

amazon_scrapper()