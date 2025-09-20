from sklearn.model_selection import train_test_split 
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier 
from sklearn import metrics 
import pandas as pd

iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=22) 

print("X_train shape:", X_train.shape) 
print("X_test shape:", X_test.shape) 
print("y_train shape:", y_train.shape) 
print("y_test shape:", y_test.shape) 

knn = KNeighborsClassifier(n_neighbors=3) 
knn.fit(X_train, y_train) 

y_pred = knn.predict(X_test) 
print("First 5 predictions:", y_pred[:15]) 
print("First 5 actual values:", y_test[:15]) 

accuracy = metrics.accuracy_score(y_test, y_pred) 
print(f"Accuracy: {accuracy * 100:.2f}%") 
print("\nClassification Report:") 
print(metrics.classification_report(y_test, y_pred, target_names=iris.target_names)) 

# Create a confusion matrix 
print("\nConfusion Matrix:") 
print(metrics.confusion_matrix(y_test, y_pred)) 
