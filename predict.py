
Predict the data
y_pred=logreg.predict(X_test)
y_pred
print('Accuracy Score:',metrics.accuracy_score(y_test,y_pred))
print('Mean Absolute Error_logreg:', metrics.mean_absolute_error(y_test, y_pred).round(3))  
print('Mean Squared Error_logreg:', metrics.mean_squared_error(y_test, y_pred).round(3))  
print('Root Mean Squared Error_logreg:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)).round(3))
print('Variance_logreg:', r2_score(y_test, y_pred).round(3))
print("True Cancellation label:",y_test.values[0:15])
print("Predicted Cancellation label:",y_pred[0:15])
cm=metrics.confusion_matrix(y_test,y_pred)
print(cm)
print(metrics.recall_score(y_test[0:2],y_pred[0:2]))
print(metrics.precision_score(y_test[0:2],y_pred[0:2]))
print(classification_report(y_test,y_pred))
