from sklearn import cross_validation as c
from sklearn import datasets
from sklearn import svm
from sklearn.metrics import accuracy_score

dataset = datasets.load_breast_cancer()
X = dataset.data
y = dataset.target
X_train,X_test,y_train,y_test=c.train_test_split(X,y,test_size=0.2)

# SVM with linear kernel
ml=svm.SVC(kernel='linear')
svc = ml.fit(X_train, y_train)
y_predict=ml.predict(X_test)
print('SVM with linear kernel accuracy score',accuracy_score(y_test,y_predict))


# SVM with RBF kernel
m2=svm.SVC(kernel='rbf')
rbf_svc = m2.fit(X_train, y_train)
y_predict=m2.predict(X_test)
print('SVM with rbf kernel accuracy score',accuracy_score(y_test,y_predict))


