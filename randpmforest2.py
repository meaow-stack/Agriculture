import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import streamlit as st
from PIL import Image

# Streamlit Title and Description
st.title("Climate and Crop Prediction using for INDIA(WE HAVE DATA TILL 2014)")
st.write("""
This application analyzes the given dataset, trains model, and predicts crop types based on climate conditions.
""")

try:
    img = Image.open("crop.png")
    st.image(img)
except FileNotFoundError:
    st.warning("Image file not found. Please ensure 'crop.png' is in the working directory.")


# Load the provided dataset
df = pd.read_csv('produce.csv')

# Display the raw data
st.subheader("Raw Data")
st.write(df.head())

# Clean the dataset
# Step 1: Drop columns with excessive missing values (e.g., >50% missing)
missing_threshold = 0.5
columns_to_keep = df.loc[:, df.isnull().mean() < missing_threshold].columns
df_cleaned = df[columns_to_keep]

# Step 2: Drop categorical columns not useful for modeling (e.g., 'Frequency', 'Unit')
categorical_to_drop = ['Frequency', 'Unit']
df_cleaned = df_cleaned.drop(columns=[col for col in categorical_to_drop if col in df_cleaned.columns])

# Step 3: Drop rows with missing values (optional: imputation could be done here instead)
df_cleaned = df_cleaned.dropna()

# Display the cleaned data
st.subheader("Cleaned Data")
st.write(df_cleaned.head())

# Step 4: Encode the target variable ('Particulars') and prepare numerical features
label_encoder = LabelEncoder()
df_cleaned['Particulars'] = label_encoder.fit_transform(df_cleaned['Particulars'])

# Separate features (X) and target (y)
X = df_cleaned.drop(columns=['Particulars'])
y = df_cleaned['Particulars']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the RandomForest classifier
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier.fit(X_train, y_train)

# Predict on the test set
y_pred = rf_classifier.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred, labels=sorted(y.unique()))  # Use all unique classes for consistency
class_report = classification_report(y_test, y_pred, output_dict=True)

# Display Results
st.subheader("Model Performance")
st.write(f"**Accuracy:** {accuracy:.2f}")

# Handle Confusion Matrix Display
class_names = label_encoder.inverse_transform(sorted(y.unique()))  # Map back to original class names
st.subheader("Confusion Matrix")
st.write(pd.DataFrame(conf_matrix, 
                      index=class_names, 
                      columns=class_names))

# Display Classification Report
st.subheader("Classification Report")
st.write(pd.DataFrame(class_report).transpose())

# Add feature importances visualization
st.subheader("Feature Importances")
feature_importances = pd.Series(rf_classifier.feature_importances_, index=X.columns)
st.bar_chart(feature_importances.sort_values(ascending=False))

# Plot histograms for each numeric feature
st.subheader("Feature Distribution - Histograms")
numeric_columns = X.select_dtypes(include=['float64', 'int64']).columns

# Plot histograms for each numerical feature
for column in numeric_columns:
    plt.figure(figsize=(6, 4))
    plt.hist(X[column], bins=30, edgecolor='k', alpha=0.7)
    plt.title(f'Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    st.pyplot(plt)
    plt.close()

# User Input for Prediction
st.subheader("Predict Crop Type Based on Climate Conditions over the year")

# Create input fields for each feature
feature_inputs = {}
for column in X.columns:
    if X[column].dtype == 'int64':  # If the column is of integer type
        value = st.number_input(f"Enter {column}", min_value=int(X[column].min()), max_value=int(X[column].max()), step=1)
    else:  # If the column is of float type
        value = st.number_input(f"Enter {column}", min_value=float(X[column].min()), max_value=float(X[column].max()))
    feature_inputs[column] = value

# Convert user input into a DataFrame
user_input_df = pd.DataFrame([feature_inputs])

# Predict Crop Type
if st.button("Predict Crop Type"):
    if user_input_df.shape[1] == X.shape[1]:
        prediction = rf_classifier.predict(user_input_df)
        predicted_crop = label_encoder.inverse_transform(prediction)[0]
        st.write(f"**Predicted Crop Type:** {predicted_crop}")
    else:
        st.error("Mismatch between the number of features provided and the number of features expected by the model.")
