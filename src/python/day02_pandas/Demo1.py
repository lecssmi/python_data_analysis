 #  pandas  data read

import  pandas  as pds


# the file path can be absolute path or relative path ..
# the base  directory is the package containing code file

# the first line will be treated as outline default
food_info=pds.read_csv("../../resources/day02_pandas/demo1.csv")


# pandas is  a  package tool based on numpy

# pandas is a grammar sugar based on numpy

print(type(food_info))

print(food_info.dtypes)

print(food_info.shape)

# head lines
print(food_info.head(2))

# tail lines
print(food_info.tail(1))

# when get data from head or tail, a line will be added to first column automatic ,
# represent line number

print(food_info["name"])

columns_tolist = food_info.columns.tolist()

for x in columns_tolist:
    print(x)


 # get all the column names
print(food_info.columns)



# pandas index and calculate

print(food_info.loc[1])



print(food_info.loc[0:3:2])


times_10=food_info["nutrition"]*100

print(times_10)

food_info["nutrition"]=food_info["nutrition"]*100

print(food_info)

food_info["100_times_nutrition"]=food_info["nutrition"]*100

print(food_info.tail(1))











