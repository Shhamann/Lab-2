from csv import reader

with open('civic.csv', 'r') as file:

    i=reader(file, delimiter=';')
    print(i[1])