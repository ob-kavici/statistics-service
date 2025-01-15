# Stats Service

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

A backend microservice developed with **FastAPI** that collects and processes game statistics.

---

## Features
- Consumes game state events via RabbitMQ.
- Computes and stores aggregated game statistics.
- Provides APIs for querying game statistics.
- Integrated with Prometheus for metrics monitoring.

---

## Table of Contents
- [Features](#features)
- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
    - [Running Locally](#running-locally)
- [Contributing](#contributing)
- [License](#license)

---

## Getting Started

Follow these instructions to set up and run the `stats-service` microservice locally.

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- RabbitMQ instance (local or hosted)

### Installation

1. **Clone the repository**:
     ```bash
     git clone https://github.com/ob-kavici/stats-service.git
     cd stats-service
     ```

2. **(Optional) Create and activate a virtual environment**:
     ```bash
     python -m venv venv
     source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
     ```

3. **Install dependencies**:
     ```bash
     pip install -r requirements.txt
     ```

### Running Locally

1. **Navigate to the /app directory**:
     ```bash
     cd app
     ```

2. **Copy and rename the .env.template file to .env**:
     ```bash
     cp .env.template .env
     ```

3. **Edit the .env file to include your environment variables (e.g., RabbitMQ connection details, Supabase credentials, etc.)**.

4. **Start the application using Uvicorn**:
     ```bash
     uvicorn main:app --reload --port 8002
     ```

The service will be accessible at [http://127.0.0.1:8002](http://127.0.0.1:8002).

---

To enable stats collection and logging, also run a local instance of RabbitMQ broker:
```bash
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:4.0-management
```

---

## Contributing

Contributions are welcome! To contribute:

1. **Fork the repository**.
2. **Create a feature branch**:
     ```bash
     git checkout -b feature/your-feature-name
     ```
3. **Commit your changes**:
     ```bash
     git commit -m "Add your commit message"
     ```
4. **Push the branch**:
     ```bash
     git push origin feature/your-feature-name
     ```
5. **Open a pull request**.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

Feel free to reach out if you encounter any issues or have suggestions for improvement!
