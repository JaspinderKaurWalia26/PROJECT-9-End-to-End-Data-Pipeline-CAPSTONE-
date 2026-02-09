# End-to-End Data Pipeline (CAPSTONE)

## Project Overview
End-to-End Data Pipeline is a mini production-grade backend pipeline built using Python.
The project demonstrates how real-world systems fetch data asynchronously, process it, store outputs, handle failures with retries, and log every step.

---

## What does this project do?
- Fetches data from multiple APIs concurrently using async programming
-Processes and transforms the fetched data
- Stores processed output in CSV files
- Implements retry mechanism for failed API calls
- Logs:
   - Pipeline start and completion
   - API success and failure

---

## Why Async Programming is Used:
In real backend systems, data often comes from multiple external services.
Fetching them one by one blocks execution and slows the system.

Async programming allows:
- Multiple API requests to run in parallel
- Faster pipeline execution
- Better scalability
---

##  Technologies Used
- Python 3
- asyncio
- aiohttp
- logging module
- csv module
- python-dotenv
- os module
---

## Project Structure
```
END_TO_END_DATA_PIPELINE/
│
├── data/
│   ├── posts.csv          # Processed posts data
│   └── users.csv          # Processed users data
│
├── logs/
│   └── pipeline.log       # Complete pipeline execution logs
│
├── src/
│   └── data_pipeline/
│       ├── __init__.py        # Marks package
│       ├── extractor.py      # Async API data fetching (with retry)
│       ├── transformer.py    # Data processing & transformation logic
│       ├── loader.py         # Stores processed data into CSV files
│       ├── logger_config.py  # Centralized logging configuration
│       ├── pipeline.py       # End-to-end pipeline orchestration
│       └── main.py           # Pipeline entry point
│
├── .env                  # Environment-based configuration (API URLs, retries)
├── README.md             # Project documentation
└── requirements.txt      # Project dependencies

```
## How to Run

### 1. Clone the repository
```
git clone https://github.com/JaspinderKaurWalia26/PROJECT-9-End-to-End-Data-Pipeline-CAPSTONE-.git
cd PROJECT-9-End-to-End-Data-Pipeline-CAPSTONE
```
### 2. Create a virtual environment (optional)
```
python -m venv venv
```
### 3. Activate the virtual environment
- Windows:
```
venv\Scripts\activate
```
- Linux/Mac:
```
source venv/bin/activate
```
### 4. Install dependencies
```
pip install -r requirements.txt
```
### 5. Run the program
```
python -m src.data_pipeline.main
```
### 6. Check outputs

- Processed data:
     - posts.csv
     - users.csv

- Logs: logs/pipeline.log



