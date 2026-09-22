from datetime import date
import csv
from pathlib import Path


records = []


def add_record():
    record_date = input("Enter date (YYYY-MM-DD): ").strip()

    try:
        date.fromisoformat(record_date)
    except ValueError:
        print("Invalid date.")
        return

    category = input("Enter category: ").strip()

    if not category:
        print("Category cannot be empty.")
        return

    description = input("Enter description: ").strip()

    if not description:
        print("Description cannot be empty.")
        return

    try:
        amount = float(input("Enter amount: "))

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

    except ValueError:
        print("Invalid amount.")
        return

    record_type = input("Enter type (Expense/Asset): ").strip().title()

    if record_type not in ["Expense", "Asset"]:
        print("Type must be Expense or Asset.")
        return

    record = {
        "date": record_date,
        "category": category,
        "description": description,
        "amount": amount,
        "type": record_type
    }

    records.append(record)

    print("Record added successfully.")


def view_records():
    if not records:
        print("No records found.")
        return

    print("\nAll Records")
    print("-" * 80)

    for index, record in enumerate(records, start=1):
        print(
            f"{index}. "
            f"{record['date']} | "
            f"{record['category']} | "
            f"{record['description']} | "
            f"₹{record['amount']:.2f} | "
            f"{record['type']}"
        )


def search_records():
    if not records:
        print("No records found.")
        return

    keyword = input(
        "Enter category or description to search: "
    ).strip().lower()

    if not keyword:
        print("Search value cannot be empty.")
        return

    found = False

    print("\nSearch Results")
    print("-" * 80)

    for record in records:
        if (
            keyword in record["category"].lower()
            or keyword in record["description"].lower()
        ):
            print(
                f"{record['date']} | "
                f"{record['category']} | "
                f"{record['description']} | "
                f"₹{record['amount']:.2f} | "
                f"{record['type']}"
            )

            found = True

    if not found:
        print("No matching records found.")


def show_summary():
    if not records:
        print("No records available.")
        return

    total = sum(record["amount"] for record in records)

    expense_total = sum(
        record["amount"]
        for record in records
        if record["type"] == "Expense"
    )

    asset_total = sum(
        record["amount"]
        for record in records
        if record["type"] == "Asset"
    )

    category_totals = {}

    for record in records:
        category = record["category"]

        category_totals[category] = (
            category_totals.get(category, 0)
            + record["amount"]
        )

    print("\nSummary")
    print("-" * 30)
    print(f"Total: ₹{total:.2f}")
    print(f"Expenses: ₹{expense_total:.2f}")
    print(f"Assets: ₹{asset_total:.2f}")

    print("\nCategory-wise Summary")

    for category, amount in category_totals.items():
        print(f"{category}: ₹{amount:.2f}")


def export_records():
    if not records:
        print("No records to export.")
        return

    file_path = Path("records.csv")

    try:
        with file_path.open(
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.DictWriter(
                file,
                fieldnames=[
                    "date",
                    "category",
                    "description",
                    "amount",
                    "type"
                ]
            )

            writer.writeheader()
            writer.writerows(records)

        print("Records exported successfully.")

    except OSError as error:
        print("Error exporting records:", error)


def import_records():
    file_path = Path("records.csv")

    if not file_path.exists():
        print("records.csv not found.")
        return

    imported_count = 0

    try:
        with file_path.open(
            "r",
            newline="",
            encoding="utf-8"
        ) as file:

            reader = csv.DictReader(file)

            required_fields = {
                "date",
                "category",
                "description",
                "amount",
                "type"
            }

            if not reader.fieldnames:
                print("Invalid CSV file.")
                return

            if not required_fields.issubset(reader.fieldnames):
                print("CSV file has missing columns.")
                return

            for row in reader:

                try:
                    date.fromisoformat(row["date"])

                    amount = float(row["amount"])

                    if amount <= 0:
                        continue

                    if row["type"] not in ["Expense", "Asset"]:
                        continue

                    if not row["category"].strip():
                        continue

                    if not row["description"].strip():
                        continue

                    record = {
                        "date": row["date"],
                        "category": row["category"].strip(),
                        "description": row["description"].strip(),
                        "amount": amount,
                        "type": row["type"]
                    }

                    records.append(record)
                    imported_count += 1

                except (ValueError, KeyError):
                    continue

        print(f"{imported_count} records imported successfully.")

    except (OSError, csv.Error) as error:
        print("Error importing records:", error)


def main():
    while True:
        print("\n==============================")
        print("    EXPENSE / ASSET TRACKER")
        print("==============================")

        print("1. Add Record")
        print("2. View Records")
        print("3. Search Records")
        print("4. Show Summary")
        print("5. Import Records")
        print("6. Export Records")
        print("7. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_record()

        elif choice == "2":
            view_records()

        elif choice == "3":
            search_records()

        elif choice == "4":
            show_summary()

        elif choice == "5":
            import_records()

        elif choice == "6":
            export_records()

        elif choice == "7":
            print("Thank you for using Expense / Asset Tracker.")
            break

        else:
            print("Invalid choice. Please enter 1-7.")


if __name__ == "__main__":
    main()