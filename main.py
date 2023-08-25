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

st.title("Batch Charlson Comorbidity Index")

st.markdown("""
#### **Description**:
The CCI Calculator is a Streamlit app designed to compute the Charlson Comorbidity Index for multiple patients based on their medical conditions and age. This index is often used to predict the one-year mortality for patients with multiple comorbidities.

#### **Usage**:

1. **Prepare Your Data**: 
   - Create a CSV file with the following columns:
     - `patient_id`: A unique identifier for each patient.
     - `age`: Age of the patient.
     - Other columns should correspond to the various comorbidities.
   - Each condition column should contain either a `1` (indicating the presence of the condition) or `0` (indicating the absence of the condition) for each patient.

2. **Uploading Data**:
   - Below, you'll see a file uploader widget. Click on "Browse files" and select the CSV file you prepared in the previous step.

3. **Viewing Results**:
   - Once the file is uploaded, the app will automatically compute the CCI for each patient. The results will be displayed in a table format below the file uploader, showing the `patient_id`, `age`, and the calculated `CCI`.

4. **Error Handling**:
   - If the uploaded file doesn't match the expected format, an error message will be displayed. Ensure you've named the columns correctly and included all the required columns.

#### **Note on Conditions**:
The CCI gives different weightings to different conditions based on their potential to influence mortality. Additionally, starting from the age of 40, a point is added for every decade.

#### **Data Security**:
Ensure that the data you upload is de-identified to protect patient privacy. The app doesn't store any of the data you upload.
""")

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
