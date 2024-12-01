# вариант 4
import random
from xml.dom.minidom import *

def name30(sp):
    index_book = sp[0].index('Название')
    kolvo_name30 = [1 for i in range(1, len(sp)) if len(sp[i][index_book])>30]
    print(f'\n Количество книг, в названии которых больше 30 символов: {sum(kolvo_name30)} штук')

def prin(st, names):
    for i in range(1, len(names)-1):
        if st[i] != '':
            print(f'{names[i]}: {st[i]}')
    print('////////\n')

def search(sp):
    index_name = sp[0].index('Автор (ФИО)')
    index_nickname = sp[0].index('Автор')
    index_cost = sp[0].index('Цена поступления')
    while True:
        flag = 0
        author = input('Введите имя автора (введите "стоп" для выхода): ')
        if author == 'стоп': break
        for i in range(1, len(sp)):
            if (sp[i][index_name] == author) or (sp[i][index_nickname] == author):
                if float(sp[i][index_cost]) <= 200:
                    prin(sp[i], sp[0]) 
                    flag += 1
        if flag == 0:
            print('Ничего не найдено.')
        else:
            print(f'Найдено {flag} результатов.')

def link_generator(sp):
    index_nickname = sp[0].index('Автор')
    index_book = sp[0].index('Название')
    index_date = sp[0].index('Дата поступления')
    output = open('library.txt', 'w')
    rand_num = [ random.randint(0, len(sp)-1) for i in range(20)]
    for num, i in enumerate(rand_num, start=1):
        print(f'{num}) {sp[i][index_nickname]}. {sp[i][index_book]} - {sp[i][index_date]}')
        output.write(f'{num}) {sp[i][index_nickname]}. {sp[i][index_book]} - {sp[i][index_date]}\n')    

def xml_parse():
    file = open('currency.xml', 'r', encoding='cp1251').read()
    data = parseString(file)
    data.normalize()
    elements = data.getElementsByTagName('Valute')
    ansDict = {}
    for node in elements:
        for child in node.childNodes:
            match child.tagName:
                case 'NumCode': NumCode = child.firstChild.data
                case 'CharCode': CharCode = child.firstChild.data
        ansDict[NumCode] = CharCode
    for i, j in ansDict.items():
        print(i, j) 

def genre(sp):
    m = set()
    index_genre = sp[0].index('Жанр книги')
    for i in range(1, len(sp)-1):
        for j in sp[i][index_genre].split('#'):
            m.add(j.strip())
    m.discard('')
    print('Теги:')
    for n, i in enumerate(m, start=1):
        print(n, i)

def popular_books(sp):
    index_count = sp[0].index('Кол-во выдач')
    index_book = sp[0].index('Название')
    sp_downl = list({(sp[i][index_book], int(sp[i][index_count])) for i in range(1, len(sp)-1)})
    sp_downl.sort(key=lambda x: x[1], reverse=True)   
    [print(i+1, sp_downl[i][0]) for i in range(20)]

with open('books.csv', 'r') as file:
    sp = [[j.rstrip('\n') for j in i.split(';')] for i in file.readlines()]
    name30(sp)
    search(sp)
    link_generator(sp)
    xml_parse()
    genre(sp)
    popular_books(sp)