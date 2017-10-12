import csv
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

dates = []
mopen = []

def getdata(fn):
    with open(fn, 'r') as csvfile:
        csvfr = csv.reader(csvfile)
        next(csvfr)  # skipping column names
        for row in csvfr:
            r=row[0].split("-")
            dates.append(int(r[0]+r[1]+r[2]))
            print(int(r[0]+r[1]+r[2]))
            print(float(row[1]))
            mopen.append(float(row[1]))
    return


def splot(dates, mopen):
    linear_mod = linear_model.LinearRegression()
    dates = np.reshape(dates, (len(dates), 1))  # converting to matrix of n X 1
    mopen = np.reshape(mopen, (len(mopen), 1))
    linear_mod.fit(dates, mopen)  # fitting the data points in the model
    plt.scatter(dates, mopen, color='blue')  # plotting the initial datapoints
    plt.xlabel("month.year")
    plt.ylabel("price")
    plt.plot(dates, linear_mod.predict(dates), color='red', linewidth=3)  # plotting the line made by linear regression
    plt.show()
    return


def predict_price(dates, mopen, x):
    linear_mod = linear_model.LinearRegression()  # defining the linear regression model
    dates = np.reshape(dates, (len(dates), 1))  # converting to matrix of n X 1
    mopen = np.reshape(mopen, (len(mopen), 1))
    linear_mod.fit(dates, mopen)  # fitting the data points in the model
    predicted_mintemp = linear_mod.predict(x)
    return predicted_mintemp[0][0], linear_mod.coef_[0][0], linear_mod.intercept_[0]


getdata('NASDAQComposite.csv')  # calling get_data method by passing the csv file to it


splot(dates, mopen)
# image of the plot will be generated. Save it if you want and then Close it to continue the execution of the below code.

print("predicted values are:")
(predicted_price, coefficient, constant) = predict_price(dates, mopen, 20171011)
print("The stock open price on 2017/10/11 is: $", str(predicted_price))
