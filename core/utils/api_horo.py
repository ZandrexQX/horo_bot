from datetime import datetime

from bs4 import BeautifulSoup
import requests

url = "https://ignio.com/r/export/utf/xml/daily/com.xml"


dict_horoskop: dict[datetime, BeautifulSoup] = {}

def get_horo(key: str) -> str:
    date_now = datetime.now().strftime('%Y-%m-%d')
    # print(date_now)
    data: BeautifulSoup = None
    response = requests.get(url)
    if dict_horoskop.get(date_now) is not None:
        data = dict_horoskop.get(date_now)
        # print("data")
    elif response.status_code == 200:
        data = BeautifulSoup(response.content, 'xml')
        dict_horoskop[date_now] = data
        # print("api")
    else:
        return "Ошибка сервера"
    return data.find(key).find('today').text