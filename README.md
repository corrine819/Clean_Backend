# Clean Backend Setup

## Installation

```bash
pip install -r requirements.txt
```

## Running the App

```bash
uvicorn main:app --reload --port 8000
```

## Endpoints

- `GET /health` → Health check
- `POST /generate_multi_day_plan` → Generates a basic multi-day workout and nutrition plan