import os
import csv
import time
import requests
import threading
import booksListSame
import booksListLanguage
import booksList_epub_pdf


def books(saveFile):
    enum = 0
    with open('Results_PDF_EPUB.csv', 'r') as titles:
        line = csv.reader(titles, delimiter=',')
        for num in line:
            if enum > 0:
                title = num[0]
                itemDOI = num[5]
                year = num[7]
                url = num[8]
                type = num[9]
                vPDF = num[10]
                vEPUB = num[11]
                category = num[12]
                language = num[13]
                if type == "Book":
                    thread1 = threading.Thread(target=urlDownloadPDF, args=(url,title,year,category,language,enum,saveFile))
                    thread2 = threading.Thread(target=urlDownloadEPUB, args=(url,title,year,category,language,enum,saveFile))
                    if vEPUB == "True":
                        thread2.start()
                        time.sleep(20)
                    if vPDF == "True":
                        thread1.start()
                        time.sleep(20)
                    print('\n')
            enum += 1
    return 0


def urlDownloadPDF(url, title, year, category, language, enum, saveFile):
    urlPDF = url[0:4]
    urlPDF += 's'
    urlPDF += url[4:25]
    urlPDF += 'content/pdf/'
    urlPDF += url[30:37]
    urlPDF += '%2F'
    urlPDF += url[38:60]
    urlPDF += '.pdf'
    try:
        req = requests.get(urlPDF)
        saveTo = saveFile
        language = makeFolder(saveTo, language)
        saveTo += language
        saveTo += '/'
        category = makeFolder(saveTo, category)
        saveTo += category
        saveTo += '/'
        title = makeFolder(saveTo, title[0:60])
        saveTo += title
        if year != "":
            saveTo += '/'
            year = makeFolder(saveTo, year)
            saveTo += year
        saveTo += '/'
        saveTo += title
        saveTo += '.pdf'
        print("Excel - Row " + str(enum + 1) + " PDF")
        print(urlPDF)
        print('\t' + saveTo)
        print('\n')
        with open(saveTo, 'wb') as f:
            f.write(req.content)
        return 0
    except requests.RequestException as err:
        return 0


def urlDownloadEPUB(url, title, year, category, language, enum, saveFile):
    urlEPUB = url[0:4]
    urlEPUB += 's'
    urlEPUB += url[4:25]
    urlEPUB += 'download/epub/'
    urlEPUB += url[30:37]
    urlEPUB += '%2F'
    urlEPUB += url[38:60]
    urlEPUB += '.epub'
    try:
        req = requests.get(urlEPUB)
        saveTo = saveFile
        language = makeFolder(saveTo, language)
        saveTo += language
        saveTo += '/'
        category = makeFolder(saveTo, category)
        saveTo += category
        saveTo += '/'
        title = makeFolder(saveTo, title[0:60])
        saveTo += title
        if year != "":
            saveTo += '/'
            year = makeFolder(saveTo, year)
            saveTo += year
        saveTo += '/'
        saveTo += title
        saveTo += '.epub'
        print("Excel - Row " + str(enum + 1) + " EPUB")
        print(urlEPUB)
        print('\t' + saveTo)
        print('\n')
        with open(saveTo, 'wb') as f:
            f.write(req.content)
        return 0
    except requests.RequestException as err:
        return 0


def makeFolder(saveTo, title):
    try:
        os.chdir(saveTo)
        title = takeAway(title)
        os.mkdir(title)
        return title
    except OSError:
        #print("Existing folder")
        return title


def takeAway(title):
    folderName = title
    for length in range(0,len(title)):
        if title[length] == ":":
            toEnd = length+1
            folderName = title[0:length]
            folderName += title[toEnd:len(title)]
            break
        elif title[length] == "/":
            toEnd = length+1
            folderName = title[0:length]
            folderName += ' '
            folderName += title[toEnd:len(title)]
            break
        elif title[length] == "@":
            toEnd = length+1
            folderName = title[0:length]
            folderName += title[toEnd:len(title)]
            break
        elif title[length] == chr(169):
            toEnd = length+1
            folderName = title[0:length]
            folderName += title[toEnd:len(title)]
            break
        elif title[length] == chr(132):
            toEnd = length+1
            folderName = title[0:length]
            folderName += title[toEnd:len(title)]
            break
        elif title[length] == chr(137):
            toEnd = length+1
            folderName = title[0:length]
            folderName += title[toEnd:len(title)]
            break
        elif title[length] == chr(139):
            toEnd = length+1
            folderName = title[0:length]
            folderName += title[toEnd:len(title)]
            break
        elif title[length] == chr(148):
            toEnd = length+1
            folderName = title[0:length]
            folderName += title[toEnd:len(title)]
            break
        elif title[length] == chr(129):
            toEnd = length+1
            folderName = title[0:length]
            folderName += title[toEnd:len(title)]
            break
        elif length >= (len(title)-1):
            if title[length] == " ":
                toEnd = len(title)-1
                folderName = title[0:toEnd]
    title = folderName
    return title


def main():
    saveFile = os.getcwd()
    os.mkdir('Springer Link')
    saveFile += '/Springer Link/'
    start_time = time.time()
    booksListSame.main()
    print("--- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    booksListLanguage.main()
    print("--- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    print("Please wait 5 to 10 minutes...")
    booksList_epub_pdf.main()
    print("--- %s seconds ---" % (time.time() - start_time))
    os.remove('SearchResults.csv')
    os.remove('bookList.csv')
    os.remove('FinalResult.csv')
    os.remove('FreeEnglish_textbooks.csv')
    os.remove('FreeGerman_textbooks.csv')
    os.remove('EmergencyNursingTitles.csv')
    time.sleep(1)
    os.system('clear')
    print("STARTS DOWNLOADING\n\n")
    books(saveFile)
    print("\nALL DOWNLOADS ARE DONE")


if __name__ == '__main__':
    main()
