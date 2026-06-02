def diagnose(crop, symptoms):

    rules = {

        "Maize": {
            "yellow_leaves": "Nitrogen Deficiency",
            "brown_edges": "Potassium Deficiency",
            "purple_leaves": "Phosphorus Deficiency",
            "orange_spots": "Rust",
            "brown_lesions": "Leaf Blight"
        },

        "Tomato": {
            "brown_spots": "Early Blight",
            "wilting": "Late Blight",
            "small_dark_spots": "Septoria Leaf Spot",
            "sudden_wilt": "Bacterial Wilt"
        },

        "Cucumber": {
            "white_powder": "Powdery Mildew",
            "yellow_patches": "Downy Mildew"
        },

        "Beans": {
            "sunken_lesions": "Anthracnose",
            "brown_circles": "Leaf Spot",
            "reddish_spots": "Rust"
        },

        "Cabbage": {
            "v_shape": "Black Rot",
            "swollen_roots": "Clubroot",
            "dark_stems": "Blackleg"
        },

        "Spinach": {
            "yellowing": "Nitrogen Deficiency",
            "white_tunnels": "Leaf Miner",
            "yellow_under": "Downy Mildew"
        }

    }

    if crop in rules:

        for symptom in symptoms:

            if symptom in rules[crop]:

                return rules[crop][symptom]

    return None
