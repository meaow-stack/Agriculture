import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Streamlit app title
st.title("Climate and Crop Data Viewer And Prediction using LinearRegression algo")

# Load and clean the climate data
@st.cache_resource
def load_and_clean_data():
    # Load the climate.csv file
    climate_data = pd.read_csv('climate-ds.csv')
    st.write("Raw Climate Data (Original):")
    st.dataframe(climate_data)
    
    # Display column names to debug
    #col = climate_data.columns
    #st.write("### The columns are:")
    
    # Convert column names to a DataFrame for row-wise display
    #col_df = pd.DataFrame(col, columns=['Column Names'])
    #st.dataframe(col_df)
    
    # Clean the data
    climate_data_cleaned = climate_data.drop_duplicates()
    
    # Remove unnecessary columns like 'Unnamed: 0'
    if 'Unnamed: 0' in climate_data_cleaned.columns:
        climate_data_cleaned = climate_data_cleaned.drop(columns=['Unnamed: 0'])
    
    # Drop rows with missing values in non-numeric columns
    climate_data_cleaned.dropna(subset=climate_data_cleaned.select_dtypes(exclude=['float64', 'int64']).columns, inplace=True)
    
    # Standardize column names (lowercase and remove spaces)
    climate_data_cleaned.columns = climate_data_cleaned.columns.str.lower().str.replace(' ', '_')
    
    return climate_data_cleaned

# Load the cleaned climate data
climate_data_cleaned = load_and_clean_data()

# Display the cleaned data
st.write("Cleaned Climate Data:")
st.dataframe(climate_data_cleaned)

# Display basic statistics of the cleaned data
st.write("Basic Statistics of Cleaned Climate Data:")
st.write(climate_data_cleaned.describe())

# Define features and target
features = climate_data_cleaned[['avg_temp', 'average_rain_fall_mm_per_year', 'year']]
target = climate_data_cleaned['hg/ha_yield']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Initialize and train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Display model results in Streamlit
st.write("Model Performance Metrics:")
st.write(f"Mean Squared Error: {mse:.2f}")
st.write(f"R² Score: {r2:.2f}")

# Create a container for the input and prediction
with st.container():
    # Create two columns
    col1, col2 = st.columns([1, 4])  # Adjust the column width ratio as needed

    # Inputs in the left column
    with col1:
        st.write("Make New Predictions:")
        temp_input = st.number_input("Enter temperature (in degrees):", value=0.0)
        rain_input = st.number_input("Enter rainfall (mm per year):", value=0.0)
        year_input = st.number_input("Enter year:", value=2024)  # Adjusted to match the feature column

        # Predict using new user input
        if st.button('Predict'):
            try:
                new_data = pd.DataFrame([[temp_input, rain_input, year_input]], columns=['avg_temp', 'average_rain_fall_mm_per_year', 'year'])
                prediction = model.predict(new_data)
                st.write(f"Predicted Crop Yield: {prediction[0]:.2f}")
            except Exception as e:
                st.error(f"Error: {e}")

    # Optional: You can add other content or results in the right column
    with col2:
        st.write("Additional Content or Results:",)
        # This column can be used for other content or results
        # You can leave it empty or add any other elements you wish

# Thumbs-up button
if st.button('👍 Thumbs Up'):
    st.write("Thank you for the thumbs up!")
