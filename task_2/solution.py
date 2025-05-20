import requests
import csv
from bs4 import BeautifulSoup, ResultSet
from config import base_url, page_url, header, filename

def get_data_and_links(url: str, data: dict) -> tuple[str, dict[str, int]]:
    """Делает запрос на страницу, и вытаскивает из нее: 
    Ссылку на следующую страницу
    Количество животных, на определенную букву, дополняет, уже, существующий dict 

    Args:
        url (str): Ссылка на страницу
        data (dict): Исходный словарь данных

    Returns:
        tuple[str, dict[str, int]]: Ссылка на следующую страницу, Обновленный словарь данных
    """
    response: requests.Response = requests.get(url, timeout=10)
    soup: BeautifulSoup = BeautifulSoup(response.text, 'html.parser')
    raw_data: ResultSet = soup.find_all('div', class_='mw-category-group')
    del raw_data[0]
    del raw_data[0]

    links: str = soup.find('div', id='mw-pages').find_all('a')[-1].get('href')

    for cluster in raw_data:
        letter: str = cluster.find('h3').text
        if letter == "A":
            links = None
            break
        if data.get(letter) is None:
            data[letter] = len(cluster.find_all('li'))
        else:
            data[letter] += len(cluster.find_all('li'))

    return links, data

def write_in_file(data: tuple, mode: str):
    """Записывает значение типа tuple в файл

    Args:
        data (tuple): Кортеж с данными
        mode (str): Режим открытия файла
    """
    with open(filename, mode, encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(data)

def solution():
    """Делает запросы и записывает данные в файл
    """
    write_in_file(header, mode="w")
    data: dict = {}
    link: str = page_url
    url: str = f"{base_url}{link}"
    while (link is not None):
        link, data = get_data_and_links(url, data)
        if link is None:
            break
        url = f"{base_url}{link}"
        if len(data) > 1:
            value: tuple = tuple(data.items())[0]
            write_in_file(value, "a")
            del data[value[0]]
    write_in_file(tuple(data.items())[0], "a")

if __name__ == "__main__":
    solution()
