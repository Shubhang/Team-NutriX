from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from sklearn.svm import LinearSVC
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_classification

dataset = read_csv("NEW-data_recipev2.csv")
array = dataset.values
X = array[:,1:3]
y = array[:,3]
X_train, X_validation, Y_train, Y_validation = train_test_split(X, y, test_size=0.20, random_state=1, shuffle=True)
LSVC = LinearSVC()
LSVC.fit(X_train,Y_train)
y2_LSVC_model = LSVC.predict(X_validation)
print("LSVC Accurary:",accuracy_score(Y_validation,y2_LSVC_model)) 
