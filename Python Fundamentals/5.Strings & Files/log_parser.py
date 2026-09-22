from pathlib import Path
LOG_LEVELS = {"INFO", "WARNING", "ERROR"}
def parse_log_file(file_path):
    log_file = Path(file_path)

    records = []
    summary = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0
    }

    try:
        lines = log_file.read_text(encoding="utf-8").splitlines()

    except FileNotFoundError:
        print("Error: Log file not found.")
        return records, summary

    except UnicodeDecodeError:
        print("Error: Invalid file encoding.")
        return records, summary

    except OSError as error:
        print("Error reading file:", error)
        return records, summary

    for line in lines:

        parts = line.split(" ", 3)

        if len(parts) != 4:
            print("Skipping invalid line:", line)
            continue

        date = parts[0]
        time = parts[1]
        level = parts[2]
        message = parts[3]

        if level not in LOG_LEVELS:
            print("Skipping unsupported log level:", level)
            continue

        record = {
            "date": date,
            "time": time,
            "level": level,
            "message": message
        }

        records.append(record)
        summary[level] += 1

    return records, summary


if __name__ == "__main__":
    records, summary = parse_log_file("app.log")

    print("\nLog Summary")
    print("-----------")

    for level, count in summary.items():
        print(f"{level}: {count}")