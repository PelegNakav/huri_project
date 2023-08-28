from download_csv import download_csv
from flask_testing import insert_data_from_csv, flask_app

if __name__ == "__main__":
    download_csv(r"C:\Code\Python\Jupyter\data\accidents.csv")
    insert_data_from_csv()
    flask_app()
