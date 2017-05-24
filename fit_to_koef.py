
import numpy as np

from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from keras import regularizers

import matplotlib.pyplot as plt
from pandas import read_csv

from sklearn import preprocessing, metrics
from sklearn.cross_validation import train_test_split


data = read_csv('drivers/edges_5000.csv')
XX = data[['Edge', 'TimeStartEdge', 'Distance']]
y = data['Accidents']
X = preprocessing.scale(XX)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=11)


def create_model():
    model = Sequential()
    model.add(Dense(12, input_dim=X.shape[1], activation='relu'))
    model.add(Dense(6, activation='relu'))
    model.add(Dense(1, activation='sigmoid', kernel_regularizer=regularizers.l2(0.001), activity_regularizer=regularizers.l1(0.001)))
    model.compile(loss='binary_crossentropy', optimizer='adam',
                  metrics=['mae'])
    return model

def fit_model():
    model = KerasClassifier(build_fn=create_model, epochs=50, batch_size=10, verbose=0)
    # isotonic = CalibratedClassifierCV
    model.fit(X_train, y_train)
    prob_pos = model.predict_proba(X_test)[:,-1]
    model_score = metrics.brier_score_loss(y_test, prob_pos, pos_label=y.max())

    return model_score

if __name__=='__main__':
    print('Brier Score: ' + fit_model())
