# Cohort Backend

This repository contains the backend code for the Cohort project, a platform designed to allow patients to own and share their medical files (e.g., sleep scans, x-rays, MRIs) directly with clinics. The backend is built with FastAPI, SQLAlchemy, and PostgreSQL, and it leverages the Solana blockchain for immutable logs and secure file sharing.

## Features

- User authentication and management
- File upload and management
- Commenting system on files
- Secure and encrypted data storage
- Integration with Solana blockchain for immutable logging

## Tech Stack

- **Backend Framework:** FastAPI
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Blockchain:** Solana
- **Authentication:** OAuth2, JWT
- **Encryption:** AES-256 for data at rest, TLS for data in transit
- **Logging and Monitoring:** ELK Stack
- **Containerization:** Docker
- **Web Server:** Nginx

## Getting Started

### Prerequisites

- Python 3.11
- PostgreSQL
- Docker (optional, for containerization)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/cohort-backend.git
    cd cohort-backend
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up your `.env` file with the following variables:

    ```env
    DATABASE_URL=postgresql://<username>:<password>@localhost/cohort_db
    SECRET_KEY=<your-secret-key>
    ```

5. Initialize the database:

    ```bash
    alembic upgrade head
    ```

### Running the Application

1. Start the FastAPI server:

    ```bash
    uvicorn app.main:app --reload
    ```

2. The application will be available at `http://127.0.0.1:8000`.

### Running Tests

To run the tests, use the following command:

```bash
pytest
```

### API Documentation 

Once the server is running, you can access the API documentation at http://127.0.0.1:8000/docs.

### Contributing

	1.	Fork the repository
	2.	Create your feature branch (git checkout -b feature/new-feature)
	3.	Commit your changes (git commit -am 'Add some feature')
	4.	Push to the branch (git push origin feature/new-feature)
	5.	Create a new Pull Request

### License

This project is licensed under the MIT License. See the LICENSE file for details.

### Contact

For any questions or support, please open an issue in the repository or contact the project maintainer.