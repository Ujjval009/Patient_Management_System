## Patient_Management_System


## Project Overview

This is a comprehensive **FastAPI Healthcare Applications Suite** that provides three interconnected applications for healthcare-related tasks:

1. **Insurance Premium Predictor** - Uses Machine Learning to predict insurance premium categories based on user health and demographic data
2. **Patient Management System** - A RESTful API for managing patient health records with CRUD operations
3. **Streamlit Frontend** - An interactive web interface for the Insurance Premium Predictor

### What Can This Project Do?

- **Predict Insurance Premiums**: Input user health metrics and get predicted insurance premium categories
- **Manage Patient Records**: Create, read, update, and delete patient health records
- **Calculate BMI**: Automatically calculate Body Mass Index for users and patients
- **Health Risk Assessment**: Determine lifestyle risk levels and health verdicts
- **Web Interface**: Provide an easy-to-use UI for non-technical users

---

## Project Structure

```
fastapi-project/
├── app.py              # Insurance Premium Prediction API (ML-based)
├── main.py             # Patient Management System API (CRUD operations)
├── frontend.py         # Streamlit web interface
├── patient.json        # JSON database for patient records
├── model.pkl           # Pre-trained scikit-learn ML model
├── requirements.txt    # Python dependencies
└── README.md           # This documentation
```

---

## Applications Explained

### 1. Insurance Premium Predictor (`app.py`)

**Purpose**: Predict insurance premium categories using machine learning

**How It Works**:
1. Accepts user data (age, weight, height, income, smoking status, city, occupation)
2. Calculates BMI automatically
3. Assesses lifestyle risk (high/medium/low)
4. Classifies age group and city tier
5. Uses a pre-trained ML model to predict premium category


**Key Components**:
- `UserInput` - Pydantic model for input validation
- City tier classification (Tier 1, 2, or 3)
- Lifestyle risk assessment
- Age group categorization
- ML model integration with pandas

**Endpoint**: `POST /predict`

---

### 2. Patient Management System (`main.py`)

**Purpose**: RESTful API for managing patient health records

**How It Works**:
1. Stores patient data in a JSON file (`patient.json`)
2. Provides CRUD operations via REST API
3. Automatically calculates BMI and health verdict
4. Supports sorting and filtering

**Key Components**:
- `Patient` - Pydantic model for patient data with computed BMI and verdict
- `PatientUpdate` - Model for partial updates
- `load_data()` - Reads from JSON file
- `save_data()` - Writes to JSON file

**Endpoints**:
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Home route |
| GET | `/about` | About page information |
| GET | `/view` | View all patients |
| GET | `/patient/{patient_id}` | View specific patient |
| GET | `/sort` | Sort patients by attribute |
| POST | `/create` | Create new patient |
| PUT | `/patient/{patient_id}` | Update patient |
| DELETE | `/delete/{patient_id}` | Delete patient |

---

### 3. Streamlit Frontend (`frontend.py`)

**Purpose**: Interactive web UI for the Insurance Premium Predictor


---

## Technology Stack

### Core Framework
- **FastAPI 0.135.2**: Modern, fast (high-performance) web framework for building APIs
- **Uvicorn 0.42.0**: Lightning-fast ASGI server, built on uvloop and httptools
- **Pydantic 2.12.5**: Data validation and settings management using Python type annotations

### Machine Learning
- **Scikit-learn 1.6.1**: Machine learning library for the prediction model
- **Pandas 3.0.2**: Data manipulation and analysis
- **NumPy 2.4.4**: Numerical computing
- **Joblib 1.5.3**: Model serialization

### Web Interface
- **Streamlit 1.56.0**: Interactive web UI framework
- **Requests 2.33.1**: HTTP library for API communication

---

## Prerequisites

Before running this project, ensure you have:

1. **Python 3.10 or higher**
   ```bash
   python --version
   ```

2. **pip (Python Package Manager)**
   ```bash
   pip --version
   ```

3. **Internet connection** (for installing packages)

---

## Installation Guide

### Step 1: Clone or Download the Project

```bash
# If using git
git clone <https://github.com/Ujjval009/Patient_Management_System.git>
cd fastapi

# Or download and extract the project folder
```

### Step 2: Create a Virtual Environment

Creating a virtual environment is recommended to avoid dependency conflicts.

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```
```

#### Running the Patient Management System API

```bash
uvicorn main:app --reload
```

#### Running the Streamlit Frontend

```bash
streamlit run frontend.py
```



## Future Enhancements

Potential improvements for this project:

1. **Database Integration**
   - Replace JSON with SQLite/PostgreSQL for better scalability
   - Add database migrations

2. **Authentication**
   - Add user authentication and authorization
   - Implement JWT tokens

3. **Enhanced ML Model**
   - Train custom model with more data
   - Add more features (medical history, family background)

4. **API Rate Limiting**
   - Implement request throttling
   - Add usage monitoring

5. **Testing**
   - Add unit tests with pytest
   - Add integration tests
   - Add API documentation tests

6. **Deployment**
   - Docker containerization
   - Cloud deployment (AWS, GCP, Azure)
   - CI/CD pipeline

7. **Additional Features**
   - Email notifications
   - Report generation
   - Data visualization dashboards
   - Export functionality (PDF, CSV)

8. **Frontend Improvements**
   - User accounts
   - Prediction history
   - Comparison features



## owner

- Ujjval Sharma


