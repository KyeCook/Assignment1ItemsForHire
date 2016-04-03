"""
Practice stuff to implement into main Assignment

https://newcircle.com/s/post/1572/python_for_beginners_reading_and_manipulating_csv_files
"""
# Following code to be used in loading function
import csv
with open('items.csv') as fp:
#csv_f = csv.reader(f)
    csv_f = csv.writer(fp)

    data = [['Me', 'you'], [1, 2], [3, 4], [5, 6]]

    csv_f.writerows(data)


# item_names = []
# item_descriptions = []
# item_costs = []
# item_availability = []
# item_id = []
#
# item_id_count = -1
#
# for row in csv_f:
#     item_id_count += 1
#
#     item_id.append(item_id_count)
#     item_names.append(row[0])
#     item_descriptions.append(row[1])
#     item_costs.append(row[2])
#
#     if row[3] == "out":
#         item_availability.append("*")
#     else:
#         item_availability.append("")
#     items = ("{} - {} ({}) = $ {}{}".format(item_id[item_id_count], item_names[item_id_count],
#                                             item_descriptions[item_id_count], item_costs[item_id_count],
#                                             item_availability[item_id_count]))
#     print(items)
#
# # Following code can be used for hire function
#
# print("Enter number of item to hire")
# item_to_hire = int(input(">>> "))
# if item_to_hire in item_id:
#     item_availability[item_to_hire] = "*"
#     print("{} - {} ({}) = $ {}{}".format(item_id[item_to_hire], item_names[item_to_hire],
#                                          item_descriptions[item_to_hire], item_costs[item_to_hire],
#                                          item_availability[item_to_hire]))
# else:
#     print("That item is not available for hire")

