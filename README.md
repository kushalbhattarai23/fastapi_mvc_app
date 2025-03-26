
# FastAPI Application with Docker

This is a simple FastAPI application with Docker support. It includes endpoints for managing tasks and their statuses.

## Features

- CRUD operations for tasks (`GET`, `POST`, `PUT`, `DELETE`).
- Task status management (`POST`, `GET`, `PUT`, `DELETE`).
- Dockerized application for easy deployment.

## Requirements

- Docker
- Python 3.9+
- Docker Compose (if needed for multi-container setups)

## Setup Instructions

### 1. Clone the repository
Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository
```

### 2. Build Docker Image

To build the Docker image, run:

```bash
docker build -t fastapi-app .
```

### 3. Run the Docker Container

Once the image is built, you can run the container:

```bash
docker run -d -p 8000:8000 fastapi-app
```

The application will be accessible at `http://localhost:8000`.

### 4. Access the FastAPI Documentation

Once the container is running, you can access the interactive API documentation provided by FastAPI at:

- [Swagger UI](http://localhost:8000/docs)
- [ReDoc UI](http://localhost:8000/redoc)

### 5. Docker Compose (Optional)

If you want to use Docker Compose, you can create a `docker-compose.yml` file with the following content:

```yaml
version: "3.8"
services:
  app:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - .:/app
    environment:
      - PYTHONUNBUFFERED=1
```

Then, use the following command to start the application with Docker Compose:

```bash
docker-compose up --build
```

### 6. Testing the API

You can test the API by sending requests to the endpoints:

- **GET /tasks**: Retrieve all tasks.
- **POST /tasks**: Create a new task.
- **GET /tasks/{task_id}**: Retrieve a specific task by ID.
- **PUT /tasks/{task_id}**: Update a task by ID.
- **DELETE /tasks/{task_id}**: Delete a task by ID.
- **POST /task_status**: Create a new task status.
- **GET /task_status/{status_id}**: Retrieve task status by ID.
- **PUT /task_status/{status_id}**: Update task status by ID.
- **DELETE /task_status/{status_id}**: Delete task status by ID.

### 7. Dependencies

- **FastAPI**: Python web framework.
- **SQLAlchemy**: ORM for database interactions.
- **Pydantic**: Data validation and settings management.
- **Uvicorn**: ASGI server to run the application.

To install the dependencies locally, run:

```bash
pip install -r requirements.txt
```

### 8. Database

This application uses an in-memory SQLite database for simplicity. You can change the database configuration in the application if you need a more persistent database.

## Troubleshooting

- **Port already in use**: If the port `8000` is already in use, change the port mapping in the Docker command to another available port.
- **Docker not found**: Ensure Docker is properly installed and running on your machine.

## License

