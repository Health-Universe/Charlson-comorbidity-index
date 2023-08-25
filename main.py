import streamlit as st
import pandas as pd

# Define the Charlson Comorbidity conditions and their respective weights
COMORBIDITIES = {
    "Myocardial infarction": 1,
    "Congestive heart failure": 1,
    "Peripheral vascular disease": 1,
    "Cerebrovascular accident or transient ischemic attack": 1,
    "Dementia": 1,
    "Chronic obstructive pulmonary disease": 1,
    "Connective tissue disease": 1,
    "Peptic ulcer disease": 1,
    "Mild liver disease": 1,
    "Uncomplicated diabetes": 1,
    "Hemiplegia": 2,
    "Moderate to severe chronic kidney disease": 2,
    "Diabetes with end-organ damage": 2,
    "Localized solid tumor": 2,
    "Leukemia": 2,
    "Lymphoma": 2,
    "Moderate to severe liver disease": 3,
    "Metastatic solid tumor": 6,
    "AIDS": 6
}

def calculate_cci_for_patient(row):
    """Calculate CCI for a single row from the dataframe."""
    score = sum(row[condition] * COMORBIDITIES[condition] for condition in COMORBIDITIES.keys())

    if row["age"] >= 40:
        score += (row["age"] - 30) // 10
        if score > 4:
            score -= (score - 4)

    return score

st.title("Batch Charlson Comorbidity Index Calculator")

uploaded_file = st.file_uploader("Upload a CSV file with patient data:", type=["csv"])

if uploaded_file:
    data = pd.read_csv(uploaded_file)
    
    # Check if the required columns are in the uploaded file
    required_columns = set(['patient_id', 'age'] + list(COMORBIDITIES.keys()))
    if not required_columns.issubset(data.columns):
        st.error("Some required columns are missing in the uploaded file. Please verify the file format.")
    else:
        data['CCI'] = data.apply(calculate_cci_for_patient, axis=1)
        st.write(data[['patient_id', 'age', 'CCI']])
