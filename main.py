import streamlit as st

# Define the Charlson Comorbidity conditions and their respective weights
COMORBIDITIES = {
    "Myocardial infarct": 1,
    "Congestive heart failure": 1,
    "Peripheral vascular disease": 1,
    "Cerebrovascular disease": 1,
    "Dementia": 1,
    "Chronic pulmonary disease": 1,
    "Connective tissue disease": 1,
    "Ulcer disease": 1,
    "Liver disease (mild)": 1,
    "Diabetes": 1,
    "Hemiplegia": 2,
    "Renal disease": 2,
    "Diabetes with end organ damage": 2,
    "Tumor without metastasis": 2,
    "Leukemia": 2,
    "Lymphoma": 2,
    "Liver disease (moderate to severe)": 3,
    "Metastatic solid tumor": 6,
    "AIDS/HIV": 6,
}

def calculate_cci(selected_conditions):
    """Calculate the CCI score based on selected comorbidities."""
    score = 0
    for condition in selected_conditions:
        score += COMORBIDITIES[condition]
    return score

st.title("Charlson Comorbidity Index Calculator")

# Allow users to select multiple comorbidities
selected_conditions = st.multiselect(
    "Select the comorbidities:", list(COMORBIDITIES.keys())
)

# Calculate CCI when user clicks the button
if st.button("Calculate CCI"):
    cci_score = calculate_cci(selected_conditions)
    st.write(f"Charlson Comorbidity Index is: {cci_score}")
