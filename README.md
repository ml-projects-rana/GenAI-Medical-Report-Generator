# Medical Report Generator

The **Medical Report Generator** is a Streamlit-based web application that leverages the power of LangChain and Ollama's **Llama3.2:1b** model to generate professional and structured medical reports. This tool is designed to assist healthcare professionals in quickly creating detailed medical reports based on patient inputs such as age, gender, symptoms, vital signs, medical history, medications, allergies, and report type.

## Web Application Demo
https://github.com/user-attachments/assets/acc1cdeb-5bd3-43ba-942c-a7bc1e974bf6

---

## Features

- **Interactive Web Interface**: Built using Streamlit, the application provides an intuitive and user-friendly interface for entering patient data.
- **AI-Powered Report Generation**: Utilizes the **Llama3.2:1b** model to generate structured medical reports with sections like Chief Complaint, History of Present Illness, Relevant Medical History, Medications, Allergies, Vital Signs, Assessment, Possible Diagnoses, Recommended Tests, Patient Education, Risk Assessment, Plan, and Follow-Up.
- **Customizable Inputs**: Users can input patient-specific details, and the application dynamically generates a tailored medical report.
- **Markdown Formatting**: The generated report is displayed in a clean and professional Markdown format for easy readability.
- **Error Handling**: The application includes validation for mandatory fields and provides meaningful error messages if any required fields are missing or if an error occurs during report generation.
- **LangChain Monitoring**: Integrated with LangChain for tracking and monitoring the AI model's performance and usage.

---

## Prerequisites

Before running the application, ensure you have the following installed:

1. **Python 3.10**: The application is built using Python 3.10.
2. **Conda**: For managing the virtual environment.
3. **Git**: For cloning the repository.
4. **Ollama**: For running the **Llama3.2:1b** model locally.

---

## Installation

### Step 1: Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/ml-projects-rana/GenAI-Medical-Report-Generator.git
cd GenAI-Medical-Report-Generator
```

### Step 2: Create and Activate the Conda Environment

Create a Conda environment with Python 3.10:

```bash
conda create -p ./llm_report_generator python=3.10 -y
conda activate ./llm_report_generator
```

### Step 3: Install Dependencies

Install the required Python packages using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

---

## Configuration

### Step 1: Set Up Environment Variables

1. Create a `.env` file in the root directory of the project.
2. Add the following environment variables to the `.env` file:

```env
LANGCHAIN_API_KEY=your_langchain_api_key
LANGCHAIN_PROJECT=your_langchain_project_name
```

Replace `your_langchain_api_key` and `your_langchain_project_name` with your actual LangChain API key and project name.

### Step 2: Download the Ollama Llama3.2:1b Model

Ensure you have downloaded the Ollama **Llama3.2:1b** model. You can download it using the following command:

```bash
ollama pull llama3.2:1b
```

---

## Running the Application

To start the Streamlit application, run the following command:

```bash
streamlit run app.py
```

Once the application is running, open your web browser and navigate to the provided local URL (usually `http://localhost:8501`).

---

## Usage

1. **Enter Patient Information**: Fill in the required fields such as Age, Gender, Primary Symptoms, Vital Signs, Medical History, Medications, Allergies, and Report Type.
2. **Generate Report**: Click the "Generate Medical Report" button to create a detailed medical report.
3. **View Report**: The generated report will be displayed in a structured format with clear headings and content.

---

## What I Have Done

1. **Streamlit Web Application**: Created an interactive web interface using Streamlit for entering patient data and generating medical reports.
2. **LangChain Integration**: Integrated LangChain to manage the AI model and generate structured medical reports.
3. **Ollama Llama3.2:1b Model**: Utilized the **Llama3.2:1b** model for generating high-quality, professional medical reports.
4. **Environment Management**: Set up a Conda environment for dependency management and reproducibility.
5. **Error Handling**: Implemented validation for mandatory fields and error handling for a smooth user experience. If any required fields are missing, the application displays a clear error message. Additionally, if an error occurs during report generation, the application provides a meaningful error message to the user.
6. **LangChain Monitoring**: Integrated LangChain for tracking and monitoring the AI model's performance and usage. This includes:
   - Enabling LangChain tracing using `LANGCHAIN_TRACING_V2="true"`.
   - Setting up the LangChain API key and project name for monitoring.
7. **Markdown Formatting**: Ensured the generated report is displayed in a clean and professional Markdown format.

---

## Future Enhancements

- **Support for Multiple Languages**: Add support for generating reports in multiple languages.
- **Integration with EHR Systems**: Integrate with Electronic Health Record (EHR) systems for seamless data import/export.
- **Customizable Templates**: Allow users to customize report templates based on their specific needs.
- **Export Options**: Add options to export the generated report as a PDF or Word document.

---

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push to the branch.
4. Submit a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- **Streamlit**: For providing an excellent framework for building interactive web applications.
- **LangChain**: For enabling seamless integration with AI models and monitoring.
- **Ollama**: For providing the **Llama3.2:1b** model used in this project.

---


### Error Handling Details
The application includes robust error handling to ensure a smooth user experience:
- **Mandatory Field Validation**: If any required fields (e.g., Age, Gender, Primary Symptoms, etc.) are missing, the application displays a clear error message listing the missing fields.
- **Report Generation Errors**: If an error occurs during report generation (e.g., due to model issues or network problems), the application catches the exception and displays a user-friendly error message.

### LangChain Monitoring Details
LangChain monitoring is enabled to track the AI model's performance and usage:
- **Tracing**: LangChain tracing is enabled using `LANGCHAIN_TRACING_V2="true"`.
- **API Key and Project**: The LangChain API key and project name are configured in the `.env` file for monitoring purposes.
- **Usage Insights**: LangChain provides insights into how the model is being used, including response times, success rates, and error rates.
---

## Contact

For any questions or feedback, feel free to reach out:

- **Email**: dipanshurana04@gmail.com
- **LinkedIn**: [Dipanshu Rana](https://www.linkedin.com/in/dipanshu-rana/)

---

Enjoy using the **Medical Report Generator**! 🚀

---

