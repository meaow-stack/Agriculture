import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import streamlit as st
from PIL import Image
import warnings
warnings.filterwarnings('ignore')

# Streamlit Title and Description
st.title("Climate and Crop Prediction")
st.write("""
This application allows you to upload climate and crop data, train a Random Forest model, and predict crop types based on climate conditions.
""")

# Load and display image
try:
    img = Image.open("crop.png")
    st.image(img)
except FileNotFoundError:
    st.warning("Image file not found. Please ensure 'crop.png' is in the working directory.")

# Upload the Dataset
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Load the dataset
    df = pd.read_csv(uploaded_file)

    # Display the raw data
    st.subheader("Raw Data")
    st.write(df.head())

    # Remove unnecessary columns
    df_cleaned = df.drop(columns=['Unnamed: 0'], errors='ignore')

    st.subheader("Cleaned Data")
    st.write(df_cleaned)

    # Encode categorical variables: "Area" (feature) and "Item" (target)
    label_encoder_area = LabelEncoder()
    df_cleaned['Area'] = label_encoder_area.fit_transform(df_cleaned['Area'])

    label_encoder_item = LabelEncoder()
    df_cleaned['Item'] = label_encoder_item.fit_transform(df_cleaned['Item'])

    # Define features (X) and target (y)
    X = df_cleaned.drop(columns=['Item'])
    y = df_cleaned['Item']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize and train the RandomForest classifier
    rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_classifier.fit(X_train, y_train)

    # Predict on the test set
    y_pred = rf_classifier.predict(X_test)

    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    conf_matrix = confusion_matrix(y_test, y_pred)
    class_report = classification_report(y_test, y_pred, output_dict=True)

    # Display Results
    st.subheader("Model Performance")
    st.write(f"**Accuracy:** {accuracy:.2f}")

    st.subheader("Confusion Matrix")
    st.write(pd.DataFrame(conf_matrix, 
                          index=label_encoder_item.classes_, 
                          columns=label_encoder_item.classes_))

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
    st.subheader("Predict Crop Type Based on Climate Conditions")

    # Create input fields for each feature
    area_input = st.selectbox("Select Area", label_encoder_area.inverse_transform(df_cleaned['Area'].unique()))
    other_features = {col: None for col in X.columns if col != 'Area'}
    for column in other_features:
        if X[column].dtype == 'int64':  # If the column is of integer type
            value = st.number_input(f"Enter {column}", min_value=int(X[column].min()), max_value=int(X[column].max()), step=1)
        else:  # If the column is of float type
            value = st.number_input(f"Enter {column}", min_value=float(X[column].min()), max_value=float(X[column].max()))
        other_features[column] = value

    # Convert user input into the same format as the training data
    area_encoded = label_encoder_area.transform([area_input])[0]
    user_input_features = [area_encoded] + [other_features.get(col, 0) for col in X.columns if col != 'Area']

    # Predict Crop Type
    if st.button("Predict Crop Type"):
        user_input_df = pd.DataFrame([user_input_features], columns=X.columns)
        prediction = rf_classifier.predict(user_input_df)
        predicted_crop = label_encoder_item.inverse_transform(prediction)[0]

        # Display the Prediction
        st.write(f"**Predicted Crop Type:** {predicted_crop}")

else:
    st.info("Awaiting for CSV file to be uploaded.")
