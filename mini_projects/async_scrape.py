import asyncio, aiohttp, webbrowser
from bs4 import BeautifulSoup



new_tasks = []
async def open_page(url):
    webbrowser.open(url)


def get_parse(data):
    base = data[0]
    soup = BeautifulSoup(data[1], 'lxml')
    url = soup.find('img')['src']
    if 'http' in url or 'https' in url:
        return url
    elif url[0] != '/':
        return base + '/' + url
    return base + url

def open_url(urls):
    for url in urls:
        webbrowser.open(url)

async def get_html(session, url):
    async with session.get(url) as r:
        text = await r.text()
        return url, text
        

async def get_tasks(session, urls):
    tasks = []

    for url in urls:
        task = asyncio.create_task(get_html(session, url))
        tasks.append(task)

    return tasks

async def main(urls):
    async with aiohttp.ClientSession() as session:
        tasks = await get_tasks(session, urls)
        responses = await asyncio.gather(*tasks)
        return responses


urls = ['https://www.facebook.com']

data = asyncio.run(main(urls))

src_urls = [get_parse(data_set) for data_set in data]

open_url(src_urls)

