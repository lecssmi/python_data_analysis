 #画折线图
import  matplotlib.pyplot as plt
import  pandas as pd

data = pd.read_csv("../../resources/day03_matplotlib/Demo.csv")

print(data)

year = data["year"]

print(type(year))

data["year"]=pd.to_datetime(data["year"]).dt.month

print(data)


plt.plot(data["year"],data["value"],label="figure1")

plt.xticks(rotation=45)

plt.xlabel("month")

plt.ylabel("value")

plt.title("Demo Diagram")

plt.legend(loc="best")

# 画直方图

fig=plt.figure()

ax2 = fig.add_subplot(2,2,2)



ax2.bar(data["year"],data["value"])

ax3=fig.add_subplot(2,2,3)

ax3.hist(data["value"])

plt.show()


