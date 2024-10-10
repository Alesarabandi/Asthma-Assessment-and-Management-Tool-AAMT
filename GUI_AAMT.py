import tkinter as tk
from tkinter import ttk
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Function to train the machine learning models
def train_models(X_train, y_train):
    # Initialize and train a Support Vector Machine (SVM) classifier
    Support_Vector_Machines = SVC(kernel='linear', random_state=42)
    Support_Vector_Machines.fit(X_train, y_train)

    # Initialize and train a Random Forest classifier
    Random_forest = RandomForestClassifier(n_estimators=100, random_state=42)
    Random_forest.fit(X_train, y_train)

    return Support_Vector_Machines, Random_forest

# Function to make predictions about asthma based on input values
def predict_asthma(input_values, scaler, Support_Vector_Machines, Random_forest):
    input_df = pd.DataFrame([input_values], columns=labels)
    input_scaled = scaler.transform(input_df)  # Scale the input values
    svm_pred = Support_Vector_Machines.predict(input_scaled)    # Get prediction from SVM model
    rf_pred = Random_forest.predict(input_scaled)      # Get prediction from Random Forest model
    return svm_pred, rf_pred

# Create the main application window
root = tk.Tk()
root.title("Asthma Assessment and Management Tool (AAMT)")

# Create a frame to hold the main content of the application
main_frame = ttk.Frame(root, padding="20")
main_frame.grid(row=0, column=0, sticky="nsew")

# Create labels and input fields for the user to enter the feature values
labels = ['Age (  Above 50 → 5 ,41-50 → 4 ,19-30 → 3 ,31-40 → 2 )', 'Gender  ( Male → 1 , Female → 0)', 'OutdoorJob ( Rarely → 0 ,Occasionally → 1 ,Frequently → 2)', 'OutdoorActivities (Extremely likely → 1 , Neither likely nor unlikely → 2 , Not at all likely → 0)', 'SmokingHabit (Yes → 1 , No → 0)', 
          'Humidity', 'Pressure', 'Temperature', 'UVIndex (Extreme → 1 , Low → 0)', 'WindSpeed']
entries = {}
for i, label in enumerate(labels):
    ttk.Label(main_frame, text=label).grid(row=i, column=0, sticky="w")  # Create label for each feature
    entries[label] = ttk.Entry(main_frame)  # Create entry field for user input
    entries[label].grid(row=i, column=1, sticky="ew")  # Place entry field in the grid

# Load data from an Excel file and prepare features and target variable
data = pd.read_excel("/Users/alesarabandi/Downloads/simp.xlsx")
X = data[['Age (  Above 50 → 5 ,41-50 → 4 ,19-30 → 3 ,31-40 → 2 )', 'Gender  ( Male → 1 , Female → 0)', 'OutdoorJob ( Rarely → 0 ,Occasionally → 1 ,Frequently → 2)', 'OutdoorActivities (Extremely likely → 1 , Neither likely nor unlikely → 2 , Not at all likely → 0)', 'SmokingHabit (Yes → 1 , No → 0)', 
          'Humidity', 'Pressure', 'Temperature', 'UVIndex (Extreme → 1 , Low → 0)', 'WindSpeed']]
y = data['ACTScore']  # Define the target variable
X_train, _, y_train, _, = train_test_split(X, y, test_size=0.2, random_state=42)  # Split the data for training
scaler = StandardScaler()  # Initialize the scaler for normalization
scaler.fit(X_train)  # Fit the scaler to the training data
X_train, _, y_train, _, = train_test_split(X, y, test_size=0.2, random_state=42)  # Split the data again for scaling
Support_Vector_Machines, Random_forest = train_models(scaler.transform(X_train), y_train)  # Train the models

