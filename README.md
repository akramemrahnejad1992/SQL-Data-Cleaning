# Data Cleaning Project

## Overview
This project involves data cleaning and preprocessing using Python to connect to a PostgreSQL database and run SQL queries. A key focus is on SQL data cleaning methods, which are employed to clean and preprocess the data directly within the database before it is pulled for further analysis. Additionally, you can use SQL Server Integration Services (SSIS) to write and execute queries directly against the database. The goal is to ensure high-quality data by addressing inconsistencies, missing values, and other data quality issues.

## Table of Contents
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Project Structure](#project-structure)

## Technologies Used
- **Python**: For data manipulation and processing.
- **pandas**: For handling and processing data.
- **SQL**: For querying the PostgreSQL database and performing data cleaning.
- **PostgreSQL**: The database used for storing and retrieving data.
- **SSIS**: For writing and executing SQL queries directly (if desired).

## Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. **Set up a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up PostgreSQL:**
   - Ensure you have PostgreSQL installed on your machine.
   - Create a new database and user if necessary.
   - Update the connection settings in the code to connect to your PostgreSQL database.

## Usage
1. **Run SQL Queries**: Use the provided SQL scripts to clean the data within the database before extraction. You can also use SSIS to write and execute queries directly.
2. **Data Processing**: Execute the Python scripts to perform additional data cleaning and processing.
   ```bash
   python main.py
   ```

## Project Structure
```
your-repo-name/
│
├── data/
│   ├── load_data.py               # Script to load data from the database
│   └── process_data.py            # Script for additional data processing
│
├── db/                   
│   ├── create_tables.py           # Script to create database tables
│   ├── db_connections.py          # Database connection settings
│   ├── queries.py                 # SQL queries for data cleaning
│   ├── insert_data.py             # Script to insert data into tables
│   └── views.py                   # SQL views for simplified data access
│
├── main.py                        # Main script for running the data cleaning process
├── requirements.txt               # Python dependencies
└── README.md                      # Project documentation
```
