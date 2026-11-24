# Insurance Premium Category Predictor

A machine-learning application that predicts an insurance premium category from user-provided information. The project uses a Streamlit interface, a FastAPI prediction service, and a scikit-learn model.

## Tech Stack

- **Python 3.11**
- **Frontend:** Streamlit
- **Backend:** FastAPI and Uvicorn
- **Machine Learning:** scikit-learn
- **Data handling:** NumPy and pandas
- **Validation:** Pydantic
- **Containerization:** Docker

## Project Architecture

The application is divided into a Streamlit frontend and a FastAPI backend.

1. The user enters personal and lifestyle information in the Streamlit interface.
2. The frontend sends the input to the FastAPI `/predict` endpoint.
3. The backend validates the request using the `UserInput` schema.
4. The backend prepares the model features and calls the prediction function.
5. The API returns the predicted insurance premium category.

## Repository Structure

Make sure the repository contains the model and schema modules imported by `app.py`. A suggested structure is:

```text
insurance-premium-predictor/
├── app.py
├── frontend.py
├── requirements.txt
├── frontend_requirements.txt
├── Dockerfile
├── .gitignore
├── README.md
├── model/
│   ├── __init__.py
│   └── predict.py
└── schema/
    ├── __init__.py
    ├── user_input.py
    └── prediction_response.py
```

Include any trained model or preprocessing files required by `model/predict.py`. Do not commit virtual environments, secrets, or temporary files.

## Features

- Streamlit-based user interface.
- FastAPI prediction endpoint.
- Input validation through Pydantic schemas.
- Health-check endpoint that reports API status, model version, and whether the model is loaded.
- Dockerfile for running the backend in a container.

## Requirements

Use Python 3.11. The backend dependencies are listed in `requirements.txt`; frontend dependencies are listed separately in `frontend_requirements.txt`.

## Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/insurance-premium-predictor.git
cd insurance-premium-predictor
```

### 2. Create and activate a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

macOS/Linux:

```bash
source venv/bin/activate
```

### 3. Install dependencies

Install backend dependencies:

```bash
pip install -r requirements.txt
```

Install frontend dependencies:

```bash
pip install -r frontend_requirements.txt
```

### 4. Start the FastAPI backend

```bash
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at:

- API root: `http://localhost:8000/`
- Health check: `http://localhost:8000/health`
- Interactive API documentation: `http://localhost:8000/docs`

### 5. Start the Streamlit frontend

In a second terminal, activate the same virtual environment and run:

```bash
streamlit run frontend.py
```

Configure the frontend API URL to point to the running backend. For local development, use:

```text
http://localhost:8000/predict
```

If the backend is deployed remotely, set the API URL to that deployment's `/predict` endpoint rather than relying on a hardcoded address.

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Basic API welcome message |
| GET | `/health` | API and model health information |
| POST | `/predict` | Predict an insurance premium category |

The `/predict` endpoint accepts the `UserInput` schema defined in `schema/user_input.py`. The backend currently prepares these model features: `bmi`, `age_group`, `lifestyle_risk`, `city_tier`, `income_lpa`, and `occupation`.

Refer to the schema and the interactive API documentation at `/docs` for the exact request fields and validation rules.

## Run with Docker

Build the backend image from the repository root:

```bash
docker build -t insurance-premium-api .
```

Run the container:

```bash
docker run -p 8000:8000 insurance-premium-api
```

Then open `http://localhost:8000/docs`.

The Dockerfile starts the FastAPI backend. Run the Streamlit frontend separately unless you configure a separate frontend container.

## Important Integration Check

Before using the application, make sure the frontend and backend agree on the request and response formats.

- The frontend currently sends `age`, `weight`, `height`, `income_lpa`, `smoker`, `city`, and `occupation`.
- The backend's `UserInput` schema and feature-preparation code must correctly transform those fields into the model features.
- The backend currently returns a JSON object containing `predicted_category` directly.
- The frontend currently checks for a top-level `response` object and reads `confidence` and `class_probabilities`.

Update one side so both use the same response contract. Do not display confidence or class probabilities unless the prediction code actually returns them.

## Model and Data

The prediction implementation is imported from `model/predict.py`. Add the required trained model, preprocessing artifacts, and any other files needed by that module to the repository, subject to file-size and licensing constraints.

Do not upload private, licensed, or sensitive datasets. If a model artifact is too large for normal Git storage, consider Git LFS or an appropriate model hosting service.

## Future Improvements

- Add automated tests for input validation and prediction responses.
- Move the backend URL to environment-based configuration.
- Add request timeouts and clearer API error handling in the frontend.
- Add logging and structured error responses.
- Document model evaluation metrics and dataset provenance.

## Author

**YOUR NAME**

Update this section with your name and relevant profile links.
