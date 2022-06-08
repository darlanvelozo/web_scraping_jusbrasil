
from csv import reader
links = []
with open('links.csv', 'r') as csv_file:
    csv_reader = reader(csv_file)
    # Passing the cav_reader object to list() to get a list of lists
    list_of_rows = list(csv_reader)
    list_of_rows.remove(list('0'))

links.append(list_of_rows)

j=0
while True:
    try:
        print(list_of_rows[j][0])
    except:
        print("F")
        break
    j+=1
print(links[0][0][0])