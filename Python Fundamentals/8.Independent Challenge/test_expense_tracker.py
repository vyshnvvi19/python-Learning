import unittest
from unittest.mock import patch

import expense_tracker


class TestExpenseTracker(unittest.TestCase):

    def setUp(self):
        expense_tracker.records.clear()

    @patch(
        "builtins.input",
        side_effect=[
            "2026-09-22",
            "Food",
            "Lunch",
            "250",
            "Expense"
        ]
    )
    def test_add_expense(self, mock_input):
        expense_tracker.add_record()

        self.assertEqual(len(expense_tracker.records), 1)
        self.assertEqual(
            expense_tracker.records[0]["category"],
            "Food"
        )
        self.assertEqual(
            expense_tracker.records[0]["amount"],
            250
        )
        self.assertEqual(
            expense_tracker.records[0]["type"],
            "Expense"
        )

    @patch(
        "builtins.input",
        side_effect=[
            "2026-09-22",
            "Electronics",
            "Headphones",
            "2000",
            "Asset"
        ]
    )
    def test_add_asset(self, mock_input):
        expense_tracker.add_record()

        self.assertEqual(len(expense_tracker.records), 1)
        self.assertEqual(
            expense_tracker.records[0]["type"],
            "Asset"
        )

    @patch(
        "builtins.input",
        side_effect=[
            "invalid-date"
        ]
    )
    def test_invalid_date(self, mock_input):
        expense_tracker.add_record()

        self.assertEqual(len(expense_tracker.records), 0)

    @patch(
        "builtins.input",
        side_effect=[
            "2026-09-22",
            "Food",
            "Lunch",
            "-100"
        ]
    )
    def test_invalid_amount(self, mock_input):
        expense_tracker.add_record()

        self.assertEqual(len(expense_tracker.records), 0)

    def test_records_start_empty(self):
        self.assertEqual(expense_tracker.records, [])


if __name__ == "__main__":
    unittest.main()
    