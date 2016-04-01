"""
Practice stuff to implement into main Assignment

https://newcircle.com/s/post/1572/python_for_beginners_reading_and_manipulating_csv_files
"""
import csv
item_costs = []
f = open('items.csv')
csv_f = csv.reader(f)

for row in csv_f:
    item_costs.append(row[2])
print(item_costs)
