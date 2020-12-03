Logistic Regression
from sklearn.model_selection import train_test_split 
from sklearn import metrics
from sklearn.metrics import r2_score,classification_report
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
Train and Test
X = data.drop(['previous_cancellations'], axis = 1)
y = data['previous_cancellations']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)
logreg = LogisticRegression(solver = 'lbfgs')
logreg.fit(X_train,y_train)
