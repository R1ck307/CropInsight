import streamlit as st
import pandas as pd
import os


USER_FILE = "database/users.csv"


def load_users():

    try:

        if os.path.exists(USER_FILE):

            users = pd.read_csv(USER_FILE)

            return users


    except Exception:

        pass


    return pd.DataFrame(
        columns=[
            "id",
            "name",
            "email",
            "password",
            "location"
        ]
    )


def save_user(user):

    users = load_users()

    users = pd.concat(
        [
            users,
            pd.DataFrame([user])
        ],
        ignore_index=True
    )

    users.to_csv(
        USER_FILE,
        index=False
    )



st.title("🌱 CropInsight Farmer Account")


users = load_users()


choice = st.radio(
    "Select option",
    [
        "Login",
        "Create Account"
    ]
)



# -----------------------------
# CREATE ACCOUNT
# -----------------------------

if choice == "Create Account":


    name = st.text_input(
        "Full Name"
    )

    email = st.text_input(
        "Email"
    )

    password = st.text_input(
        "Password",
        type="password"
    )

    location = st.text_input(
        "Farm Location"
    )


    if st.button("Create Account"):


        new_user = {

            "id": len(users)+1,

            "name": name,

            "email": email,

            "password": password,

            "location": location

        }


        save_user(new_user)


        st.success(
            "Account created successfully 🌱"
        )



# -----------------------------
# LOGIN
# -----------------------------

if choice == "Login":


    email = st.text_input(
        "Email"
    )


    password = st.text_input(
        "Password",
        type="password"
    )



    if st.button("Login"):


        result = users[
            (users["email"] == email)
            &
            (users["password"] == password)
        ]



        if len(result) > 0:


            user = result.iloc[0]


            st.session_state.logged_in = True


            st.session_state.user = user["name"]


            st.session_state.user_id = user["id"]



            st.success(
                f"Welcome {user['name']} 🌱"
            )



        else:


            st.error(
                "Invalid email or password"
)
