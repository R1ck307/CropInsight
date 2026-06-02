def diagnose(crop, symptoms):

    if crop == "Maize":
        if "yellow_leaves" in symptoms:
            return "Nitrogen Deficiency"
        elif "brown_edges" in symptoms:
            return "Potassium Deficiency"
        elif "purple_leaves" in symptoms:
            return "Phosphorus Deficiency"
        elif "orange_spots" in symptoms:
            return "Rust"
        elif "brown_lesions" in symptoms:
            return "Leaf Blight"

    elif crop == "Tomato":
        if "brown_spots" in symptoms:
            return "Early Blight"
        elif "wilting" in symptoms:
            return "Late Blight"
        elif "small_dark_spots" in symptoms:
            return "Septoria Leaf Spot"
        elif "sudden_wilt" in symptoms:
            return "Bacterial Wilt"

    elif crop == "Cucumber":
        if "white_powder" in symptoms:
            return "Powdery Mildew"
        elif "yellow_patches" in symptoms:
            return "Downy Mildew"

    elif crop == "Beans":
        if "sunken_lesions" in symptoms:
            return "Anthracnose"
        elif "brown_circles" in symptoms:
            return "Leaf Spot"
        elif "reddish_spots" in symptoms:
            return "Rust"

    elif crop == "Cabbage":
        if "v_shape" in symptoms:
            return "Black Rot"
        elif "swollen_roots" in symptoms:
            return "Clubroot"
        elif "dark_stems" in symptoms:
            return "Blackleg"

    elif crop == "Spinach":
        if "yellowing" in symptoms:
            return "Nitrogen Deficiency"
        elif "white_tunnels" in symptoms:
            return "Leaf Miner"
        elif "yellow_under" in symptoms:
            return "Downy Mildew"

    return None