# Function to retrieve input values and display predictions
def display_prediction():
    input_values = [float(entries[label].get()) for label in labels]  # Collect input values from entry fields
    svm_pred, rf_pred = predict_asthma(input_values, scaler, Support_Vector_Machines, Random_forest)  # Make predictions
    svm_label.config(text=f"SVM Prediction: {svm_pred}")  # Update SVM prediction display
    rf_label.config(text=f"Random Forest Prediction: {rf_pred}")  # Update Random Forest prediction display

    avg_pred=(rf_pred+svm_pred)/2  # Calculate average prediction score
    # Display corresponding medicine recommendations based on average prediction score
    if 5 <= avg_pred <= 10:
        show_medicines_for_score_5_to_10()
    elif 10 < avg_pred <= 19:
        show_medicines_for_score_10_to_19()
    elif avg_pred > 19:
        show_medicines_for_score_above_19()

# Create a button that triggers the prediction function when clicked
predict_button = ttk.Button(main_frame, text="Predict", command=display_prediction)
predict_button.grid(row=len(labels)+1, columnspan=2, pady=10)  # Place button in the grid

# Create labels to display the results of the predictions
svm_label = ttk.Label(main_frame, text="")
svm_label.grid(row=len(labels)+2, columnspan=2, pady=5)  # Display SVM prediction label
rf_label = ttk.Label(main_frame, text="")
rf_label.grid(row=len(labels)+3, columnspan=2, pady=5)  # Display Random Forest prediction label

# Function to show recommended medicines for ACT Score 5 to 10
def show_medicines_for_score_5_to_10():
    info_text.set("For ACT Score 5 to 10:\n\n"
                  "Medicines:\n"
                  "- Short-Acting Beta Agonists (SABAs)\n"
                  "- Oral Corticosteroids\n"
                  "- Theophylline\n\n"
                  "Natural Remedies:\n"
                  "- Breathing Exercises\n"
                  "- Herbal Remedies\n"
                  "- Honey and Ginger Tea\n\n"
                  "Rare but serious side effects:\n"
                    "-Rapid or irregular heartbeat (palpitations)\n"
                    "-Tremor\n"
                    "-Nervousness or anxiety\n"
                    "-Dizziness\n"
                        "-Muscle cramps\n")

# Function to show recommended medicines for ACT Score 10 to 19
def show_medicines_for_score_10_to_19():
    info_text.set("For ACT Score 10 to 19:\n\n"
                  "Medicines:\n"
                  "- Inhaled Corticosteroids (ICS)\n"
                  "- Combination Inhalers\n"
                  "- Leukotriene Modifiers\n\n"
                  "Natural Remedies:\n"
                  "- Breathing Exercises\n"
                  "- Yoga\n"
                  "- Omega-3 Fatty Acids\n"
                  "- Quercetin\n\n"
                  "Rare but serious side effects:\n"
                "-Adrenal insufficiency (especially with long-term use of high doses)\n"
                "-Osteoporosis (bone thinning)\n"
                "-Growth suppression in children\n"
                "-Glaucoma or cataracts (with prolonged use at high doses)\n"
                "-Increased risk of infections\n")

# Function to show recommended medicines for ACT Score above 19
def show_medicines_for_score_above_19():
    info_text.set("For ACT Score >19:\n\n"
                  "Medicines:\n"
                  "- Long-Acting Beta Agonists (LABAs)\n"
                  "- Biologic Therapies\n"
                  "- Oral Corticosteroids (for exacerbations)\n\n"
                  "Natural Remedies:\n"
                  "- Breathing Exercises\n"
                  "- Yoga\n"
                  "- Acupuncture\n"
                  "- Lifestyle Modifications\n\n"
                  "Rare but serious side effects:\n"
                  "-Sore throat\n"
                    "-Hoarseness or voice changes\n"
                    "-Thrush (oral fungal infection)\n"
                 "-Cough\n"
                    "-Headache\n")

# Variable to hold the information text for medicine recommendations
info_text = tk.StringVar()
info_label = ttk.Label(main_frame, textvariable=info_text, wraplength=500)  # Create label for displaying info text
info_label.grid(row=20, columnspan=2)  # Place information label in the grid

# Start the main event loop of the application
root.mainloop()
