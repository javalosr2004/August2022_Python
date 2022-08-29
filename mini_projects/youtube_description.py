'''Gets the youtube description from the links provided'''

from requests_html import HTMLSession
import sys, pyperclip, re
from bs4 import BeautifulSoup


user_link = []
url_html = []

if len(sys.argv) > 1:
    if sys.argv[1] == '-c':
        print('Copying all links')
        all_links = pyperclip.paste()
        cleanString = re.sub(',',' ', all_links)
        user_link.extend(cleanString.split())
    else:
        print('Copying one link:')
        user_link.append(sys.argv[1])
        print(f'Link: {user_link[0]}')
else:
    user_link.append(input('Enter link: '))


html_list = {}

def parse_soup(html):
    soup = BeautifulSoup(html, 'lxml')
    r = soup.find_all('meta')
    return r


def request_html(url):
    with HTMLSession() as session:
        r = session.get(url)
        r.html.render(sleep = 15).html.search('meta')
        parsed_data = parse_soup(r)
        return parsed_data



def url_tasks():
    global html_list, user_link
    for url in user_link:
        response = request_html(url)
        print(response)


url_tasks()