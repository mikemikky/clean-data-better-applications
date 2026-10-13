# import csv

# INPUT_FILE = "sample_data.csv"

# OUTPUT_FILE = "cleaned_data.csv"

# def validate_row(row):

#     """Return a list of data quality problems."""

#     issues = []

#     if not row["name"].strip():

#         issues.append("Missing name")

#     if not row["age"].strip():

#         issues.append("Missing age")

#     else:

#         try:

#             age = int(row["age"])

#             if age < 0 or age > 120:

#                 issues.append("Invalid age")

#         except ValueError:

#             issues.append("Age is not a number")

#     if not row["income"].strip():

#         issues.append("Missing income")

#     else:

#         try:

#             income = float(row["income"])

#             if income < 0:

#                 issues.append("Negative income")

#         except ValueError:

#             if row["income"].strip().lower() != "unknown":

#                 issues.append("Income is not a number")

#     return issues

# def main():

#     with open(INPUT_FILE, "r", newline="", encoding="utf-8") as file:

#         reader = csv.DictReader(file)

#         rows = list(reader)

#     seen_ids = set()

#     cleaned_rows = []

#     issue_count = 0

#     duplicate_count = 0

#     for row in rows:

#         row_issues = validate_row(row)

#         if row_issues:

#             issue_count += len(row_issues)

#             print(f"ID {row['id']}: {', '.join(row_issues)}")

#         if row["id"] in seen_ids:

#             duplicate_count += 1

#             print(f"ID {row['id']}: Duplicate record removed")

#             continue

#         seen_ids.add(row["id"])

#         # Replace missing or invalid values with "Unknown".

#         for field in ["name", "age", "income"]:

#             value = row[field].strip()

#             if not value or value.lower() == "unknown":

#                 row[field] = "Unknown"

#             elif field == "age":

#                 try:

#                     age = int(value)

#                     if age < 0 or age > 120:

#                         row[field] = "Unknown"

#                 except ValueError:

#                     row[field] = "Unknown"

#             elif field == "income":

#                 try:

#                     income = float(value)

#                     if income < 0:

#                         row[field] = "Unknown"

#                 except ValueError:

#                     row[field] = "Unknown"

#         cleaned_rows.append(row)

#     with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:

#         writer = csv.DictWriter(

#             file,

#             fieldnames=["id", "name", "age", "income"]

#         )

#         writer.writeheader()

#         writer.writerows(cleaned_rows)
#     print("\n--- DATA CLEANING REPORT ---")
#     print(f"Original records: {len(rows)}")
#     print(f"Data quality issues detected: {issue_count}")
#     print(f"Duplicate records removed: {duplicate_count}")
#     print(f"Cleaned records: {len(cleaned_rows)}")
#     print(f"Output saved to: {OUTPUT_FILE}")

# if __name__ == "__main__":
#     main()


import csv

from collections import Counter

INPUT_FILE = "sample_data.csv"

OUTPUT_FILE = "cleaned_data.csv"

def validate_row(row):

    """Identify data quality problems in one row."""

    issues = []

    if not row["name"].strip():

        issues.append("Missing name")

    try:

        age = int(row["age"])

        if age < 0 or age > 120:

            issues.append("Invalid age")

    except ValueError:

        issues.append("Missing or invalid age")

    try:

        income = float(row["income"])

        if income < 0:

            issues.append("Negative income")

    except ValueError:

        if row["income"].strip().lower() != "unknown":

            issues.append("Missing or invalid income")

    return issues

def clean_rows(rows):

    """Remove duplicate IDs and clean invalid values."""

    seen_ids = set()

    cleaned_rows = []

    issue_count = 0

    duplicate_count = 0

    for original_row in rows:

        row = original_row.copy()

        issues = validate_row(row)

        issue_count += len(issues)

        if row["id"] in seen_ids:

            duplicate_count += 1

            continue

        seen_ids.add(row["id"])

        for field in ["name", "age", "income"]:

            value = row[field].strip()

            if not value or value.lower() == "unknown":

                row[field] = "Unknown"

            elif field == "age":

                try:

                    age = int(value)

                    if age < 0 or age > 120:

                        row[field] = "Unknown"

                except ValueError:

                    row[field] = "Unknown"

            elif field == "income":

                try:

                    income = float(value)

                    if income < 0:

                        row[field] = "Unknown"

                except ValueError:

                    row[field] = "Unknown"

        cleaned_rows.append(row)

    return cleaned_rows, issue_count, duplicate_count

def main():

    with open(INPUT_FILE, "r", newline="", encoding="utf-8") as file:

        rows = list(csv.DictReader(file))

    cleaned, issues, duplicates = clean_rows(rows)

    # Count each type of issue in the original dataset.

    issue_types = Counter()

    rows_with_issues = 0

    for row in rows:

        row_issues = validate_row(row)

        if row_issues:

            rows_with_issues += 1

            issue_types.update(row_issues)

    # Save cleaned data to a separate file.

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:

        writer = csv.DictWriter(

            file, fieldnames=["id", "name", "age", "income"]

        )

        writer.writeheader()

        writer.writerows(cleaned)

    print("\n========== DATA QUALITY REPORT ==========")

    print(f"Original records: {len(rows)}")

    print(f"Records with validation issues: {rows_with_issues}")

    print(f"Total validation issues: {issues}")

    print(f"Duplicate records removed: {duplicates}")

    print(f"Cleaned records: {len(cleaned)}")

    print("\nIssue breakdown:")

    if issue_types:

        for issue, count in sorted(issue_types.items()):

            print(f"- {issue}: {count}")

    else:

        print("- No validation issues found.")

    print(f"\nCleaned data saved to: {OUTPUT_FILE}")

    print("Original dataset preserved.")

if __name__ == "__main__":

    main()