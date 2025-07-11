import numpy as np
from simpleai.model import LogisticRegression

def test_training():
    X = np.array([[0.2, 0.8], [0.5, 0.4], [0.9, 0.5]])
    y = np.array([0, 0, 1])
    model = LogisticRegression(learning_rate=0.1, iterations=500)
    model.fit(X, y)
    predictions = model.predict(X)
    assert predictions.shape == y.shape