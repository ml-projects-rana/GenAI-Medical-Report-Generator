import streamlit as st
from model import generate_medical_report

# Custom CSS to center-align the title and header
st.markdown(
    """
    <style>
    /* Center-align the title */
    h1 {
        text-align: center;
    }

    /* Center-align the header */
    h2 {
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Streamlit App Title
st.title("Medical Report Generator")

# Input Fields for Medical Data
st.header("Patient Information")

# Use placeholders and increase the size of input fields
age = st.text_input("Age", placeholder="Enter age (e.g. 55)")
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
primary_symptoms = st.text_area(
    "Primary Symptoms",
    placeholder="Enter primary symptoms (e.g. Severe chest pain radiating to left arm with shortness of breath)",
    height=100,  # Increase height for text area
)
vital_signs = st.text_input(
    "Vital Signs",
    placeholder="Enter vital signs (e.g. BP: 140/90, Pulse: 88, Temp: 99.2°F, SpO2: 96%)",
)
medical_history = st.text_area(
    "Medical History",
    placeholder="Enter medical history (e.g. Type 2 diabetes, hypertension 5 years ago)",
    height=100,  # Increase height for text area
)
medications = st.text_input(
    "Medications",
    placeholder="Enter medications (e.g. Metformin 500 mg twice daily, Lisinopril 10 mg daily)",
)
allergies = st.text_input(
    "Allergies",
    placeholder="Enter allergies (e.g. Penicillin, Aspirin)",
)
report_type = st.selectbox(
    "Report Type",
    ["Initial Consultation", "Follow-Up", "Emergency Visit", "Routine Checkup"],
)

# Generate Report Button
if st.button("Generate Medical Report"):
    # Validate mandatory inputs
    mandatory_fields = {
        "Age": age,
        "Gender": gender,
        "Primary Symptoms": primary_symptoms,
        "Vital Signs": vital_signs,
        "Medical History": medical_history,
        "Report Type": report_type,
    }
    missing_fields = [field for field, value in mandatory_fields.items() if not value]

    if missing_fields:
        st.error(f"Please fill in the following mandatory fields: {', '.join(missing_fields)}")
    else:
        try:
            with st.spinner("Generating medical report..."):
                # Call the function from model.py
                report = generate_medical_report(
                    age=age,
                    gender=gender,
                    primary_symptoms=primary_symptoms,
                    vital_signs=vital_signs,
                    medical_history=medical_history,
                    medications=medications,
                    allergies=allergies,
                    report_type=report_type,
                )
                st.success("Medical Report Generated Successfully!")
                st.subheader("Generated Medical Report")
                st.markdown(report)  # Display the report with Markdown formatting
        except Exception as e:
            st.error(f"An error occurred: {e}")


