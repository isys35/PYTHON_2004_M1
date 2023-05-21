import requests
from bs4 import BeautifulSoup

url ="https://www.copart.com/ru/how-it-works/"
#Замаенить на сайи аукциона который нужен
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")
cars = soup.find_all("div", class_="car-info")

#получаем нужную информацию
for car in cars:
   make = car.find("div", class_="car-make").get_text()
   model = car.find("div", class_="car-model").get_text()
   vin = car.find("div", class_="car-vin").get_text()
   #Получаем ссылку на изображение
img_url = car.find("img")["src"]
#сохраняем информацию в базу данных или файл на жёсткий диск
# даллее можем обрабатывать данные и выгружать на веб-сайт WordPress

print("Данные успешно собраны ")