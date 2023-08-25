import streamlit as st

# Define the updated Charlson Comorbidity conditions and their respective weights
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

def calculate_cci(selected_conditions, age):
    """Calculate the CCI score based on selected comorbidities and age."""
    score = 0

    # Handle mutual exclusivity of liver disease
    if "Mild liver disease" in selected_conditions and "Moderate to severe liver disease" in selected_conditions:
        st.error("You cannot select both 'Mild liver disease' and 'Moderate or severe liver disease'.")
        return

    for condition in selected_conditions:
        score += COMORBIDITIES[condition]
    
    # Add age factor starting from age 40
    if age >= 40:
        score += (age - 30) // 10
        if score > 4:  # Ensure maximum of 4 points for age
            score -= (score - 4)
        
    return score

st.title("Charlson Comorbidity Index Calculator")

# Input age
age = st.number_input("Enter the patient's age:", min_value=0, max_value=120, value=40, step=1)

# Allow users to select multiple comorbidities
selected_conditions = st.multiselect(
    "Select the comorbidities:", list(COMORBIDITIES.keys())
)

# Calculate CCI when user clicks the button
if st.button("Calculate CCI"):
    cci_score = calculate_cci(selected_conditions, age)
    if cci_score is not None:  # Ensure score is not None due to liver disease error
        st.write(f"Charlson Comorbidity Index is: {cci_score}")
