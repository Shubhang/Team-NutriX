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
from sklearn.feature_extraction import FeatureHasher
from sklearn.preprocessing import MultiLabelBinarizer
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt # for data visualization purposes
import seaborn as sns # for statistical data visualization

dataset = read_csv("data/NEW-data_recipe.csv",encoding='unicode_escape')

def convertToList(x):
    return x.replace(" ","").lower().split(',')

dataset['ingredients']=dataset['ingredients'].apply(convertToList)
dataset['Allergens']=dataset['Allergens'].apply(convertToList)
mlb = MultiLabelBinarizer(sparse_output=True)

def OneHotAllergens(df):
    v = df.Allergens.values
    l = [len(x) for x in v.tolist()]
    f, u = pd.factorize(np.concatenate(v))
    n, m = len(v), u.size
    i = np.arange(n).repeat(l)
    dummies = pd.DataFrame(
        np.bincount(i * m + f, minlength=n * m).reshape(n, m),
        df.index, u
    )
    return df.drop('Allergens', 1).join(dummies)

dataset=OneHotAllergens(dataset)
def OneHotIngredients(df):
    v = df.ingredients.values
    l = [len(x) for x in v.tolist()]
    f, u = pd.factorize(np.concatenate(v))
    n, m = len(v), u.size
    i = np.arange(n).repeat(l)
    dummies = pd.DataFrame(
        np.bincount(i * m + f, minlength=n * m).reshape(n, m),
        df.index, u
    )
    df.drop('ingredients',1)
    return df.drop('ingredients', 1).join(dummies,lsuffix='', rsuffix='2')
dataset=OneHotIngredients(dataset)
dietres = ['diabetes','highbloodpressure','halah','celiac','allergens','lactoseintolerance','vegan','vegetarian','none','kosher']
for allergenType in dietres:
    X = dataset.drop(dietres+['recipe_id','recipe_name'],axis=1)
    y = dataset[allergenType]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)

    cols = X_train.columns
    from sklearn.preprocessing import RobustScaler

    scaler = RobustScaler()

    X_train = scaler.fit_transform(X_train)

    X_test = scaler.transform(X_test)
    X_train = pd.DataFrame(X_train, columns=[cols])
    X_test = pd.DataFrame(X_test, columns=[cols])

    LSVC = LinearSVC()
    LSVC.fit(X_train,y_train)
    y2_LSVC_model = LSVC.predict(X_test)
    print("Perform analysis on:"+allergenType)
    print("LSVC Accurary:",accuracy_score(y_test,y2_LSVC_model)) 
    ('Training-set accuracy score: {0:0.4f}'. format(LSVC.score(X_train,y_train)))
    print('Test set score: {:.4f}'.format(LSVC.score(X_test, y_test)))
