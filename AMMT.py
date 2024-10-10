import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import warnings

# Load the dataset from an Excel file
dataset = pd.read_excel("/Users/alesarabandi/Downloads/org.xlsx")

# Specify independent variables (features) and the dependent variable (target)
predictors = ['Age', 'Gender', 'OutdoorJob', 'OutdoorActivities', 'SmokingHabit',
              'Humidity', 'Pressure', 'Temperature', 'UVIndex', 'WindSpeed']
X_data = dataset[predictors]
target = dataset['ACTScore']

# Split the dataset into training and testing sets (80% for training, 20% for testing)
X_train_data, X_test_data, y_train_data, y_test_data = train_test_split(X_data, target, test_size=0.2, random_state=42)

# Normalize the features for better performance
norm = StandardScaler()
X_normalized = norm.fit_transform(X_train_data)
X_test_normalized = norm.transform(X_test_data)

# Create and train a linear Support Vector Machine (SVM) model
svm_model = SVC(kernel='linear', random_state=42)
svm_model.fit(X_normalized, y_train_data)

# Create and train a Random Forest classifier
forest_model = RandomForestClassifier(n_estimators=100, random_state=42)
forest_model.fit(X_normalized, y_train_data)

# Make predictions using both models
svm_results = svm_model.predict(X_test_normalized)
forest_results = forest_model.predict(X_test_normalized)

# Print performance metrics for the SVM model
print("Results for SVM Classifier:")
print(f"Accuracy: {accuracy_score(y_test_data, svm_results):.4f}")
print("Classification Report:")
print(classification_report(y_test_data, svm_results))

# Print performance metrics for the Random Forest model
print("\nResults for Random Forest Classifier:")
print(f"Accuracy: {accuracy_score(y_test_data, forest_results):.4f}")
print("Classification Report:")
print(classification_report(y_test_data, forest_results))
