from csv import reader
classificacao =[]
with open('classificacao.csv', 'r') as csv_file:
    csv_reader = reader(csv_file)
    # Passing the cav_reader object to list() to get a list of lists
    list_of_rows = list(csv_reader)
    #list_of_rows.remove(list('0'))
classificacao.append(list_of_rows)
print(classificacao)