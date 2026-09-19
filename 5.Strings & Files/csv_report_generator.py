import csv
from pathlib import Path

from log_parser import parse_log_file


def generate_csv_report(records, summary, file_path):
    report_file = Path(file_path)

    try:
        with report_file.open(
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.writer(file)

            writer.writerow(["Log Level", "Count"])

            for level, count in summary.items():
                writer.writerow([level, count])

            writer.writerow([])

            writer.writerow([
                "Date",
                "Time",
                "Level",
                "Message"
            ])

            for record in records:
                writer.writerow([
                    record["date"],
                    record["time"],
                    record["level"],
                    record["message"]
                ])

        print("CSV report created successfully.")

    except OSError as error:
        print("Error creating CSV report:", error)


records, summary = parse_log_file("app.log")

generate_csv_report(
    records,
    summary,
    "log_report.csv"
)