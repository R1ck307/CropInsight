import streamlit as st


# -----------------------------
# Crop Quality Analyzer
# -----------------------------

st.title("📊 Crop Quality Analyzer")


st.write(
    """
    Evaluate whether your crop is suitable
    for commercial selling based on quality factors.
    """
)


# -----------------------------
# Inputs
# -----------------------------

crop = st.selectbox(
    "Select Crop",
    [
        "Maize",
        "Tomato",
        "Beans",
        "Potato",
        "Cabbage",
        "Other"
    ]
)


size = st.slider(
    "Crop Size Quality",
    0,
    100,
    50
)


appearance = st.slider(
    "Appearance / Freshness",
    0,
    100,
    50
)


damage = st.slider(
    "Damage Level (%)",
    0,
    100,
    0
)


disease = st.selectbox(
    "Disease Status",
    [
        "No Disease",
        "Minor Disease",
        "Severe Disease"
    ]
)



# -----------------------------
# Analysis
# -----------------------------

if st.button("Analyze Crop Quality"):


    score = (
        (size * 0.35)
        +
        (appearance * 0.35)
        +
        ((100 - damage) * 0.20)
    )


    if disease == "Minor Disease":

        score -= 10


    elif disease == "Severe Disease":

        score -= 30



    # Keep score between 0 and 100

    score = max(
        0,
        min(
            score,
            100
        )
    )



    # Grade

    if score >= 85:

        grade = "A"

        status = "Ready for commercial market"


    elif score >= 65:

        grade = "B"

        status = "Suitable for local markets"


    else:

        grade = "C"

        status = "Needs improvement before selling"



    # -----------------------------
    # Report
    # -----------------------------

    st.divider()


    st.subheader(
        "🌱 CropInsight Quality Report"
    )


    st.metric(
        "Quality Score",
        f"{score:.1f}%"
    )


    st.metric(
        "Grade",
        grade
    )


    st.success(
        status
    )



    st.write(
        f"""
        **Crop:** {crop}

        **Recommendation:**

        Continue monitoring crop health and
        maintain good farming practices.
        """
)
