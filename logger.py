import csv
import os
from datetime import datetime


FILE = "data/sensor_data.csv"


def save_data(data, fault_code, fault_name):

    # Create data folder if it doesn't exist
    os.makedirs("data", exist_ok=True)

    file_exists = os.path.exists(FILE)

    with open(FILE, "a", newline="") as file:

        writer = csv.writer(file)

        # Write header only for a new file
        if not file_exists:
            writer.writerow([
                "timestamp",
                "temperature",
                "pressure",
                "voltage",
                "rpm",
                "fault_code",
                "fault"
            ])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            data["temperature"],
            data["pressure"],
            data["voltage"],
            data["rpm"],
            fault_code,
            fault_name
        ])