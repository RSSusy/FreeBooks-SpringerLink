import os
import csv
import requests
import pandas as pd


def books(fileCSV):
    x = 0
    with open('bookList.csv', 'r') as titles:
        line = csv.reader(titles, delimiter=',')
        for num in line:
            y = 0
            found = False
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
                with open(fileCSV,'r') as check:
                    checkLine = csv.reader(check, delimiter=',')
                    for enum in checkLine:
                        if y > 0:
                            language = enum[9]
                            category = enum[11]
                            checkDOI = enum[17]
                            checkDOI = checkDOI[15:len(checkDOI)]
                            if itemDOI == checkDOI:
                                #print(str(x+1) + "\t\tMATCH FOUND")
                                found = True
                                break
                            else:
                                found = False
                        y += 1
            if found == True:
                #print(str(x+1) + "\t\tMATCH FOUND")
                with open('FinalResult.csv', mode='a+') as textbooks:
                    data = csv.writer(textbooks, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    data.writerow([title, publication, bookSeries, journalV, journalI, itemDOI, authors, year, url, type, category, language])
            x += 1
        #print("\n\nFINISH")
    return 0


def main():
    #os.remove('FinalResult.csv')
    here = os.getcwd()
    with open('bookList.csv', 'r') as titles:
        line = csv.reader(titles, delimiter=',')
        for num in line:
            '''y = 0
            found = False'''
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
            category = 'Language Collection'
            language = 'English Package Name'
            with open('FinalResult.csv', mode='a+') as textbooks:
                data = csv.writer(textbooks, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                data.writerow([title, publication, bookSeries, journalV, journalI, itemDOI, authors, year, url, type, category, language])
                break
    saveTo = here
    #print(saveTo)
    saveTo += '/Free+English+textbooks.xlsx'
    req = requests.get('https://resource-cms.springernature.com/springer-cms/rest/v1/content/17858272/data/v4')
    with open(saveTo, 'wb') as f:
        f.write(req.content)
    convert = pd.read_excel('Free+English+textbooks.xlsx')
    df = pd.DataFrame(convert)
    os.remove('Free+English+textbooks.xlsx')
    df.to_csv('FreeEnglish_textbooks.csv', index=False, encoding='utf-8')
    file = 'FreeEnglish_textbooks.csv'
    books(file)
    saveTo = here
    #print(saveTo)
    saveTo += '/free+textbooks+GER+03042020.xlsx'
    req = requests.get('https://resource-cms.springernature.com/springer-cms/rest/v1/content/17863240/data/v2')
    with open(saveTo, 'wb') as f:
        f.write(req.content)
    convert = pd.read_excel('free+textbooks+GER+03042020.xlsx')
    df = pd.DataFrame(convert)
    os.remove('free+textbooks+GER+03042020.xlsx')
    df.to_csv('FreeGerman_textbooks.csv', index=False, encoding='utf-8')
    file = 'FreeGerman_textbooks.csv'
    books(file)
    saveTo = here
    #print(saveTo)
    saveTo += '/Emergency+Nursing+Titles.xlsx'
    req = requests.get('https://resource-cms.springernature.com/springer-cms/rest/v1/content/17856246/data/v3')
    with open(saveTo, 'wb') as f:
        f.write(req.content)
    convert = pd.read_excel('Emergency+Nursing+Titles.xlsx')
    df = pd.DataFrame(convert)
    os.remove('Emergency+Nursing+Titles.xlsx')
    df.to_csv('EmergencyNursingTitles.csv', index=False, encoding='utf-8')
    file = 'EmergencyNursingTitles.csv'
    books(file)


if __name__ == '__main__':
    main()
