import csv

i=0
j=0
count=3
# Read text from txt file
with open("date.txt", "r") as file:
    text = file.read().strip()

print(text)


def search_cell(txt1):
    global i,j
    with open('dat_als.csv', 'r') as f:
        reader = csv.reader(f)
        #print(txt1)
        #print('1')
        for i, row in enumerate(reader):
            #print('2')
            for j, column in enumerate(row):
                #print('3')
                if txt1 in column:
                    #print(txt1)
                    #print('4')
                    print((i,j))
                    #write_csv(i,j,txt1)
                    return (i,j)
    print('nope')
    return 'nope'

search_cell(text)
print((i,j))

with open('dat_als.csv', mode='w') as fi:
    writer = csv.writer(fi)
    row_number = i  # Index starts at 0
    column_number = j  # Index starts at 0
    print((row_number,column_number))
    #writer.writerow([None] * column_number + [count] + [None] * (column_number - 1))
    writer.writerow([None] * column_number + [count] + [None] * (row_number - 1))
    fi.close()
