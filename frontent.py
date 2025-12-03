import streamlit as st
import requests

API_URL = "http://34.226.152.222:8000/predict"

st.title("Insurance Premium Category Predictor")
st.write("Fill in your details to get the predicted insurance premium category.")

# ----------------------------
# Input Fields
# ----------------------------
age = st.number_input("Age", min_value=1, max_value=119, value=30)
weight = st.number_input("Weight (kg)", min_value=1.0, max_value=300.0, value=65.0)
height = st.number_input("Height (m)", min_value=0.5, max_value=2.5, value=1.70)
income_lpa = st.number_input("Annual Income (LPA)", min_value=0.1, max_value=100.0, value=10.0)

smoker = st.radio("Are you a smoker?", options=[False, True], format_func=lambda x: "Yes" if x else "No")

city = st.text_input("City", value="Mumbai")

occupation = st.selectbox(
    "Occupation",
    [
        'retired', 'freelancer', 'student', 'government_job',
        'business_owner', 'unemployed', 'private_job'
    ]
)

# ----------------------------
# Predict Button
# ----------------------------
if st.button("Predict Premium Category"):
    input_data = {
        "age": age,
        "weight": weight,
        "height": height,
        "income_lpa": income_lpa,
        "smoker": smoker,
        "city": city,
        "occupation": occupation
    }

    st.write("Sending data to API...")
    st.json(input_data)

    try:
        response = requests.post(API_URL, json=input_data, timeout=10)

        if response.status_code == 200:
            result = response.json()

            prediction = result.get("predicted_category")

            if prediction:
                st.success(f"Predicted Insurance Premium Category: **{prediction}**")
            else:
                st.error("API returned unexpected response format.")
                st.json(result)

        else:
            st.error(f"API Error {response.status_code}")
            st.write(response.text)

    except requests.exceptions.ConnectionError:
        st.error("❌ Could not connect to the FastAPI server. Make sure it's running and accessible.")
    except requests.exceptions.Timeout:
        st.error("⏳ Request timed out. Try again.")
    except Exception as e:
        st.error(f"Unexpected error: {e}")
