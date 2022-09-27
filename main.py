from typing import Dict, Any

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# print(type(data))
# print(data["Primary Fur Color"])

# data_dict = data.to_dict()
# print(data_dict)

color_list = data["Primary Fur Color"].to_list()
gray_count = color_list.count("Gray")
black_count = color_list.count("Black")
cinnamon_count = color_list.count("Cinnamon")
print(gray_count, black_count, cinnamon_count)





