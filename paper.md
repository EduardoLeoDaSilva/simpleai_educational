---
title: 'SimpleAI: Logistic Regression from Scratch for Educational Use'
tags:
  - Python
  - machine learning
  - artificial intelligence
  - logistic regression
  - education
authors:
  - name: Eduardo Leonardo
    orcid: 0000-0000-0000-0000
    affiliation: 1
    corresponding: true
affiliations:
 - name: Independent Researcher
   index: 1
   ror: ""
date: 2025-07-11
---

# Summary

**SimpleAI** is a minimal Python package that implements logistic regression from scratch using only NumPy. Designed specifically for educational purposes, it aims to help students understand the fundamentals of binary classification, gradient descent, and the inner workings of machine learning algorithms without the abstraction of high-level libraries.

# Statement of Need

Many students and newcomers to artificial intelligence face a steep learning curve due to the complexity and abstraction of modern machine learning libraries like scikit-learn, TensorFlow, or PyTorch. **SimpleAI** addresses this gap by providing:

- A readable and minimal implementation of logistic regression
- A codebase that can be easily modified for experiments and exercises
- A lightweight environment with minimal dependencies, ideal for teaching

This makes it highly suitable for university courses, tutorials, and workshops on machine learning fundamentals.

# Installation

```bash
pip install -e .
```

# Example

```python
from simpleai.model import LogisticRegression
model = LogisticRegression(learning_rate=0.1, iterations=1000)
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```

# Educational Use Cases

- Teaching the principles of gradient descent
- Visualizing decision boundaries in 2D
- Demonstrating overfitting and regularization manually
- Guiding students to extend the model to multi-class classification

# Acknowledgements

Inspired by teaching experiences and student needs in introductory AI and ML courses.