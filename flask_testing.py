from flask import Flask, render_template, request, jsonify
from flask_uploads import UploadSet, configure_uploads, DATA
from io import StringIO
import sqlite3
import os
import pandas as pd
from download_csv import download_csv


db_path = r'db/my_database.db'  # SQLite database path
table_name = 'accidents'
csv_path = r"C:\Code\Python\Jupyter\data\accidents.csv"


def flask_app():
    app = Flask(__name__)
    uploads = UploadSet('uploads', DATA) # uploads object the accepts csv
    app.config['UPLOADED_UPLOADS_DEST'] = 'uploads' # dest directory of files
    configure_uploads(app, uploads) # connect between the app and the uploads object

    @app.route('/', methods=['GET', 'POST'])
    def display_database():
        if request.method == 'POST' and 'csv_file' in request.files: # if file has been uploded
            csv_file = request.files['csv_file']
            if csv_file.filename.endswith('.csv'):
                csv_data = csv_file.read().decode('utf-8')
                df = pd.read_csv(StringIO(csv_data))
                db_connection = sqlite3.connect(db_path)
                df.to_sql(table_name, db_connection, if_exists='replace', index=False)
                db_connection.close()
                return render_template('index.html', data=df.to_html())

        # If no file is specified, fetch data from the SQLite database
        db_connection = sqlite3.connect(db_path)
        query = f"SELECT * FROM {table_name};"
        df = pd.read_sql(query, db_connection)
        db_connection.close()

        return render_template('index.html', data=df.to_html())

    @app.route('/add_row', methods=['POST'])
    def add_row():
        content = request.json
        df = pd.DataFrame(content)
        db_connection = sqlite3.connect(db_path)
        existing_columns = pd.read_sql(f"PRAGMA table_info({table_name})", db_connection)["name"]
        # Set missing values in the DataFrame
        for column in existing_columns:
            if column not in df.columns:
                df[column] = None
        df.to_sql(table_name, db_connection, if_exists='append', index=False)
        return render_template('index.html', data=content)

    app.run()

def insert_data_from_csv():
    if os.path.exists(csv_path):
        import pandas as pd
        import sqlite3

        # Read CSV data into a pandas DataFrame
        df = pd.read_csv(csv_path)

        # Connect to the SQLite database
        db_connection = sqlite3.connect(db_path)  # Replace with your database file name

        # Write DataFrame to SQLite database

        df.to_sql(table_name, db_connection, if_exists='replace', index=False)

        # Close the database connection
        db_connection.close()

        print("CSV data inserted into the SQLite database.")

