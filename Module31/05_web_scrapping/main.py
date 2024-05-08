import re
import requests
from selenium import webdriver

pattern = re.compile(r'<h3.*?>(.*?)<\/h3>')


def get_h3_from_page(url: str) -> None:
    """
    Функция получения текста всех заголовков h3
    """
    
    dr = webdriver.Chrome()
    dr.get(url)
    html = dr.page_source
    subheadings = pattern.findall(html)
    print(subheadings)


with open('examples.html', 'r') as f:
    text = f.read()
    result = pattern.findall(text)
print(result)
url = input('Введите URL страницы: ')
get_h3_from_page(url)
