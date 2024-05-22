# SigmaBank столкнулась с проблемой: количество спам-сообщений, содержащих URL, увеличивается, и они обходят текущие фильтры.
# Ваша задача — создать Python-функцию, которая будет проверять входящие сообщения
# и выявлять скрытые в них ссылки для дальнейшего анализа.

import re
from collections import Counter
from typing import Dict
import requests

URL_REGEX = re.compile(r'(?:(?:https?|ftp):\/\/)?(?:www\.)?([a-zA-Z0-9-]+\.[a-zA-Z]{2,}(?:\.[a-zA-Z]{2})?[\/\w=?:-]*)')

def parse_urls(message: str) -> Dict[str, int]:
    link_list = URL_REGEX.findall(message)
    link_list = [re.sub(r'[^a-zA-Z\s\d]$','', link) for link in link_list]
    reachable_urls = []
    for url in link_list:
        try:
            if url in reachable_urls:
                reachable_urls.append(url)
                continue
            response = requests.head(f'http://www.{url}', allow_redirects=True, timeout=5)
            if response.ok:
                reachable_urls.append(url)
            else:
                response = requests.head(f'http://www.{url}', allow_redirects=False, timeout=5)
                if response.ok:
                    reachable_urls.append(url)
        except requests.RequestException:
            pass
    return dict(Counter(reachable_urls))

if __name__ == "__main__":
    message = (
        "Check out this link www.example.com, example.com and"
        " also https://www.xn--80ak6aa92e.com/space"
        " also www.xn--80ak6aa92e.com"
        " also xn--80ak6aa92e.com/"
        " also apple.com"
        " Don't miss this great opportunity!"
        " www.google.com."
        " hello.ru"
        " Quick visit to https://www.wikipedia.org/ for a wealth of knowledge."
        " Stay updated with news on https://www.bbc.co.uk or https://www.cnn.com."
    )
    print(parse_urls(message))

