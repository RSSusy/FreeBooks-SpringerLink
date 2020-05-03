import os
import csv
import numpy as np
import requests
from bs4 import BeautifulSoup

same = 0

def sameBooks(amount):
    same = np.zeros(amount, dtype=np.int)
    x = 0
    with open('SearchResults.csv', 'r') as titles:
        line = csv.reader(titles, delimiter=',')
        for num in line:
            y = 0
            found = 1
            title = num[0]
            publication = num[1]
            bookSeries = num[2]
            journalV = num[3]
            journalI = num[4]
            itemDOI = num[5]
            authors = num[6]
            year = num[7]
            url = num[8]
            type = num[9]
            if x > 0:
                #same[x] = 0
                with open('SearchResults.csv','r') as check:
                    checkLine = csv.reader(check, delimiter=',')
                    for enum in checkLine:
                        if y > x:
                            checkTitle = enum[0]
                            #checkDOI = enum[5]
                            checkYear = enum[7]
                            checkUrl = enum[8]
                            #checkType = enum[9]
                            if title == checkTitle:
                                if year != checkYear:
                                    same[x] = 1
                                    same[y] = 1
                                elif year == checkYear:
                                    same[x] = 2
                                    same[y] = 2
                                break
                        y += 1
            else:
                same[x] = 1
            x += 1
        #print("\n\nFINISH")
    return same

def subtitle(urlSub):
    response = requests.get(urlSub)
    htmlSpringer = BeautifulSoup(response.text, 'html.parser')
    subtitle = htmlSpringer.find_all('div', class_='page-title')
    subtitle = htmlSpringer.find('h2', class_='page-title__subtitle')
    subtitle = subtitle.text
    return subtitle


def rewrite(same):
    a = 0
    with open('SearchResults.csv', 'r') as titles:
        line = csv.reader(titles, delimiter=',')
        for num in line:
            title = num[0]
            publication = num[1]
            bookSeries = num[2]
            journalV = num[3]
            journalI = num[4]
            itemDOI = num[5]
            authors = num[6]
            year = num[7]
            url = num[8]
            type = num[9]
            if same[a] == 0:
                with open('bookList.csv', mode='a+') as textbooks:
                    data = csv.writer(textbooks, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    data.writerow([title, publication, bookSeries, journalV, journalI, itemDOI, authors, None, url, type])
            elif same[a] == 1:
                with open('bookList.csv', mode='a+') as textbooks:
                    data = csv.writer(textbooks, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    data.writerow([title, publication, bookSeries, journalV, journalI, itemDOI, authors, year, url, type])
            elif same[a] == 2:
                with open('bookList.csv', mode='a+') as textbooks:
                    data = csv.writer(textbooks, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    data.writerow([title, publication, bookSeries, journalV, journalI, itemDOI, authors, subtitle(url), url, type])
            a += 1
    return 0


def amountRows():
    cuantity = 0
    with open('SearchResults.csv', 'r') as all:
        row = csv.reader(all, delimiter=',')
        for a in row:
            cuantity += 1
    return cuantity


def main():
    #os.remove('bookList.csv')
    saveTo = os.getcwd()
    #print(saveTo)
    saveTo += '/SearchResults.csv'
    req = requests.get('https://link.springer.com/search/csv?facet-content-type=%22Book%22&fbclid=IwAR1UldNESSETOXq4wO7KXrLA2NKKNOiKhuvJrP9XgQ9-qjz9dHIgcFUraN4&package=mat-covid19_textbooks&utm_source=commission_junction&utm_content=de_textlink&utm_medium=affiliate&utm_campaign=3_nsn6445_brand_PID7988357&countryChanged=true')
    with open(saveTo, 'wb') as f:
        f.write(req.content)
    amount = amountRows()
    same = sameBooks(amount)
    #print(np.count_nonzero(same))
    new = same
    rewrite(new)


if __name__ == '__main__':
    main()
