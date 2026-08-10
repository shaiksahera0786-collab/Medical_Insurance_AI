# src/utils.py

def get_bmi_category(bmi):
    """
    Returns BMI category based on BMI value.
    """

    if bmi < 18.5:
        return "Underweight"

    elif bmi < 25:
        return "Normal Weight"

    elif bmi < 30:
        return "Overweight"

    else:
        return "Obese"


def get_risk_level(charges):
    """
    Returns insurance risk level based on predicted charges.
    """

    if charges < 10000:
        return "🟢 Low Risk"

    elif charges < 30000:
        return "🟡 Medium Risk"

    else:
        return "🔴 High Risk"


def get_health_recommendation(bmi, smoker):
    """
    Returns health recommendation based on BMI and smoking status.
    """

    recommendations = []

    # BMI Recommendation
    if bmi < 18.5:
        recommendations.append(
            "• Maintain a balanced diet to reach a healthy weight."
        )

    elif bmi < 25:
        recommendations.append(
            "• Great! Maintain your healthy lifestyle."
        )

    elif bmi < 30:
        recommendations.append(
            "• Regular exercise and a healthy diet are recommended."
        )

    else:
        recommendations.append(
            "• Consult a healthcare professional for weight management."
        )

    # Smoking Recommendation
    if smoker == 1:
        recommendations.append(
            "• Quitting smoking can improve your health and reduce insurance costs."
        )
    else:
        recommendations.append(
            "• Continue avoiding smoking to maintain good health."
        )

    return recommendations