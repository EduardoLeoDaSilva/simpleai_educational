import numpy as np
from simpleai.model import LogisticRegression

# Dados fictícios para demonstração
X = np.array([[0.1, 1.1], [1.2, 0.9], [0.9, 1.5], [1.0, 1.0]])
y = np.array([0, 1, 1, 0])

model = LogisticRegression(learning_rate=0.1, iterations=1000)
model.fit(X, y)
print(model.predict(X))