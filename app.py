import csv
import io
import os
import secrets
from collections import Counter

from flask import (
    Flask, render_template, request, send_file, session
)
from main import validate_row, clean_rows

app = Flask(__name__)

# For local development. Set FLASK_SECRET_KEY in the
# environment when deploying the application.
app.secret_key = os.environ.get("FLASK_SECRET_KEY") or secrets.token_hex(32)

app.config["MAX_CONTENT_LENGTH"] = 2 * 1024 * 1024

# Temporary server-side storage for demonstration results.
# Results are lost when the application restarts.
cleaned_results = {}


@app.route("/", methods=["GET", "POST"])
def index():
    report = None
    error = None

    if request.method == "POST":
        uploaded_file = request.files.get("file")

        if not uploaded_file or not uploaded_file.filename:
            error = "Please select a CSV file."
            return render_template(
                "index.html", report=report, error=error
            )

        if not uploaded_file.filename.lower().endswith(".csv"):
            error = "Please upload a file with a .csv extension."
            return render_template(
                "index.html", report=report, error=error
            )

        try:
            content = uploaded_file.stream.read().decode("utf-8-sig")
            reader = csv.DictReader(io.StringIO(content))

            expected_fields = {"id", "name", "age", "income"}

            if not reader.fieldnames or not expected_fields.issubset(
                set(reader.fieldnames)
            ):
                raise ValueError(
                    "The CSV must contain id, name, age, and income columns."
                )

            rows = list(reader)

            if not rows:
                raise ValueError("The CSV file contains no data rows.")

            if any(
                None in row or any(value is None for value in row.values())
                for row in rows
            ):
                raise ValueError(
                    "Some rows have missing columns. Check the CSV format."
                )

            if any(
                not row["id"].strip()
                for row in rows
            ):
                raise ValueError(
                    "Every row must have an ID so duplicates can be checked."
                )

            # Analyse the uploaded data before cleaning it.
            issue_types = Counter()
            affected_records = 0

            for row in rows:
                issues = validate_row(row)
                if issues:
                    affected_records += 1
                    issue_types.update(issues)

            cleaned, issue_count, duplicate_count = clean_rows(rows)

            # Keep the cleaned CSV in memory for downloading.
            output = io.StringIO(newline="")
            writer = csv.DictWriter(
                output,
                fieldnames=["id", "name", "age", "income"]
            )
            writer.writeheader()
            writer.writerows(cleaned)

            output_bytes = io.BytesIO(
                output.getvalue().encode("utf-8")
            )
            output_bytes.seek(0)

            report = {
                "original": len(rows),
                "affected": affected_records,
                "issues": issue_count,
                "duplicates": duplicate_count,
                "cleaned": len(cleaned),
                "breakdown": dict(issue_types),
            }

            # Store the report and result for this browser session.
            result_id = secrets.token_urlsafe(24)
            cleaned_results[result_id] = output_bytes.getvalue()
            session["result_id"] = result_id

            return render_template(
                "index.html", report=report, error=None
            )

        except (UnicodeDecodeError, csv.Error, ValueError) as exc:
            error = str(exc)

        except Exception:
            app.logger.exception("CSV processing failed")
            error = "The file could not be processed. Please check its format."

    return render_template("index.html", report=report, error=error)


@app.route("/download")
def download_file():
    result_id = session.get("result_id")
    cleaned_csv = cleaned_results.get(result_id)

    if cleaned_csv is None:
        return "Please upload and process a CSV file first.", 400

    return send_file(
        io.BytesIO(cleaned_csv),
        mimetype="text/csv",
        as_attachment=True,
        download_name="cleaned_data.csv",
    )


if __name__ == "__main__":
    app.run(debug=True)