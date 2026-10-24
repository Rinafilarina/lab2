from csv import reader
import random

def findstring(searchline, str):
    str = str.lower()
    index = str.find(searchline.lower())
    return index


def search_name(table):
    searchline=input('Введите на английском автора, которого хотите найти:')
    flag=0
    for row in table:
        if findstring(searchline, row[2]) != -1 and float(row[6].replace(',', '.'))<=150:
            print(f'{row[1]}, price: {row[6]}')
            flag+=1
    if flag==0:
        print("Ничего не найдено")
    else:
        print(f'Найдено позиций: {flag}')


def generate(table):
    output = open('result.txt', 'w')
    indices = random.sample(range(0, 9410), 20)
    for n in range(len(indices)):
        row = table[indices[n]]
        output.write(f'{n+1}: <{row[2]}>. <{row[1]}> - <{row[3]}>\n')
    output.close()


def publishers(table):
    print('Все издательства без повтоорений:')
    publish = []
    table.pop(0)
    for row in table:
        if not (row[4] in publish):
            publish.append(row[4])
            print(row[4])
    print('20 самых популярных книг:')
    top20 = sorted(table, key=lambda row: int(row[5]), reverse=True)[:20]
    for i in range(20):
        row = top20[i]
        print(f'{i+1}. {row[1]}: {row[5]} скачиваний')

    

def work_table():
    try:
        with open('books-en.csv', 'r') as csvfile:
            table = list(reader(csvfile, delimiter=';'))
            longname=0
            for row in table:
                if len(row[1])>30:
                    longname+=1
            print(longname)
            search_name(table)
            print('Введите любой символ, чтобы продолжить')
            a=input()
            generate(table)
            print('Введите любой символ, чтобы продолжить')
            a=input()
            publishers(table)
            print('Введите любой символ, чтобы продолжить')
            a=input()
    except FileNotFoundError:
        print('Файл не найден')
        return 0


work_table()


        

