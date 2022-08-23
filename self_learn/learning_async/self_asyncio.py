'''fetching the content of multiple urls'''
import asyncio, aiohttp
from bs4 import BeautifulSoup


urls = ['https://www.google.com', 'https://www.facebook.com']


async def get_site(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as r:
            return await r.text()

async def main(urls):

    cors = [get_site(url) for url in urls]
 
    response = await asyncio.gather(*cors)

    return response

def parse(html):
    soup = BeautifulSoup(html, 'lxml')
    all_links = soup.find_all('a', href=True)
    for link in all_links:
        print(link['href'])

htmls = asyncio.run(main(urls))

for html in htmls:
    parse(html)