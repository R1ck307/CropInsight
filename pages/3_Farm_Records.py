import streamlit as st
import pandas as pd
import os


FARM_FILE = "database/farms.csv"
RECORD_FILE = "data/records.csv"


# -----------------------------
# Check Login
# -----------------------------

if "logged_in" not in st.session_state or not st.session_state.logged_in:

    st.warning(
        "Please login first 🌱"
    )

    st.stop()



# -----------------------------
# Load Data
# -----------------------------

def load_farms():

    if os.path.exists(FARM_FILE):

        return pd.read_csv(FARM_FILE)

    return pd.DataFrame()



def load_records():

    if os.path.exists(RECORD_FILE):

        return pd.read_csv(RECORD_FILE)

    return pd.DataFrame()



# -----------------------------
# Dashboard
# -----------------------------

st.title("🚜 Farmer Dashboard")


st.write(
    f"Welcome {st.session_state.user} 🌱"
)



# FARM DATA

farms = load_farms()



if not farms.empty:


    my_farm = farms[
        farms["farmer_id"]
        ==
        st.session_state.user_id
    ]


    if not my_farm.empty:


        st.subheader(
            "🌾 My Farm"
        )


        st.dataframe(
            my_farm
        )


    else:

        st.info(
            "Create your farm profile first."
        )



else:

    st.info(
        "No farm data available."
    )



# RECORD DATA

st.divider()


st.subheader(
    "📋 My Crop Records"
)



records = load_records()



if not records.empty:


    my_records = records[
        records["farmer_id"]
        ==
        st.session_state.user_id
    ]


    if not my_records.empty:

        st.dataframe(
            my_records
        )

    else:

        st.info(
            "No crop diagnoses yet."
        )


else:

    st.info(
        "No diagnosis history available."
    )



# STATISTICS

st.divider()


st.subheader(
    "📊 Farm Statistics"
)


col1, col2 = st.columns(2)



with col1:

    st.metric(
        "Total Crops Diagnosed",
        len(records)
    )



with col2:

    st.metric(
        "Farm Profile",
        "Active"
    )
