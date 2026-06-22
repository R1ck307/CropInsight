import streamlit as st
import pandas as pd
import os


FARM_FILE = "database/farms.csv"


# -----------------------------
# Check Login
# -----------------------------

if "logged_in" not in st.session_state or not st.session_state.logged_in:

    st.warning(
        "Please login first to create your farm profile 🌱"
    )

    st.stop()



# -----------------------------
# Load Farms
# -----------------------------

def load_farms():

    if os.path.exists(FARM_FILE):

        try:

            return pd.read_csv(FARM_FILE)

        except:

            pass


    return pd.DataFrame(
        columns=[
            "farmer_id",
            "farm_name",
            "location",
            "crops",
            "size"
        ]
    )



# -----------------------------
# Save Farm
# -----------------------------

def save_farm(farm):

    farms = load_farms()


    farms = pd.concat(
        [
            farms,
            pd.DataFrame([farm])
        ],
        ignore_index=True
    )


    farms.to_csv(
        FARM_FILE,
        index=False
    )



# -----------------------------
# Page
# -----------------------------

st.title("🚜 My Farm Profile")


st.write(
    f"Welcome {st.session_state.user} 🌱"
)



farm_name = st.text_input(
    "Farm Name"
)


location = st.text_input(
    "Farm Location"
)


crops = st.text_input(
    "Crops you grow"
)


size = st.number_input(
    "Farm Size (hectares)",
    min_value=0.0
)



if st.button("Save Farm Profile"):


    new_farm = {


        "farmer_id":
        st.session_state.user_id,


        "farm_name":
        farm_name,


        "location":
        location,


        "crops":
        crops,


        "size":
        size

    }


    save_farm(new_farm)


    st.success(
        "Farm profile saved successfully 🌱"
    )



# -----------------------------
# Show Farmer Farm
# -----------------------------

st.divider()

st.subheader(
    "Your Farm Information"
)


farms = load_farms()


my_farms = farms[
    farms["farmer_id"]
    ==
    st.session_state.user_id
]



if not my_farms.empty:


    st.dataframe(
        my_farms
    )


else:


    st.info(
        "No farm profile created yet."
)
