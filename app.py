import streamlit as st
import joblib

st.title("Phishing URL Detection")

st.write("Enter URL features to predict whether the URL is Legitimate or Phishing.")

# Load the trained model
model = joblib.load("phishing_url_knn_model.pkl")

# Load the feature list
feature_columns = joblib.load("feature_columns.pkl")

st.write("Model loaded successfully.")
st.write("Number of features:", len(feature_columns))

st.subheader("Enter URL Features")

inputs = {}

for feature in feature_columns:
    inputs[feature] = st.number_input(
        feature,
        value=0.0
    )

if st.button("Predict"):
    input_data = [[inputs[feature] for feature in feature_columns]]

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("⚠️ Phishing URL")
    else:
        st.success("✅ Legitimate URL")