
# titanic train

import pandas as pd

titanic_survival=pd.read_csv("../../resources/day02_pandas/train.csv")

print(titanic_survival.shape)

print(titanic_survival.head(1))


# pandas use 'NaN' to represent null or empty value
print(titanic_survival.columns.tolist())



import numpy as np


age=titanic_survival["Age"]

print(age.head(10))

age_is_null=pd.isnull(age)

print(len(age[age_is_null]))


print(age.mean)


good_ages=age[age_is_null==False]


print(good_ages)

print(good_ages.sum()/len(good_ages))

print(good_ages.mean())


passenger_class=[1,2,3]

fares_by_class={}

for this_class in passenger_class:
    pclass_rows=titanic_survival[titanic_survival["Pclass"]==this_class]

    pclass_fares=pclass_rows["Fare"]

    pclass_fares_mean=pclass_fares.mean()

    fares_by_class[this_class]=pclass_fares_mean

print(fares_by_class)




# select aggfunc(values ) from table group by  index
passenger_survival=titanic_survival.pivot_table(index="Pclass",values="Survived",aggfunc=np.mean)


print(passenger_survival)

# the default aggregate function is 'mean'
passenge_age=titanic_survival.pivot_table(index="Pclass",values="Age",aggfunc=np.mean)

print(passenge_age)



port_stats=titanic_survival.pivot_table(index="Pclass",values=["Fare","Survived"],aggfunc=np.sum)

print(port_stats)



drop_na_columns=titanic_survival.dropna(axis=0,subset=["Age","Sex"])

print(titanic_survival.shape)
print(drop_na_columns.shape)







