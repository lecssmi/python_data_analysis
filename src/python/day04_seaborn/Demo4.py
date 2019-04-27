

# linear regression

import seaborn as sns

import  matplotlib.pyplot as plt


tips=sns.load_dataset("tips")

print(tips)

# sns.pairplot(tips)


# the x, y specifies columns used to draw with
sns.regplot(x="total_bill",y="tip",data=tips)


plt.show()


g=sns.FacetGrid(tips,col="sex")
g.map(plt.hist,"total_bill")

plt.show()

