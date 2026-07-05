import pandas as pd
import os


DISEASE_FILE = "data/diseases.csv"


# -----------------------------
# Load Disease Database
# -----------------------------

def load_diseases():

    if os.path.exists(DISEASE_FILE):

        try:

            df = pd.read_csv(DISEASE_FILE)

            # Convert all column names to lowercase
            df.columns = df.columns.str.lower()

            return df

        except Exception:

            return pd.DataFrame()

    return pd.DataFrame()



# -----------------------------
# Diagnosis Engine
# -----------------------------

def diagnose_crop(crop, symptoms):

    diseases = load_diseases()

    if diseases.empty:

        return None


    crop_data = diseases[
        diseases["crop"].str.lower()
        ==
        crop.lower()
    ]


    matches = []


    for _, row in crop_data.iterrows():

        disease_symptoms = str(
            row["symptoms"]
        ).lower()


        score = 0


        symptom_list = symptoms.lower().split(",")


        for symptom in symptom_list:

            symptom = symptom.strip()

            if symptom in disease_symptoms:

                score += 1


        if score > 0:

            matches.append(

                {
                    "disease":
                    row["disease"],

                    "confidence":
                    min(score * 25, 100),

                    "severity":
                    row["severity"],

                    "cause":
                    row["cause"],

                    "treatment":
                    row["treatment"],

                    "prevention":
                    row["prevention"],

                    "organic_solution":
                    row["organic_solution"],

                    "chemical_solution":
                    row["chemical_solution"],

                    "risk_conditions":
                    row["risk_conditions"]
                }

            )


    if matches:

        matches = sorted(
            matches,
            key=lambda x: x["confidence"],
            reverse=True
        )

        return matches[0]


    return {

        "disease":
        "Unknown",

        "confidence":
        0,

        "severity":
        "Unknown",

        "cause":
        "Unknown",

        "treatment":
        "No recommendation available",

        "prevention":
        "No prevention advice available",

        "organic_solution":
        "N/A",

        "chemical_solution":
        "N/A",

        "risk_conditions":
        "N/A"
    }
# -----------------------------
# Compatibility Function
# -----------------------------

def diagnose(crop, symptoms):
    return diagnose_crop(crop, symptoms)
