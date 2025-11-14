# FinSight – AI-Powered Personal Finance Dashboard (Backend)

FinSight is an AI-powered personal finance system that helps users understand and improve their money habits using data analytics and intelligent insights. This repository contains the backend API built with Python and FastAPI.

## 1. Overview

FinSight will allow users to:

- Register and log in securely.
- Upload or sync transaction data.
- View spending and savings summaries.
- Receive AI-generated explanations about their financial behaviour.

The backend is designed to be secure, modular, and ready for a modern React + TypeScript frontend.

## 2. Tech Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- python-dotenv

## 3. Project Structure

```text
finsight/
├─ app/
│  ├─ main.py
│  ├─ config.py
│  ├─ database.py
│  ├─ models/
│  ├─ schemas/
│  ├─ routers/
│  ├─ services/
├─ docs/
├─ tests/
├─ .env.example
├─ .gitignore
├─ README.md
├─ requirements.txt

```


 ## 4. Getting Started

``` bash 
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
uvicorn app.main:app --reload

```

Then open:

http://127.0.0.1:8000/

http://127.0.0.1:8000/docs

In your terminal (still in `C:\Users\kylli\finsight`, venv active):

```powershell
uvicorn app.main:app --reload
```


