# Huri Project

## Download and Run Instructions

1. Clone the project repository:
git clone https://github.com/PelegNakav/huri_project.git

2. Navigate to the project directory:
cd huri_project

3. Run the project:
py main.py

4. Open the website in your browser:
http://127.0.0.1:5000/

## Project Overview

The Huri Project involves several key steps:

1. Sending an API Request: The project initiates an API request to www.gov.il to fetch a dataset.

2. Dataset Storage: The retrieved dataset is stored in a database using SQLite.

3. Web Display: The project presents the contents of the database in a user-friendly website using Flask.

## Features

To add new data entries to the database, you can use the following feature:

### Adding Rows via API

You can use the following command to send a POST API request and add new rows to the database:

curl -X POST -H "Content-Type: application/json" -d "[{\"CITY\": \"Sample City\"}]" http://127.0.0.1:5000/add_row

## Here are the details of this feature:

Send a POST API request to http://127.0.0.1:5000/add_row.
Specify the columns and their values that you want to add to the database.
If a column is not specified, its value will be set to "None."
If you attempt to add a column that doesn't exist, an error will be returned.

## Changing Dataset via Upload
You can also update the dataset in the database using the following feature:

Click on the "Upload Dataset" button on the website.
Select a new CSV file containing the updated dataset.
The uploaded data will replace the existing dataset in the database.
