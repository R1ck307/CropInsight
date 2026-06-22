import streamlit as st


# -----------------------------
# CropInsight Configuration
# -----------------------------

st.set_page_config(
    page_title="CropInsight",
    page_icon="🌱",
    layout="wide"
)


# -----------------------------
# Session Management
# -----------------------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user" not in st.session_state:
    st.session_state.user = None


# -----------------------------
# Main App
# -----------------------------

st.title("🌱 CropInsight Smart Farming Platform")

st.write(
    """
    CropInsight is an AI-powered agricultural assistant
    designed to help farmers diagnose crop diseases,
    monitor crop health, and improve farming decisions.
    """
)


# -----------------------------
# Login Status
# -----------------------------

if st.session_state.logged_in:

    st.success(
        f"Welcome back {st.session_state.user} 🌱"
    )

    st.write(
        """
        Your farming profile is active.

        You can now:
        - Diagnose crops
        - Track farm records
        - View recommendations
        - Manage your farming data
        """
    )


else:

    st.info(
        """
        Welcome to CropInsight.

        Please create an account or login from the
        Login page to save your farming progress.
        """
    )


# -----------------------------
# Features Preview
# -----------------------------

st.subheader("🚜 CropInsight Features")

features = [
    "🌿 Crop Disease Diagnosis",
    "📷 Image Disease Detection",
    "🌦 Weather-Aware Farming Advice",
    "📊 Farm Health Dashboard",
    "🧪 Fertilizer Recommendations",
    "💧 Irrigation Advice",
    "📈 Yield Prediction",
    "🤖 AI Farming Assistant",
    "🌍 African Crop Knowledge Base"
]


for feature in features:
    st.write(feature)


# -----------------------------
# Footer
# -----------------------------

st.divider()

st.caption(
    "CropInsight | Smart Agriculture Platform 🌱"
)
