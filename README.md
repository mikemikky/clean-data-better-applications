Clean Data, Better Applications
A Python data validation and cleaning project that demonstrates how simple validation rules can help improve data quality in applications.

## Application Preview
![clean Data application dashboard](screenshots/dashboard.png/dashboardc.png)

Overview
Data quality is important for building reliable software. Missing values, invalid ages, negative income values, and duplicate records can cause problems when applications process data.

This project uses Python and Flask to validate uploaded CSV files, identify common data quality issues, and provide a cleaned CSV file for download.

Features
* Upload CSV files through a web interface.
* Validate required columns: id, name, age, and income.
* Identify missing or invalid age values.
* Flag negative income values.
* Detect duplicate IDs.
* Generate a data quality report.
* Download the cleaned CSV output.
* Reject unsupported file types and CSV files missing required columns.
* Run automated tests with Python’s unittest framework.

Technologies Used

* Python
* Flask
* HTML and CSS
* Chart.js
* CSV data processing
* unittest

Project Structure

clean-data-better-applications/
├── app.py
├── main.py
├── test_main.py
├── sample_data.csv
├── README.md
└── templates/
    └── index.html

Getting Started

1. Clone the repository

git clone https://github.com/mikemikky/clean-data-better-applications.git
cd clean-data-better-applications

2. Create a virtual environment

python -m venv venv

Activate it on Windows:

venv\Scripts\activate

3. Install Flask

python -m pip install Flask

4. Run the application

python app.py

Open the local address displayed in your terminal in your web browser.

Run the Tests

Run the automated tests with:

python -m unittest

Sample Data

The repository includes sample_data.csv for testing common data quality issues. It contains synthetic practice data and should not be treated as real-world or official statistics.

Limitations
This is a learning project and prototype. Its validation rules are intentionally simple and may need to be adapted for different datasets and business requirements. It has not been presented as a production-ready data processing system.

Future Improvements
* Add more configurable validation rules.
* Improve validation summaries and reporting.
* Expand automated test coverage.
* Improve handling of larger datasets.
* Prepare the application for secure production deployment.

Author
Created by mikemikky as a practical Python software development project exploring data validation, data cleaning, and web application development.

Project Roadmap

* [x]	Build a CSV validation and cleaning application.
* [x]	Create a Flask web interface for uploading CSV files.
* [x]	Generate data quality reports and cleaned CSV downloads.
* [x]	Add automated tests for core validation logic.
* [x]	Document installation and usage instructions.
* [x]	Add an application screenshot to the README.
* [ ]	Expand automated test coverage.
* [ ]	Improve validation rules and error reporting.
* [ ]	Prepare the application for secure public deployment.

Learning Goals
This project helps me develop practical skills in Python programming, data validation, automated testing, and web application development. I plan to improve it incrementally as I learn new techniques.
