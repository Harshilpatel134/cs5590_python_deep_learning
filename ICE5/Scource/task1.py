import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

def show_plot(dates, prices):
    linear_mod = linear_model.LinearRegression()
    dates = np.reshape(dates, (len(dates), 1))
    prices = np.reshape(prices, (len(prices), 1))
    linear_mod.fit(dates, prices)
    plt.scatter(dates, prices, color='yellow')  # plotting the initial datapoints
    plt.plot(dates, linear_mod.predict(dates), color='blue', linewidth=3)  # plotting the line made by linear regression
    plt.show()
    return

x = [0,1,2,3,4,5,6,7,8,9]
y = [1,3,2,5,7,8,8,9,10,12]

x=np.reshape(x,(len(x),1))

y=np.reshape(y,(len(y),1))

show_plot(x,y)
linear_mod = linear_model.LinearRegression()
linear_mod.fit(x,y)
predicted_y = linear_mod.predict(10)
print(predicted_y)





