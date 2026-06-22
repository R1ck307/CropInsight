import streamlit as st
import pandas as pd
import os


USER_FILE = "database/users.csv"


# -----------------------------
# Load Users
# -----------------------------

def load_users():

    if os.path.exists(USER_FILE):

        try:
            users = pd.read_csv(USER_FILE)

            return users

        except:
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



# -----------------------------
# Save User
# -----------------------------

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



# -----------------------------
# Page
# -----------------------------

st.title("🌱 CropInsight Farmer Account")


users = load_users()


option = st.radio(
    "Choose option",
    [
        "Login",
        "Create Account"
    ]
)



# -----------------------------
# CREATE ACCOUNT
# -----------------------------

if option == "Create Account":


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
        "Location"
    )



    if st.button("Create Account"):


        new_user = {

            "id": len(users) + 1,

            "name": name.strip(),

            "email": email.strip().lower(),

            "password": password.strip(),

            "location": location.strip()

        }


        save_user(new_user)


        st.success(
            "Account created successfully 🌱"
        )



# -----------------------------
# LOGIN
# -----------------------------

if option == "Login":


    email = st.text_input(
        "Email"
    )


    password = st.text_input(
        "Password",
        type="password"
    )



    if st.button("Login"):


        email = email.strip().lower()

        password = password.strip()



        users["email"] = (
            users["email"]
            .astype(str)
            .str.strip()
            .str.lower()
        )


        users["password"] = (
            users["password"]
            .astype(str)
            .str.strip()
        )



        result = users[
            (users["email"] == email)
            &
            (users["password"] == password)
        ]



        if not result.empty:


            user = result.iloc[0]


            st.session_state.logged_in = True

            st.session_state.user = user["name"]

            st.session_state.user_id = user["id"]



            st.success(
                f"Welcome {user['name']} 🌱"
            )


        else:


            st.error(
                "Email or password incorrect"
            )
