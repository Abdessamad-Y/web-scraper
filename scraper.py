import requests
from bs4 import BeautifulSoup
import os
import re
if __name__ == "__main__":
    number_of_pages = int(input())
    type_of_articles = input()
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    tup = ()
    r = requests.get('https://www.nature.com/nature/articles')
    soup = BeautifulSoup(r.content, 'html.parser')
    article = soup.find_all('article')
    for i in range(1, number_of_pages + 1):
        if i == 1:
            os.mkdir('page_' + str(i))  # creating saving path
            save_path = 'page_' + str(i)
            os.chdir(save_path)  # making the saving path by default
            tup = os.path.split(os.getcwd())  # saving in the specified file

            article = soup.find_all('article')
            sp = soup.findAll('span', {'class': 'c-pagination__link c-pagination__link--active'})
            saved_articles = []
            for b in article:
                s = b.find('span', {'data-test': "article.type"})
                x = s.get_text()
                x = x.strip('\n')
                if x == type_of_articles:  # cheking what types of article the users want

                    a = b.find_all('a', {'data-track-action': "view article"})
                    for j in a:  # getting content & names
                        name = j.get_text()
                        s = j.get('href')
                        new_name = name.strip()
                        for ele in new_name:
                            if ele in punc:
                                new_name = new_name.replace(ele, "")
                        new_name = new_name.replace(" ", "_")

                        url1 = 'https://www.nature.com' + s
                        r = requests.get(url1)
                        soup = BeautifulSoup(r.content, 'html.parser')
                        # comp = 'c-article-body'|'article-item__body'
                        c_article_body = soup.find('div', class_='article-item__body')
                        body = c_article_body.text.strip()
                        body = body.replace("\n", "")
                        body = body.encode('utf-8')
                        file = open(new_name + '.txt', 'wb')
                        file.write(body)

                        saved_articles.append(new_name + '.txt')
            os.chdir(tup[0])  # returning to the original path
        elif i != 1:
            os.mkdir('page_' + str(i))  # creating saving path
            save_path = 'page_' + str(i)
            os.chdir(save_path)  # making the saving path by default
            tup = os.path.split(os.getcwd())  # saving in the specified file

            #a = soup.find_all('a', {'class': 'c-pagination__link'})
            #for j in a:
            # s = j.get('href')
                #print(s)
            new_url = "https://www.nature.com/nature/articles/page=?searchType=journalSearch&sort=PubDate&page=" + str(i)
            #print(new_url)
            r = requests.get(new_url)
            soup = BeautifulSoup(r.content, 'html.parser')
            article = soup.find_all('article')
            sp = soup.findAll('span', {'class': 'c-pagination__link c-pagination__link--active'})
            saved_articles = []
            for k in article:
                s = k.find('span', {'data-test': "article.type"})
                x = s.get_text()
                x = x.strip('\n')
                if x == type_of_articles:  # cheking what types of article the users want
                    a = k.find_all('a', {'data-track-action': "view article"})
                    for e in a:  # getting content & names
                        name = e.get_text()
                        s = e.get('href')
                        new_name = name.strip()
                        for ele in new_name:
                            if ele in punc:
                                new_name = new_name.replace(ele, "")
                        new_name = new_name.replace(" ", "_")

                        url1 = 'https://www.nature.com' + s
                        r = requests.get(url1)
                        soup = BeautifulSoup(r.content, 'html.parser')
                        #comp = 'c-article-body'|'article-item__body'
                        c_article_body = soup.find('div', class_='article-item__body')
                        body = c_article_body.text.strip()
                        body = body.replace("\n", "")
                        body = body.encode('utf-8')
                        file = open(new_name + '.txt', 'wb')
                        file.write(body)

                        saved_articles.append(new_name + '.txt')
            os.chdir(tup[0])  # returning to the original path