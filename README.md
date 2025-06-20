# 🌾 Crop Yield Prediction using Machine Learning

A web-based machine learning application that predicts the **crop yield** based on environmental and agricultural factors such as average rainfall, temperature, pesticide usage, and location. The project utilizes a trained Decision Tree Regressor model and Flask for deployment.

---

## 🧠 Overview

This project aims to help farmers, researchers, and agribusinesses estimate crop yield based on past trends and present inputs, thereby enabling better planning and resource allocation.

---

## 📁 Project Structure

```
crop-yield-prediction/
│
├── app.py                       # Flask web application
├── CropYield-Prediction.ipynb  # Jupyter notebook (EDA + model training)
├── dtr.pkl                      # Trained Decision Tree Regressor model
├── preprocessor.pkl             # Preprocessing pipeline (Label Encoding, Scaling, etc.)
├── yield_df.csv                 # Dataset used for training
├── requirements.txt             # Python dependencies
└── README.md                    # Project overview
```

---

## 🔍 Input Features

- **Year**
- **Average Rainfall (mm/year)**
- **Pesticide Usage (tonnes)**
- **Average Temperature (°C)**
- **Area** (e.g., country or region)
- **Item** (type of crop)

---

## 🎯 Output

- **Predicted Crop Yield**

---

## 🚀 How to Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/shaurya7303/crop-yield-prediction.git
   cd crop-yield-prediction
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask app**
   ```bash
   python app.py
   ```

5. **Open in browser**
   Navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000) to access the app.

---

## 🛠️ Tech Stack

- **Python**
- **Flask** (for web interface)
- **Scikit-learn** (for machine learning)
- **Pandas & NumPy** (for data manipulation)
- **Pickle** (for model serialization)

---

## 📊 Model Info

- **Algorithm**: Decision Tree Regressor
- **Preprocessing**: Label Encoding + Feature Scaling
- **Evaluation**: [add metrics from notebook here if needed]

---

## ✅ Example Usage

Enter values like:
- Year: `2015`
- Rainfall: `1100`
- Temperature: `22.3`
- Pesticides: `500`
- Area: `India`
- Item: `Rice`

And get an estimated yield for the given crop and location.

---

## 📌 Future Enhancements

- Add support for multiple crops or regions
- Connect to real-time weather API
- Build a dashboard with analytics
- Integrate with mobile app