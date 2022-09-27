from typing import Dict, Any

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)


data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")





# print(type(data))
# print(data["Primary Fur Color"])

# data_dict = data.to_dict()
# print(data_dict)

# color_list = data["Primary Fur Color"].to_list()
# gray_count = color_list.count("Gray")
# black_count = color_list.count("Black")
# cinnamon_count = color_list.count("Cinnamon")
# print(gray_count, black_count, cinnamon_count)





