
# panda data pre-deal

import pandas  as pds

food_info=pds.read_csv("../../resources/day02_pandas/demo1.csv")

print(food_info)


food_info=food_info.sort_values("nutrition",ascending=True)

print(food_info)






