import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Load your data
df = pd.read_csv('health_data.csv')

# Encode text labels to numbers
label_mapping = {'Healthy': 0, 'Fever': 1, 'Hypoxia': 2, 'Unwell': 3}
df['Label'] = df['Label'].map(label_mapping)

# Separate features and label
X = df[['HeartRate', 'SpO2', 'Temperature', 'ECG']]
y = df['Label']

# Split into training & testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest Classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Evaluate
y_pred = clf.predict(X_test)
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Confusion Matrix
plt.figure(figsize=(6, 4))
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt="d", cmap="Blues",
            xticklabels=label_mapping.keys(), yticklabels=label_mapping.keys())
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.tight_layout()
plt.show()

# Save model (optional)
import joblib
joblib.dump(clf, 'health_rf_model.pkl')
