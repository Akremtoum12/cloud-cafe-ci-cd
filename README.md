![CI Pipeline](https://github.com/AkremToum12/cloud-cafe-ci-cd/actions/workflows/ci.yml/badge.svg)

# ☕ Cloud Café v2 — Dockerised Flask API with PostgreSQL & CI/CD

Cloud Café v2 is a fully containerised learning project that demonstrates key DevOps concepts, including Docker, Docker Compose, Python microservices, service-to-service networking, environment variable management, and continuous integration with GitHub Actions.

---

## 🔧 Features

- **Flask API** with two routes:
  - `/` – basic health message  
  - `/db-check` – tests API ↔ PostgreSQL connection  
- **PostgreSQL** running as a separate container  
- **Docker Compose** orchestration (web + db)  
- Secure **.env** configuration (ignored by Git)  
- Automated **GitHub Actions CI pipeline**:
  - Python setup  
  - Dependency installation  
  - Syntax check  
  - Linting (Ruff)  
  - Docker build test  

---

## 🐳 Running the Application

### 1️⃣ Create a `.env` file  
Use `.env.example` as a template:

```
DB_HOST=db
DB_PORT=5432
DB_NAME=cafe_db
DB_USER=postgres
DB_PASSWORD=postgres
```

This file stays local and must **not** be committed to Git.

---

### 2️⃣ Start the containers

To build and start the Docker environment:

```bash
docker compose up --build
```

Docker will:

- Build the Flask image  
- Start the Flask container  
- Start the PostgreSQL container  
- Connect them using an internal Docker network  

---

### 3️⃣ Test the endpoints

- http://localhost:5000  
- http://localhost:5000/db-check  

You should see JSON responses confirming both services are running.

---

## 🔄 Continuous Integration (GitHub Actions)

The CI pipeline runs automatically on every push to `main`.

It includes:

- Checking out the repo  
- Installing Python  
- Installing dependencies  
- Linting with Ruff  
- Syntax checking  
- Docker build test  

---

## 🛠️ Tools & Technologies

- Docker  
- Docker Compose  
- Flask (Python)  
- PostgreSQL  
- GitHub Actions  
- Environment variables (`.env`)  

---

## 📌 Future Improvements

- Add automated tests (pytest)  
- Add database migrations  
- Add health-check scripts  
- Deploy to AWS, Render, or Railway  
- Add monitoring and logging support  

