import pandas as p
import matplotlib.pyplot as p1

from sklearn.cluster import KMeans
data = p.read_csv('Customers.csv') # getting dataset from customer.csv file
x = data.iloc[:, [3, 4]].values  # retriving annual income and spending scoure
km = KMeans(n_clusters = 5, init = 'k-means++', random_state = 10)  #applying k mean to dataset
y_km = km.fit_predict(x)
p1.scatter(x[y_km == 3, 0], x[y_km== 3, 1], s = 100, c = 'cyan', label = 'Cluster1')      #ploting cluster
p1.scatter(x[y_km == 0, 0], x[y_km == 0, 1], s = 100, c = 'blue', label = 'Cluster2')
p1.scatter(x[y_km == 4, 0], x[y_km == 4, 1], s = 100, c = 'magenta', label = 'Cluster3')
p1.scatter(x[y_km == 2, 0], x[y_km == 2, 1], s = 100, c = 'green', label = 'Cluster4')
p1.scatter(x[y_km == 1, 0], x[y_km == 1, 1], s = 100, c = 'red', label = 'Cluster5')
p1.scatter(km.cluster_centers_[:, 0], km.cluster_centers_[:, 1], s = 300, c = 'black', label = 'center')
p1.title('Clusters of customers')
p1.ylabel('Spending Score (1-100)')
p1.xlabel('Annual Income (k$)')

p1.legend()
p1.show()