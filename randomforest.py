from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse, StreamingResponse
from pydantic import BaseModel
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import io
from fastapi.middleware import cors
import matplotlib.pyplot as plt

app = FastAPI()

# Initialize global variables for model and encoders
rf_classifier = None
label_encoder_area = None
label_encoder_item = None
X_columns = None

class PredictionRequest(BaseModel):
    Area: float
    Temperature: float
    Rainfall: float
    # Add other features as needed...

@app.post("/upload-data/")
async def upload_data(file: UploadFile = File(...)):
    global rf_classifier, label_encoder_area, label_encoder_item, X_columns
    
    # Read the uploaded file into a pandas DataFrame
    contents = await file.read()
    df = pd.read_csv(io.BytesIO(contents))
    
    # Clean the DataFrame
    df_cleaned = df.drop(columns=['Unnamed: 0'])
    
    # Encode categorical variables: "Area" (feature) and "Item" (target)
    label_encoder_area = LabelEncoder()
    df_cleaned['Area'] = label_encoder_area.fit_transform(df_cleaned['Area'])

    label_encoder_item = LabelEncoder()
    df_cleaned['Item'] = label_encoder_item.fit_transform(df_cleaned['Item'])

    # Define features (X) and target (y)
    X = df_cleaned.drop(columns=['Item'])
    y = df_cleaned['Item']
    X_columns = X.columns

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize and train the RandomForest classifier
    rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_classifier.fit(X_train, y_train)
    
    return JSONResponse(content={"message": "Model trained successfully."})

@app.post("/predict/")
def predict_crop(request: PredictionRequest):
    global rf_classifier, label_encoder_area, label_encoder_item, X_columns
    
    # Check if the model is trained
    if rf_classifier is None or label_encoder_area is None or label_encoder_item is None:
        return JSONResponse(content={"error": "Model is not trained."}, status_code=400)
    
    # Prepare input data
    area_encoded = label_encoder_area.transform([request.Area])[0]
    user_input_features = [area_encoded, request.Temperature, request.Rainfall]  # Add other features as needed
    
    # Predict Crop Type
    user_input_df = pd.DataFrame([user_input_features], columns=X_columns)
    prediction = rf_classifier.predict(user_input_df)
    predicted_crop = label_encoder_item.inverse_transform(prediction)[0]
    
    return JSONResponse(content={"predicted_crop": predicted_crop})

@app.get("/feature-importance/")
def get_feature_importance():
    global rf_classifier, X_columns
    
    # Check if the model is trained
    if rf_classifier is None:
        return JSONResponse(content={"error": "Model is not trained."}, status_code=400)

    # Get feature importances
    feature_importances = rf_classifier.feature_importances_
    
    # Plot histogram
    plt.figure(figsize=(10, 6))
    plt.barh(X_columns, feature_importances, color='skyblue')
    plt.xlabel('Feature Importance')
    plt.title('Feature Importance for Random Forest Classifier')

    # Save the plot to a BytesIO object
    img_bytes = io.BytesIO()
    plt.savefig(img_bytes, format='png')
    img_bytes.seek(0)
    
    # Return the image as a response
    return StreamingResponse(img_bytes, media_type="image/png")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
