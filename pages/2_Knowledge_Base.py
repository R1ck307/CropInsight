import streamlit as st
import pandas as pd

st.title("📚 CropInsight Knowledge Base")

st.write(
    """
    Search and browse crop diseases,
    treatments, prevention methods,
    severity levels and costs.
    """
)

df = pd.read_csv("data/diseases.csv")

search = st.text_input(
    "Search Disease"
)

if search:

    results = df[
        df["Disease"].str.contains(
            search,
            case=False,
            na=False
        )
    ]

    st.dataframe(results)

else:

    crop = st.selectbox(
        "Browse by Crop",
        sorted(df["Crop"].unique())
    )

    crop_data = df[df["Crop"] == crop]

    st.dataframe(crop_data)

    st.subheader("Disease Details")

    disease = st.selectbox(
        "Select Disease",
        crop_data["Disease"].unique()
    )

    selected = crop_data[
        crop_data["Disease"] == disease
    ].iloc[0]

    st.write("### Symptoms")
    st.write(selected["Symptoms"])

    st.write("### Treatment")
    st.write(selected["Treatment"])

    st.write("### Prevention")
    st.write(selected["Prevention"])

    st.write("### Severity")
    st.write(selected["Severity"])

    st.write("### Estimated Cost")
    st.write(selected["EstimatedCost"])
