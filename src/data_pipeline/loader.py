import csv
import os
from .logger_config import get_logger


logger = get_logger(__name__)
# saving to csv format
def save_csv(data, path, fields):
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)

    logger.info(f"Data saved to {path}")
