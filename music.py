import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def music_prediction(music):
    X = music_data.drop(columns=['genre'])
    Y = music_data['genre']

    model = DecisionTreeClassifier()
    model.fit(X_train, Y_train)

    predictions = model.predict(X_test)

music_prediction(music)
