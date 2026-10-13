Clean Data, Better Applications: Simple Data Validation with Python

Project Overview

This project demonstrates how Python can identify and handle common data-quality problems in CSV files.

It was developed as a practical learning project to explore data validation, data cleaning, automated testing, and web application development.

Features

* Upload CSV files through a web interface.
* Detect missing values and invalid ages.
* Identify negative income values.
* Detect and remove duplicate IDs.
* Replace selected missing or invalid values with Unknown.
* Display a data-quality report and bar chart.
* Download the cleaned CSV file.
* Run automated tests to check core validation and cleaning functions.

Technologies Used

* Python
* Flask
* HTML and CSS
* Chart.js
* Python unittest
* CSV file handling

Project Structure

clean_data_project/
├── app.py
├── main.py
├── test_main.py
├── sample_data.csv
├── cleaned_data.csv
├── README.md
└── templates/
    └── index.html

How to Run the Project

1. Install Python.
2. Install Flask:
    python -m pip install flask
3. Start the web application:
    python app.py
4. Open http://127.0.0.1:5000 in your browser.
5. Upload a CSV file containing the required columns: id, name, age, and income.
6. Review the data-quality report and download the cleaned file.

Run the Automated Tests

Run:

python -m unittest -v

The tests check selected validation and cleaning behaviours, including missing ages, invalid ages, negative income, and duplicate IDs.

Dataset and Limitations

The included sample dataset contains synthetic practice records, not real personal or financial data.

This project is a learning prototype. It is not yet designed for large datasets, concurrent users, or public production deployment. Replacing invalid values with Unknown is a simplified demonstration and may not be appropriate for every real-world application.

Learning Goals

This project explores how validation rules, automated tests, and clear reporting can improve confidence in data used by software applications.