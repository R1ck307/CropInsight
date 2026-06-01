import streamlit as st
import pandas as pd

# Load database
df = pd.read_csv("diseases.csv")

st.set_page_config(
    page_title="CropInsight",
    page_icon="🌱"
)

st.title("🌱 CropInsight")
st.subheader("Crop Disease Expert System")

st.write(
    "Answer a few questions and CropInsight will diagnose the crop problem."
)

crop = st.selectbox(
    "Select Crop",
    ["Maize", "Tomato", "Cucumber", "Cabbage", "Beans"]
)

st.header("Symptoms")

yellow_leaves = st.checkbox("Yellow leaves")
brown_spots = st.checkbox("Brown spots")
white_powder = st.checkbox("White powder on leaves")
wilting = st.checkbox("Wilting")
brown_edges = st.checkbox("Brown leaf edges")
v_shape = st.checkbox("Yellow V-shaped lesions")

if st.button("Diagnose"):

    disease = None

    # Expert System Rules

    if crop == "Maize" and yellow_leaves:
        disease = "Nitrogen Deficiency"

    elif crop == "Maize" and brown_edges:
        disease = "Potassium Deficiency"

    elif crop == "Tomato" and brown_spots:
        disease = "Early Blight"

    elif crop == "Tomato" and wilting:
        disease = "Late Blight"

    elif crop == "Cucumber" and white_powder:
        disease = "Powdery Mildew"

    elif crop == "Cabbage" and v_shape:
        disease = "Black Rot"

    elif crop == "Beans" and brown_spots:
        disease = "Leaf Spot"

    if disease:

        result = df[df["Disease"] == disease]

        st.success("Diagnosis Complete")

        st.write(
            "### Disease Identified:"
        )

        st.write(
            result.iloc[0]["Disease"]
        )

        st.write(
            "### Symptoms:"
        )

        st.write(
            result.iloc[0]["Symptoms"]
        )

        st.write(
            "### Treatment:"
        )

        st.write(
            result.iloc[0]["Treatment"]
        )

    else:

        st.error(
            "No matching disease found. Please consult an agricultural expert."
        )
severity = st.select_slider(
    "Severity",
    ["Low", "Medium", "High"]
)
name = st.text_input("Farmer Name")
location = st.text_input("Farm Location")
st.download_button(
    "Download Report", report_text)
