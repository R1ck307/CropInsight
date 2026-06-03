import streamlit as st
import pandas as pd
from expert_system.rules import diagnose

st.title("🌾 Crop Diagnosis")

# -----------------------
# FARMER DETAILS
# -----------------------

st.header("Farmer Information")

farmer_name = st.text_input("Farmer Name")

farm_location = st.text_input("Farm Location")

# -----------------------
# CROP SELECTION
# -----------------------

st.header("Crop Details")

crop = st.selectbox(
    "Select Crop",
    [
        "Maize",
        "Tomato",
        "Cabbage",
        "Beans",
        "Cucumber",
        "Spinach"
    ]
)

# -----------------------
# CROP IMAGES
# -----------------------

try:

    if crop == "Maize":
        st.image("assets/maize.jpg.jpeg", width=300)

    elif crop == "Tomato":
        st.image("assets/tomato.jpg.jpeg", width=300)

    elif crop == "Cabbage":
        st.image("assets/cabbage.jpg.jpeg", width=300)

    elif crop == "Beans":
        st.image("assets/beans.jpg.jpeg", width=300)

    elif crop == "Cucumber":
        st.image("assets/cucumber.jpg.jpeg", width=300)

    elif crop == "Spinach":
        st.image("assets/spinach.jpg.jpeg", width=300)

except:
    pass

# -----------------------
# GROWTH STAGE
# -----------------------

growth_stage = st.selectbox(
    "Growth Stage",
    [
        "Seedling",
        "Vegetative",
        "Flowering",
        "Harvest"
    ]
)

# -----------------------
# SOIL TYPE
# -----------------------

soil_type = st.selectbox(
    "Soil Type",
    [
        "Sandy",
        "Clay",
        "Loam"
    ]
)

# -----------------------
# SYMPTOMS
# -----------------------

st.header("Symptoms")

yellow_leaves = st.checkbox("Yellow Leaves")
brown_edges = st.checkbox("Brown Leaf Edges")
purple_leaves = st.checkbox("Purple Leaves")
orange_spots = st.checkbox("Orange Spots")
brown_lesions = st.checkbox("Brown Lesions")
brown_spots = st.checkbox("Brown Spots")
wilting = st.checkbox("Wilting")
small_dark_spots = st.checkbox("Small Dark Spots")
sudden_wilt = st.checkbox("Sudden Wilt")
white_powder = st.checkbox("White Powder")
yellow_patches = st.checkbox("Yellow Patches")
sunken_lesions = st.checkbox("Sunken Lesions")
brown_circles = st.checkbox("Brown Circular Spots")
reddish_spots = st.checkbox("Reddish Brown Spots")
v_shape = st.checkbox("V-Shaped Lesions")
swollen_roots = st.checkbox("Swollen Roots")
dark_stems = st.checkbox("Dark Stem Lesions")
yellowing = st.checkbox("Yellowing")
white_tunnels = st.checkbox("White Tunnels")
yellow_under = st.checkbox("Yellow Spots Under Leaves")

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

# -----------------------
# DIAGNOSIS
# -----------------------

if st.button("Diagnose"):

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

            symptom_count = len(symptoms)

            if symptom_count >= 4:
                confidence = 95
            elif symptom_count >= 2:
                confidence = 80
            else:
                confidence = 60

            st.success("Diagnosis Complete")

            st.header("Diagnosis Results")

            st.write("### Disease")
            st.write(disease_name)

            st.write("### Treatment")
            st.write(treatment)

            st.write("### Prevention")
            st.write(prevention)

            st.write("### Severity")
            st.write(severity)

            st.write("### Estimated Cost")
            st.write(cost)

            st.metric(
                "Confidence Score",
                f"{confidence}%"
            )

            st.header("Expert Reasoning")

            st.write(
                f"""
                Crop Selected: {crop}

                Symptoms Selected:
                {', '.join(symptoms)}

                Rule Activated:
                {crop} + Symptoms

                Diagnosis:
                {disease_name}
                """
            )

            st.header("Treatment Timeline")

            st.write("Day 1: Apply treatment")
            st.write("Day 7: Inspect crop")
            st.write("Day 14: Reapply if necessary")
            st.write("Day 21: Monitor recovery")

            report = f"""
CROPINSIGHT REPORT

Farmer: {farmer_name}
Location: {farm_location}

Crop: {crop}
Growth Stage: {growth_stage}
Soil Type: {soil_type}

Disease: {disease_name}

Treatment:
{treatment}

Prevention:
{prevention}

Severity:
{severity}

Cost:
{cost}

Confidence:
{confidence}%
"""

            st.download_button(
                "Download Report",
                report,
                file_name="CropInsight_Report.txt"
            )
   # Save Record

try:

    records = pd.read_csv(
        "data/records.csv"
    )

except:

    records = pd.DataFrame(
        columns=[
            "Farmer",
            "Location",
            "Crop",
            "Disease",
            "Severity",
            "Date"
        ]
    )

new_record = pd.DataFrame(
    {
        "Farmer":[farmer_name],
        "Location":[farm_location],
        "Crop":[crop],
        "Disease":[disease_name],
        "Severity":[severity],
        "Date":[pd.Timestamp.today().date()]
    }
)

records = pd.concat(
    [records, new_record],
    ignore_index=True
)

records.to_csv(
    "data/records.csv",
    index=False
)

    else:

        st.error(
            "No matching disease found."
    )
