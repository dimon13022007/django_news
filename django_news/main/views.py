from django.shortcuts import render
from bs4 import BeautifulSoup as Bs
import requests



# Создаем функцию-обработчик для отображения цен на биткоин
def bitcoin_prices(request):
    # Получаем HTML-страницу с сайта Binance
    url = 'https://www.binance.com/ru-UA/price/bitcoin'
    r = requests.get(url)

    # Используем BeautifulSoup для парсинга HTML-страницы
    soup = Bs(r.text, 'html.parser')
    bitok = soup.find_all('div', class_='css-12ujz79')
    clear_bitok = [i.text for i in bitok]

    # Возвращаем рендеринг шаблона с данными о ценах на биткоин
    return render(request, 'main/bitcoin.html', {'prices':clear_bitok})




def index(request):
    return render(request, 'main/index.html')




def about(request):
    return render(request, 'main/about.html')



