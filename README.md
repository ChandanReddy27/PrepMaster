# PrepMaster
PrepMaster is a full-stack interview prep platform that simulates real SWE interviews. Practice HLD, LLD, and LeetCode problems with AI-powered follow-up questions and evaluations. Built with React, FastAPI, and Postgres, deployed on Kubernetes with Claude AI via stdio.

## Local Development

### 1. Environment setup

Copy the example env file and fill in your values:

```bash
cp .env.example .env
```

### 2. Start the database

```bash
docker compose up -d
```

### 3. Start the backend

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### 4. Start the frontend

```bash
cd frontend
npm install
npm run dev
```
