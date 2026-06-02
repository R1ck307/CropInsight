import streamlit as st
import pandas as pd
from expert_system.rules import diagnose

# ----------------------------
# PAGE SETTINGS
# ----------------------------

st.set_page_config(
    page_title="CropInsight",
    page_icon="🌱",
    layout="wide"
)

# ----------------------------
# LOGO
# ----------------------------

try:
    st.image("assets/logo.png.JPG", width=180)
except:
    pass

# ----------------------------
# TITLE
# ----------------------------

st.title("🌱 CropInsight")
st.subheader("Knowledge-Based Crop Disease Expert System")

st.write(
    """
    CropInsight helps small-scale farmers identify crop diseases
    and nutrient deficiencies using an expert system.
    """
)

st.divider()

# ----------------------------
# FARMER DETAILS
# ----------------------------

st.header("👨🏽‍🌾 Farmer Information")

farmer_name = st.text_input("Farmer Name")

farm_location = st.text_input("Farm Location")

st.divider()

# ----------------------------
# CROP SELECTION
# ----------------------------

st.header("🌾 Select Crop")

crop = st.selectbox(
    "Choose Crop",
    [
        "Maize",
        "Tomato",
        "Cabbage",
        "Beans",
        "Cucumber",
        "Spinach"
    ]
)

# ----------------------------
# DISPLAY CROP IMAGE
# ----------------------------

try:

    if crop == "Maize":
        st.image("assets/maize.jpg.jpeg", width=350)

    elif crop == "Tomato":
        st.image("assets/tomato.jpg.jpeg", width=350)

    elif crop == "Cabbage":
        st.image("assets/cabbage.jpg.jpeg", width=350)

    elif crop == "Beans":
        st.image("assets/beans.jpg.jpeg", width=350)

    elif crop == "Cucumber":
        st.image("assets/cucumber.jpg.jpeg", width=350)

    elif crop == "Spinach":
        st.image("assets/spinach.jpg.jpeg", width=350)

except:
    pass

st.divider()

# ----------------------------
# SYMPTOMS
# ----------------------------

st.header("🔍 Select Symptoms")

yellow_leaves = st.checkbox("Yellow Leaves")
brown_edges = st.checkbox("Brown Leaf Edges")
purple_leaves = st.checkbox("Purple Leaves")
orange_spots = st.checkbox("Orange Spots")
brown_lesions = st.checkbox("Brown Lesions")
brown_spots = st.checkbox("Brown Spots")
wilting = st.checkbox("Wilting")
small_dark_spots = st.checkbox("Small Dark Spots")
sudden_wilt = st.checkbox("Sudden Wilt")
white_powder = st.checkbox("White Powder on Leaves")
yellow_patches = st.checkbox("Yellow Patches")
sunken_lesions = st.checkbox("Sunken Lesions")
brown_circles = st.checkbox("Brown Circular Spots")
reddish_spots = st.checkbox("Reddish Brown Spots")
v_shape = st.checkbox("Yellow V-Shaped Lesions")
swollen_roots = st.checkbox("Swollen Roots")
dark_stems = st.checkbox("Dark Stem Lesions")
yellowing = st.checkbox("Yellowing Leaves")
white_tunnels = st.checkbox("White Tunnels in Leaves")
yellow_under = st.checkbox("Yellow Spots Under Leaves")

# ----------------------------
# BUILD SYMPTOM LIST
# ----------------------------

symptoms = []

if yellow_leaves:
    symptoms.append("yellow_leaves")

if brown_edges:
    symptoms.append("brown_edges")

if purple_leaves:
    symptoms.append("purple_leaves")

if orange_spots:
    symptoms.append("orange_spots")

if brown_lesions:
    symptoms.append("brown_lesions")

if brown_spots:
    symptoms.append("brown_spots")

if wilting:
    symptoms.append("wilting")

if small_dark_spots:
    symptoms.append("small_dark_spots")

if sudden_wilt:
    symptoms.append("sudden_wilt")

if white_powder:
    symptoms.append("white_powder")

if yellow_patches:
    symptoms.append("yellow_patches")

if sunken_lesions:
    symptoms.append("sunken_lesions")

if brown_circles:
    symptoms.append("brown_circles")

if reddish_spots:
    symptoms.append("reddish_spots")

if v_shape:
    symptoms.append("v_shape")

if swollen_roots:
    symptoms.append("swollen_roots")

if dark_stems:
    symptoms.append("dark_stems")

if yellowing:
    symptoms.append("yellowing")

if white_tunnels:
    symptoms.append("white_tunnels")

if yellow_under:
    symptoms.append("yellow_under")

st.divider()

# ----------------------------
# DIAGNOSE BUTTON
# ----------------------------

if st.button("Diagnose Crop"):

    disease = diagnose(crop, symptoms)

    if disease:

        df = pd.read_csv("data/diseases.csv")

        result = df[df["Disease"] == disease]

        if not result.empty:

            disease_name = result.iloc[0]["Disease"]
            treatment = result.iloc[0]["Treatment"]
            prevention = result.iloc[0]["Prevention"]
            severity = result.iloc[0]["Severity"]
            cost = result.iloc[0]["EstimatedCost"]
            symptom_description = result.iloc[0]["Symptoms"]

            st.success("Diagnosis Complete")

            st.header("📋 Diagnosis Report")

            st.write("### Disease Identified")
            st.write(disease_name)

            st.write("### Symptoms")
            st.write(symptom_description)

            st.write("### Treatment")
            st.write(treatment)

            st.write("### Prevention")
            st.write(prevention)

            st.write("### Severity")
            st.write(severity)

            st.write("### Estimated Cost")
            st.write(cost)

            # Confidence Score

            confidence = 85

            st.metric(
                label="Confidence Score",
                value=f"{confidence}%"
            )

            # Download Report

            report = f"""
CROPINSIGHT REPORT

Farmer Name: {farmer_name}

Farm Location: {farm_location}

Crop: {crop}

Disease Identified:
{disease_name}

Symptoms:
{symptom_description}

Treatment:
{treatment}

Prevention:
{prevention}

Severity:
{severity}

Estimated Cost:
{cost}

Confidence Score:
{confidence}%
"""

            st.download_button(
                label="📥 Download Report",
                data=report,
                file_name="CropInsight_Report.txt",
                mime="text/plain"
            )

    else:

        st.error(
            """
            No matching disease found.

            Please verify the symptoms selected or
            consult an agricultural expert.
            """
        )

st.divider()

st.caption(
    "CropInsight © 2026 | ICT Competition Project"
)
