# real-time-data-processing-api
Real-Time Data Processing and ASGI API

## Setup Instructions

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/real-time-data-processing-api.git
    cd real-time-data-processing-api
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python3 -m venv .virtualenvs/data-processing-api
    source .virtualenvs/data-processing-api/bin/activate
    ```

3. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application:**
    ```bash
    uvicorn src.main:app --reload
    ```

## Architecture

The application is structured as follows:

- **app**: Contains the core application logic, including data generation, data pipeline, and models.
- **routers**: Contains the API route definitions.
- **services**: Contains the service layer for data processing.
- **main.py**: The entry point of the application.

## API Endpoints

- **POST /data/insert-new-data**: Ingest and process new data based on post body.
- **POST /data/processing**: Process the existing data.
- **GET /data/latest**: Retrieve the latest data point.
- **GET /data**: Query data with optional start and end timestamps.
- **POST /start-data-load**: Trigger data generation and auto load.

## Assumptions and Limitations

- The application assumes that the data source is reliable and provides data in the expected format.
- The application is designed to handle a moderate load of real-time data processing. For high-load scenarios, further optimization and scaling strategies would be required.
- The current implementation does not include authentication or authorization mechanisms.

## Architecture
    ├── .gitignore
    ├── Makefile
    ├── README.md
    ├── requirements.txt
    ├── setup.py
    └── src/
      ├── __init__.py
      ├── __pycache__/
      ├── app/
      │   ├── __init__.py
      │   ├── data_generator.py
      │   ├── data_pipeline.py
      │   └── models.py
      ├── main.py
      ├── routers/
      │   ├── __init__.py
      │   └── data_router.py
      └── services/
        ├── __init__.py
        └── data_processing.py
