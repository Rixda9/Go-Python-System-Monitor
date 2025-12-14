# System Metrics API
A simple system metrics API made with the use of FastAPI and psutils.

## Goals

Learn API development and system data-fetching

## Tech Stack

- Python
- FastAPI
- psutils

## Building

```bash
git clone https://github.com/Rixda9/System-Metrics-API.git
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Then head to localhost:8000/stats.

## What I Learned

Learned Pydantic for data validation 

Mastered environment isolation with venv

## Limitations

Limited visibility: The API currently only exposes three metrics (CPU, RAM, OS). It lacks critical data points for production monitoring.

Not scalable: All logic (API routing and data fetching) is within a single Python process.

## Future Goal

Adopting Microservices Architecture
