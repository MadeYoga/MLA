from mla.algos.Classification.Neighbors import KNeighborsClassifier
from mla.algos.Preprocessing.Scaler import MinMaxScaler
from mla.algos.Preprocessing.LabelEncoder import LabelEncoder
import pandas as pd

dataset = pd.read_csv('Datasets/gwr.csv')
print(dataset.head())

X_train = dataset.loc[:, dataset.columns[:-1]]
y_train = dataset.loc[:, dataset.columns[-1:]]
print(X_train)
print(y_train)

## Preprocessing
encoder = LabelEncoder()
X_train['gender'] = encoder.fit_transform(X_train['gender'].values)

scaler = MinMaxScaler()
X_train['weight'] = scaler.transform(X_train['weight'])
X_train['gender'] = scaler.transform(X_train['gender'])

print(X_train)

## Create Model
knn = KNeighborsClassifier(n_neighbors=2)
## Train Model
knn.fit(X_train.values, y_train.values) ## pass numpy array instead of pandas DataFrame
## Predict
x_test = [[1, 0.3], [0, 0.4]]
pred_y = knn.predict([[1, 0.3], [0, 0.4]])
print("Prediction: " + str(pred_y))
y_test = ['high', 'high']
print("Actual Val: " + str(y_test))
## Model's Accuracy
from mla.algos.Metrics.Score import accuracy_score
print(str(accuracy_score(pred_y, y_test)) + "%")
