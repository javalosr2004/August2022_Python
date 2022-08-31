'''Gets the youtube description from the links provided'''

import sys, pyperclip, re, logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver

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




options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)")
driver = webdriver.Chrome('/Users/jesusavalos/Documents/Python/August2022_Python/chromedriver', options = options)


html_list = []

def get_html(url):   
    global html_list, driver
    driver.get(url)
    logging.warning('SUCCESFULLY GRABBED HTML')
    logging.warning('WAITING FOR YOUTUBE TO LOAD')
    wait = WebDriverWait(driver,15).until(EC.visibility_of_element_located((By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[1]/h1/yt-formatted-string")))
    logging.warning('SUCCESS: LOADED YOUTUBE')
    html_list.append(driver.page_source)

def parse(html):
    soup = BeautifulSoup(html, 'lxml')
    description = soup.find('div', {'id':'description'})
    description_text = description.text.splitlines()
    title = soup.find_all('h1')
    print('Title: ' + str(title))
    for i in description_text:
        print(i)
    print('\n\n\n\n')



def main():
    global user_link, html_list


    for url in user_link:
        get_html(url)
    
    for html in html_list:
        parse(html)

    driver.quit()

main()