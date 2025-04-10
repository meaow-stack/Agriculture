# 🌾 SmartCrop - Intelligent Crop Recommendation System using ML

**SmartCrop** is an AI-powered crop recommendation platform designed to assist farmers and agri-enthusiasts in making **data-driven decisions** about what crops to grow based on real-time and historical environmental conditions. It merges the power of **Machine Learning** with an elegant and intuitive **frontend (React + Bootstrap)** and a **Python backend powered by Streamlit**. The app is responsive, theme-adaptive (light/dark mode), and includes a unique **India Exclusive section** for region-specific insights.
---

## 📌 Table of Contents

- [🌐 Live Demo](#)(will be added)
- [📦 Tech Stack](#tech-stack)
- [🧠 ML Algorithm](#ml-algorithm)
- [🖥️ UI/UX Features](#uiux-features)
- [🇮🇳 India Exclusive Section](#india-exclusive)
- [📸 Screenshots](#screenshots)
- [🛠️ How to Run](#how-to-run-the-project)
- [📂 Folder Structure](#folder-structure)
- [🗣️ User Feedback System](#user-feedback-system)
- [🔮 Future Prospects](#future-prospects)
- [🤝 Contribute](#contribute)
- [📄 License](#license)
- [👤 Author](#author)

---

## 🧰 Tech Stack

| Layer         | Tech Used                                              |
|---------------|--------------------------------------------------------|
| **Frontend**  | React.js, Bootstrap 5, Material UI, SweetAlert2        |
| **Backend**   | Python, Streamlit, Pandas                              |
| **ML Model**  | RandomForestClassifier (scikit-learn)                  |
| **Styling**   | SCSS, Bootstrap, Material UI themes                    |
| **Alerts**    | SweetAlert2 (SWL) for user confirmations               |
| **Storage**   | JSON (for reviews), CSV (for datasets)                 |

---
### 📊 Accuracy:
Achieved **~95% accuracy** on test data, with effective handling of outliers and missing values.


## 🧠 ML Algorithm

We leverage the **Random Forest Classifier**, a powerful ensemble learning algorithm ideal for classification problems.

### 🔍 Features Used:
- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature (°C)
- Humidity (%)
- pH Level
- Rainfall (mm)

### 🧪 Dataset:
The dataset is curated from **open government agricultural sources** and manually cleaned for optimal performance.

### 🔧 Model Highlights:
- Accuracy: ~95%
- Handles missing data robustly
- Low variance due to ensemble trees

---

## 🖥️ UI/UX Features

- 🌓 **Light/Dark Mode** – Seamless toggle for accessibility
- 🧭 **Intuitive Navigation** – Clean and structured routes
- 📱 **Mobile Responsive** – Works on phones, tablets, desktops
- 💬 **Live Feedback Form** – Real-time user feedback system
- 📊 **Graphical Output** – Displays predictions and suggestions with visual context

---

## 🇮🇳 India Exclusive

India has **diverse agro-climatic zones**, and SmartCrop offers region-specific insights via:

- State-wise crop advisories
- Recommended sowing periods
- Soil compatibility tips
- Rainfall and seasonal climate analysis
- **(Future)** Links to government schemes and mandi prices

---

## 📸 Screenshots


---
![Screenshot 2025-04-10 155930](https://github.com/user-attachments/assets/742b37b1-f71b-4ca4-9c49-f17220612a27)
![Screenshot 2025-04-10 155913](https://github.com/user-attachments/assets/a9efc93d-24d0-4712-8e2f-0888f47218a1)
![Screenshot 2025-04-10 155904](https://github.com/user-attachments/assets/7a647c84-8639-4225-899c-ed4968996af8)
![Screenshot 2025-04-10 155856](https://github.com/user-attachments/assets/044e6766-83f3-473d-8348-47ee24665377)
![Screenshot 2025-04-10 155847](https://github.com/user-attachments/assets/419ebb0a-299b-4a3d-adcc-83001394fb4e)
![Screenshot 2025-04-10 155208](https://github.com/user-attachments/assets/eff5b4f3-2b17-4fb0-a893-d1f985b92351)
![Screenshot 2025-04-10 155149](https://github.com/user-attachments/assets/c9fd5aa6-c415-446a-991d-0c5de13f5339)
![Screenshot 2025-04-10 155143](https://github.com/user-attachments/assets/80bcd3c0-c283-4c71-a81b-dd8b332668da)
![Screenshot 2025-04-10 155136](https://github.com/user-attachments/assets/52170de5-f98e-4ea8-b473-a48f84fb94d1)
![Screenshot 2025-04-10 155129](https://github.com/user-attachments/assets/9ccd795f-4300-4e01-bd8c-db6df0721d3c)
![Screenshot 2025-04-10 155123](https://github.com/user-attachments/assets/ad66cc70-4fd9-421a-a109-ef93bda58d6b)
![Screenshot 2025-04-10 155117](https://github.com/user-attachments/assets/d2b42272-4702-415e-8124-28fff7f957a9)
![Screenshot 2025-04-10 155101](https://github.com/user-attachments/assets/eee69156-a9f2-4ef9-b84c-6f8dda2b68b4)
![Screenshot 2025-04-10 155052](https://github.com/user-attachments/assets/5aa1d914-4237-4f0d-bc8a-ab95c9630bde)
![Screenshot 2025-04-10 155045](https://github.com/user-attachments/assets/3d2b091e-eb74-45a2-bddc-a36d3bfe9aa4)
![Screenshot 2025-04-10 155035](https://github.com/user-attachments/assets/c273aaee-5d08-409c-b773-0cb8911dfd7f)
![Screenshot 2025-04-10 155027](https://github.com/user-attachments/assets/edce7a86-64c4-4e2d-b94f-138f06c02132)
![Screenshot 2025-04-10 155018](https://github.com/user-attachments/assets/947f53ff-fcb2-47dc-a2d8-20f0ddb17060)
![Screenshot 2025-04-10 155011](https://github.com/user-attachments/assets/e1a52f97-e209-4f21-b91b-68b60ce97ccd)
![Screenshot 2025-04-10 155001](https://github.com/user-attachments/assets/5d312fd2-f8c6-4672-a634-4c0d642afa83)
![Screenshot 2024-11-17 123351](https://github.com/user-attachments/assets/6a28fe89-7432-48d9-af11-bb3ca53a358a)
![Screenshot 2024-11-17 122818](https://github.com/user-attachments/assets/13af13af-b03b-4102-bc10-45a6956dc035)
![Screenshot 2024-11-17 121645](https://github.com/user-attachments/assets/dd49462d-5580-4c03-971f-75bdef7ef2ca)
![Screenshot 2024-11-17 121607](https://github.com/user-attachments/assets/b589bc7a-e735-4ad0-ad9e-3708306ae750)
![Screenshot 2024-11-17 121531](https://github.com/user-attachments/assets/3da2adad-a010-43ca-82f3-dfaf5b9a9caf)
![Screenshot 2024-11-17 121454](https://github.com/user-attachments/assets/523f4200-7208-4a6d-b5f6-37cacdaff35e)
![Screenshot 2024-11-17 121351](https://github.com/user-attachments/assets/0f893072-ec4c-4810-b381-a5d0cfea30b5)
![Screenshot 2024-11-17 112544](https://github.com/user-attachments/assets/7a029c8c-77b8-46e7-8d0d-840c28ece73c)

```bash


## 🛠️ How to Run the Project

### 🧪 Backend - Streamlit (Python)

cd backend
pip install -r requirements.txt
streamlit run app.py
cd frontend
npm install
npm start
smartcrop/
├── backend/
│   ├── app.py               # Streamlit backend logic
│   ├── model/
│   │   └── crop_model.pkl   # Trained Random Forest model
│   └── utils/
│       └── helper.py
├── frontend/
│   ├── public/
│   └── src/
│       ├── components/
│       └── pages/
├── assets/
│   └── images/
├── feedback/
│   └── reviews.json         # User reviews stored here
├── README.md
└── requirements.txt
🗣️ User Feedback System
Users can provide feedback using a simple, styled form component. Feedbacks are:

✅ Collected anonymously or with a name

💾 Stored in a JSON file

🔁 Displayed dynamically on the homepage

🔮 Future Prospects
Here’s what the next iteration of SmartCrop may include:

🌍 Advanced Features
🔗 Integration with OpenWeatherMap / IMD APIs for real-time weather

📡 Satellite soil moisture & NDVI mapping for hyper-local predictions

🧭 GPS-based localization to auto-detect user region

🗣️ Multi-language Support
Add support for Hindi, Tamil, Bengali, and other Indian languages

Speech-to-text input for illiterate or semi-literate farmers

📲 Mobile App (React Native / Flutter)
Lightweight companion app for farmers in remote areas

📊 Admin Dashboard
View user statistics

Monitor prediction usage patterns

Manage feedback and crop dataset

📈 Data Enhancement
Incorporate real-time yield and price forecasting

Historical analysis and trend prediction

💬 Chatbot Assistant
AI-powered agri-assistant chatbot for 24/7 help

Pre-trained on Indian farming FAQs using Rasa / OpenAI

🤝 Contribute
We welcome community contributions! To get started:

Fork the repository

Create a new branch

Make your changes

Submit a PR

Feel free to open issues for suggestions or bug reports.

👤 Author
[Sayantan Mukherjee]
💼 AI & Full-Stack Developer
📧sayantanmukherjee000@gmail.com


🌱 “AI in Agriculture isn't the future – it's already growing today.”
– SmartCrop


---

Let me know if you'd like:
- A logo or landing page design
- Deployment guide (Streamlit + React on Heroku, Render, or Vercel)
- A documentation site for contributors

I'm happy to help with those next!

HERE ARE FEW SCREENSHOTS

![Screenshot 2024-11-17 123351](https://github.com/user-attachments/assets/bed921fb-4f7e-4359-91b9-bbe0b7194df0)
![Screenshot 2024-11-16 132202](https://github.com/user-attachments/assets/4f5f132a-d0e2-4e34-b4a9-5e393670505f)
![Screenshot 2024-11-16 131329](https://github.com/user-attachments/assets/eb487460-8df9-436a-88bb-b5878a300c7f)
![Screenshot 2024-11-16 131205](https://github.com/user-attachments/assets/b8bfe24b-dfb8-41b7-abc0-6424ab871488)
![Screenshot 2024-11-16 131115](https://github.com/user-attachments/assets/887e2f12-834b-4cdc-8043-b645961530b0)
![Screenshot 2024-11-16 130913](https://github.com/user-attachments/assets/53699356-0072-4e81-859b-3ba61092c297)
![Screenshot 2024-11-16 130107](https://github.com/user-attachments/assets/70c11c76-b53b-49c5-824f-c6c059dea1c5)
![Screenshot 2024-11-16 130002](https://github.com/user-attachments/assets/165ab8e6-7391-4dcc-ade8-061bc5a480bb)
![Screenshot 2024-11-16 125834](https://github.com/user-attachments/assets/7fb4e916-0c07-4a9b-8ff2-c5013466f56d)
![Screenshot 2024-11-16 125801](https://github.com/user-attachments/assets/c7683c8c-5a04-4e6b-a36e-2aa7f89a97ff)
![Screenshot 2024-11-16 125750](https://github.com/user-attachments/assets/ce5cf40e-b87e-4d03-b20d-216e63704e40)
![Screenshot 2024-11-16 125650](https://github.com/user-attachments/assets/170d49b4-c70c-44c9-8320-fd436a6a9aee)
![Screenshot 2024-11-16 125132](https://github.com/user-attachments/assets/8d347366-0e98-4fb3-bdbe-914355ef67e2)
![Screenshot 2024-11-16 124734](https://github.com/user-attachments/assets/c1ad4076-0f57-4d99-b9e6-8ff3a3b3974c)
![Screenshot 2024-11-16 124646](https://github.com/user-attachments/assets/f6f0eede-649c-42fa-a818-24e4d9606ce5)
![Screenshot 2024-09-04 144847](https://github.com/user-attachments/assets/d6a5031d-fa73-4b3a-a560-83f462c299d5)
![Screenshot 2024-09-04 144147](https://github.com/user-attachments/assets/dc95160d-d8cc-4ee6-aad8-a9f0cd52059e)
![Screenshot 2024-09-04 143244](https://github.com/user-attachments/assets/9ab919c8-c4f6-4c95-8309-b5ddf66e5bf1)
![Screenshot 2024-09-04 143229](https://github.com/user-attachments/assets/b0f77dca-a552-4ee5-83d9-07c538cb42b8)
![Screenshot 2024-09-04 130833](https://github.com/user-attachments/assets/e6ca1ad0-7125-452a-b805-630dd33daca7)
![Screenshot 2024-09-04 130741](https://github.com/user-attachments/assets/2a6baa85-02ee-482b-b673-8230a11a83e4)
![Screenshot 2024-09-04 124650](https://github.com/user-attachments/assets/91d90ad4-37e5-4083-a2ad-2e9d0dc301e9)
![Screenshot 2024-09-04 124431](https://github.com/user-attachments/assets/d5660cc0-fa29-4770-930a-2987aa6bc3f5)
![Screenshot 2024-09-04 124403](https://github.com/user-attachments/assets/37a188f7-f28d-4da1-adb1-119081f701d8)
![Screenshot 2024-09-04 124337](https://github.com/user-attachments/assets/2ea51b06-5ecb-498b-8c9e-f8887cc254ca)
![Screenshot 2024-09-04 124221](https://github.com/user-attachments/assets/8000fd42-916f-4a98-81b3-f820bbbdff1b)
![Screenshot 2024-09-04 123340](https://github.com/user-attachments/assets/0388a77b-3e82-4e07-b00a-7ea446cac9e1)


