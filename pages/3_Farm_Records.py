import streamlit as st
import pandas as pd

st.title("📊 Farm Records Dashboard")

try:

    records = pd.read_csv(
        "data/records.csv"
    )

except:

    st.warning(
        "No records available."
    )

    st.stop()

st.subheader("Diagnosis Records")

st.dataframe(records)

st.divider()

total_records = len(records)

st.metric(
    "Total Diagnoses",
    total_records
)

if total_records > 0:

    common_disease = (
        records["Disease"]
        .value_counts()
        .idxmax()
    )

    st.metric(
        "Most Common Disease",
        common_disease
    )

    common_crop = (
        records["Crop"]
        .value_counts()
        .idxmax()
    )

    st.metric(
        "Most Diagnosed Crop",
        common_crop
    )

st.divider()

st.subheader("Recent Diagnoses")

st.dataframe(
    records.tail(10)
)
