import unittest

from main import validate_row, clean_rows

class DataValidationTests(unittest.TestCase):

    def make_row(self, age="25", income="50000", name="John", id="101"):

        return {

            "id": id,

            "name": name,

            "age": age,

            "income": income,

        }

    def test_missing_age_is_detected(self):

        row = self.make_row(age="")

        self.assertIn("Missing or invalid age", validate_row(row))

    def test_invalid_age_is_detected(self):

        row = self.make_row(age="150")

        self.assertIn("Invalid age", validate_row(row))

    def test_negative_income_is_detected(self):

        row = self.make_row(income="-50000")

        self.assertIn("Negative income", validate_row(row))

    def test_duplicate_id_is_removed(self):

        rows = [

            self.make_row(id="101"),

            self.make_row(id="101", name="Another Person"),

        ]

        cleaned, issues, duplicates = clean_rows(rows)

        self.assertEqual(len(cleaned), 1)

        self.assertEqual(duplicates, 1)

    def test_invalid_age_is_cleaned(self):

        rows = [self.make_row(age="150")]

        cleaned, issues, duplicates = clean_rows(rows)

        self.assertEqual(cleaned[0]["age"], "Unknown")

if __name__ == "__main__":

    unittest.main()