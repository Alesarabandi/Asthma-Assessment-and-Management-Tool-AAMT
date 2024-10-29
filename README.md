# Asthma-Assessment-and-Management-Tool-AAMT
The Asthma Assessment and Management Tool(AAMT) is a Python-based application designed to assist in the assessment and management of asthma symptoms. It leverages machine learning techniques to predict asthma-related outcomes based on various input features, including patient demographics, environmental factors, and health indicators.

# Framework

![photo-output 2](https://github.com/user-attachments/assets/b2cc9985-0b44-40df-8ced-912789b9c99d)


# Features

User Friendly Interface: Built with Tkinter for easy input and output interaction.

Machine Learning Models: Trained using Support Vector Machines (SVM) and Random Forest classifiers to provide reliable assesment.

Custom Medicine Recommendations: Based on prediction scores, the tool offers tailored medication and natural remedy suggestions for users.

Data Handling: Utilizes Pandas for data manipulation and Excel for input data sources, ensuring seamless integration of patient data.

# How It Works

Input Collection: Users enter their information through a series of input fields related to age, gender, outdoor job exposure, smoking habits, humidity, temperature, and other relevant factors.

Model Training: The application trains the machine learning models using historical data stored in an Excel file.

Prediction: Upon clicking the "Predict" button, the app evaluates the input against the trained models and displays predictions along with recommended treatments.

Medicine Guidance: Based on the average prediction score from both models, the app suggests appropriate medications and natural remedies, along with important side effect information.

<img width="786" alt="Screenshot 2024-10-11 at 14 50 20" src="https://github.com/user-attachments/assets/1b89e85e-76d4-4c93-acc9-d60c02969572">


# Tools Used

Programming Language: Python

Libraries: Tkinter, Pandas, Scikit-learn

Machine Learning: Support Vector Machines, Random Forest
