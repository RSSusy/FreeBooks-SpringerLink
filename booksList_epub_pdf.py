import os
import csv
import urllib2


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
                vPDF = urlDownloadPDF(url)
                vEPUB = urlDownloadEPUB(url)
            if x > 0:
                with open(fileCSV,'r') as check:
                    checkLine = csv.reader(check, delimiter=',')
                    for enum in checkLine:
                        if y > 0:
                            language = enum[11]
                            category = enum[10]
                            checkDOI = enum[5]
                            if itemDOI == checkDOI:
                                #print(str(x+1) + "\t\tMATCH FOUND")
                                found = True
                                break
                            else:
                                found = False
                        y += 1
            if found == True:
                #print(str(x+1) + "\t\tMATCH FOUND")
                with open('Results_PDF_EPUB.csv', mode='a+') as textbooks:
                    data = csv.writer(textbooks, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    data.writerow([title, publication, bookSeries, journalV, journalI, itemDOI, authors, year, url, type, vPDF, vEPUB, category, language])
            x += 1
        #print("\n\nFINISH")
    return 0


def urlDownloadPDF(url):
    urlPDF = url[0:4]
    urlPDF += 's'
    urlPDF += url[4:25]
    urlPDF += 'content/pdf/'
    urlPDF += url[30:37]
    urlPDF += '%2F'
    urlPDF += url[38:60]
    urlPDF += '.pdf'
    #print(urlPDF)
    try:
        urllib2.urlopen(urlPDF, timeout=10)
        return True
    except urllib2.URLError as err:
        return False


def urlDownloadEPUB(url):
    urlEPUB = url[0:4]
    urlEPUB += 's'
    urlEPUB += url[4:25]
    urlEPUB += 'download/epub/'
    urlEPUB += url[30:37]
    urlEPUB += '%2F'
    urlEPUB += url[38:60]
    urlEPUB += '.epub'
    try:
        urllib2.urlopen(urlEPUB, timeout=10)
        return True
    except urllib2.URLError as err:
        return False


def main():
    #os.remove('Results_PDF_EPUB.csv')
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
            vPDF = 'PDF'
            vEPUB = 'EPUB'
            with open('Results_PDF_EPUB.csv', mode='a+') as textbooks:
                data = csv.writer(textbooks, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                data.writerow([title, publication, bookSeries, journalV, journalI, itemDOI, authors, year, url, type, vPDF, vEPUB, category, language])
                break
    file = 'FinalResult.csv'
    books(file)


if __name__ == '__main__':
    main()
