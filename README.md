# SimpleAI

**SimpleAI** is an educational Python package that implements binary logistic regression from scratch using NumPy.

## 🎯 Purpose

This package is intended for:

- Students learning machine learning fundamentals
- Instructors teaching the math behind logistic regression
- Developers who want a clear, simple implementation of binary classification

## 🚀 Features

- No black boxes: everything is visible and modifiable
- No external ML dependencies
- Minimal code for maximum clarity
- Ideal for classroom and assignment use

## 📦 Installation

```bash
pip install -e .
```

## 🔍 Example

```python
from simpleai.model import LogisticRegression
model = LogisticRegression(learning_rate=0.1, iterations=1000)
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```

## 📘 License

MIT License