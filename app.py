import streamlit as st

st.set_page_config(
    page_title="CropInsight",
    page_icon="🌱",
    layout="wide"
)

try:
    st.image("assets/logo.png.JPG", width=180)
except:
    pass

st.title("🌱 CropInsight")

st.header("Welcome to CropInsight")

st.write(
    """
    CropInsight is a knowledge-based expert system
    designed to help small-scale farmers identify
    crop diseases and nutrient deficiencies.
    """
)

st.info(
    """
    Use the navigation menu on the left
    to access Diagnosis, Knowledge Base,
    and Farm Records.
    """
)

st.subheader("Features")

st.write("✅ Expert System Diagnosis")
st.write("✅ Knowledge Base")
st.write("✅ Prevention Advice")
st.write("✅ Treatment Plans")
st.write("✅ Severity Assessment")
st.write("✅ Diagnosis Records")
