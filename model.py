from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import os
from dotenv import load_dotenv


load_dotenv()

## Langsmith Tracking
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")

# Load the Ollama LLaMA model
llm = Ollama(model="llama2")  # Use "llama2" or the specific model you downloaded

# Updated Prompt Template for Medical Report
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a medical AI assistant designed to generate professional and structured medical reports. Include possible diagnoses, recommended tests, patient education, and risk assessment based on the provided inputs. Ensure the report is formatted with clear headings and content, as specified below."),
        ("user", """Generate a detailed medical report based on the following inputs:

- Age: {age}
- Gender: {gender}
- Primary Symptoms: {primary_symptoms}
- Vital Signs: {vital_signs}
- Medical History: {medical_history}
- Medications: {medications}
- Allergies: {allergies}
- Report Type: {report_type}

**Format Instructions:**
1. Use '# Heading 1' for main sections to make them larger and bold.
2. Each section heading should be on a separate line, followed by a blank line.
3. The content for each section should start on the next line after the heading.
4. Ensure the report is professional, concise, and free of placeholders.

**Sections:**

# Chief Complaint
[Content for Chief Complaint]

# History of Present Illness
[Content for History of Present Illness]

# Relevant Medical History
[Content for Relevant Medical History]

# Medications
[Content for Medications]

# Allergies
[Content for Allergies]

# Vital Signs
[Content for Vital Signs]

# Assessment
[Content for Assessment]

# Possible Diagnoses
[Content for Possible Diagnoses]

# Recommended Tests
[Content for Recommended Tests]

# Patient Education
[Content for Patient Education]

# Risk Assessment
[Content for Risk Assessment]

# Plan
[Content for Plan]

# Follow-Up
[Content for Follow-Up]

**Important Notes:**
- Do not combine headings and content on the same line.
- Each heading must be followed by a blank line, and the content must start on the next line.
- Ensure the report adheres to the above format strictly.
""")
    ]
)

# Create the Chain
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

# Function to Generate Medical Report
def generate_medical_report(age, gender, primary_symptoms, vital_signs, medical_history, medications, allergies, report_type):
    try:
        # Generate the medical report using the chain
        report = chain.invoke({
            "age": age,
            "gender": gender,
            "primary_symptoms": primary_symptoms,
            "vital_signs": vital_signs,
            "medical_history": medical_history,
            "medications": medications,
            "allergies": allergies,
            "report_type": report_type
        })
        return report
    except Exception as e:
        return f"An error occurred while generating the report: {e}"