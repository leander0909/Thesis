import csv
import pandas as pd


count=3
# Read text from txt file
with open("date.txt", "r") as file:
    text = file.read().strip()

print(text)
def ret_count(cell):
    print(cell)

df = pd.read_excel("dat_anys.xlsx","Sheet1",converters={
    text:ret_count
})
#print(df)