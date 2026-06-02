def diagnose(crop, symptoms):

    if crop == "Maize" and "yellow_leaves" in symptoms:
        return "Nitrogen Deficiency"

    if crop == "Tomato" and "brown_spots" in symptoms:
        return "Early Blight"

    return None
