from ast import parse
import json
import requests, asyncio, aiohttp
from bs4 import BeautifulSoup
from importingJSON import data as words

url = 'https://kids.wordsmyth.net/we/?ent={}'




async def request_page(session, url):
    try:
        async with session.get(url) as r:
            return await r.text()
    except:
        return 0

async def get_tasks(session, urls):
    tasks = []
    for url in urls:
        task = asyncio.create_task(request_page(session, url))
        tasks.append(task)

    results = await asyncio.gather(*tasks)
    return results

async def main(urls):
    async with aiohttp.ClientSession() as session:
        responses = await get_tasks(session, urls)
        return responses
    

def parse_data(soup):

    try:
        all_data = soup.find('tbody').find('tr', {'class': 'definition'}).find('td', {'class': 'data'})
        data = [data for data in all_data]

        return data[0].text
    except:
        return 0

words = list(words) #creates an 'ordered' list
urls = [url.format(word) for word in words[0:]]

responses = asyncio.run(main(urls))
word_dictionary = {}

for word, html in zip(words, responses):
    soup = BeautifulSoup(html, 'lxml')
    parsed_data = parse_data(soup)

    if parsed_data == 0:
        pass
    else:
        try:
            index = str(parsed_data).index('.')
        except:
            index = len(str(parsed_data))
        word_dictionary[str(word)] = parsed_data[:index + 1]

with open('words_dictionary.json', 'w') as f:
    json.dump(word_dictionary, f)


