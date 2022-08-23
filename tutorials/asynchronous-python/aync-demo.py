import asyncio, aiohttp
from bs4 import BeautifulSoup

urls = ['https://www.google.com', 'https://www.twitter.com']


async def get_page(session, url):
    async with session.get(url) as r:
        return await r.text()
    
async def get_tasks(session, urls):
    tasks = []
    for url in urls:
        task = asyncio.create_task(get_page(session, url))
        tasks.append(task)

    results = await asyncio.gather(*tasks) #unpacks variable
    return results

async def main(urls):

    async with aiohttp.ClientSession() as session:
        data = await get_tasks(session, urls)
        return data

def parse(results):
    for html in results:
        soup = BeautifulSoup(html, 'lxml')

data = asyncio.run(main(urls))
print(type(data[0]))
 