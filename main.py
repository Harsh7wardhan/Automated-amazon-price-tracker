import requests
from bs4 import BeautifulSoup
import smtplib
import lxml
url='https://www.amazon.in/Realme-Buds-Android-Smartphones-Orange/dp/B081RK5ZSP/ref=sr_1_4?dchild=1&keywords=realme+earphones&qid=1627535233&sr=8-4'
#printing the price**************************
response=requests.get(url='https://www.amazon.in/Realme-Buds-Android-Smartphones-Orange/dp/B081RK5ZSP/ref=sr_1_4?dchild=1&keywords=realme+earphones&qid=1627535233&sr=8-4',headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36','Accept-Language':'en-GB,en-US;q=0.9,en;q=0.8,mr;q=0.7'})
web_page=response.text
soup=BeautifulSoup(web_page,'lxml')
tag=soup.find(name='span',class_='a-size-medium a-color-price priceBlockBuyingPriceString')
x=tag.getText()
price=x.split('₹')[1]
og=float(price)
print(og)
#sending mails***************
my_email="wharsh89@gmail.com"
password='testing001'
buy_price=600
if og<buy_price:
    message = f"earbuds are now {price}"
    with smtplib.SMTP('smtp.gmail.com',port=587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,to_addrs='harsh07natu@gmail.com',msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}")