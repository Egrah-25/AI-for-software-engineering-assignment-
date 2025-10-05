# breast_cancer_priority_predictor.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, classification_report
from sklearn.datasets import load_breast_cancer

# Load and preprocess data
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target)

# Map targets to priority: 0 = Malignant (High Priority), 1 = Benign (Low Priority)
# We'll invert the labels so that 1 represents the critical class (Malignant)
y = (y == 0).astype(int)
priority_labels = {1: 'high', 0: 'low'}
y_named = y.map(priority_labels)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train a Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred) # Focuses on the 'high priority' class (1)

print("### Performance Metrics ###")
print(f"Accuracy: {accuracy:.4f}")
print(f"F1-Score (for 'high priority' class): {f1:.4f}")
print("\n### Detailed Report ###")
print(classification_report(y_test, y_pred, target_names=['low', 'high']))
