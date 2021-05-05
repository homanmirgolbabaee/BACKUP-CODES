import csv
import pandas
from csv import reader
#1st subproblem
# >50% honest
row_list = [
    ["ELF(A)", "ELF(B)", "A Says (about B)","B Says(about A)"],
    ["Honest", "Honest", "Honest","Honest"],
    ["Honest", "Liar", "Liar","Either"],
    ["Liar", "Honest", "Either","Liar"]
]
read_row_list=[]
csv.register_dialect('myDialect',
                     quoting=csv.QUOTE_ALL)
with open('data.csv', 'w+', newline='') as file:
    writer = csv.writer(file, dialect='myDialect')
    writer.writerows(row_list)
df = pandas.read_csv('data.csv')
print(df)
i = 0
with open('office.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile))
print("Rows Of The CSV Is:"+str(len(data)))
print("\n")
TruthFull_Factor = "Honest"
Liar_Factor = "Lie"
Either_Factor = "Either"
for i in range(3):
    if data[i][0]==str(TruthFull_Factor) and data[i][1]==str(TruthFull_Factor):
        print("Yes We Have A Truthfullness Happening")
for j in range(3):
    if data[j][0]==str(Liar_Factor) and data[j][1]==str(Liar_Factor):
        print("We Dont have A CERTAIN CASE (?)")
for k in range(3):
    if data[k][0]==Liar_Factor and data[k][1]==TruthFull_Factor:
        print("Elf A Is Liar")
    if data[k][0]==TruthFull_Factor and data[k][1]==Liar_Factor:
        print("Elf B Is Liar")
           
