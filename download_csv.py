def download_csv(csv_file_path = r'C:\Code\python\jupyter\data\accidents.csv', api_url = r'https://data.gov.il/api/3/action/datastore_search?resource_id=57c5aef9-70f9-4b71-82fa-52304cfbd031&limit=10000'):
    import pandas as pd
    import json
    import requests

    # Example API URL (replace with your actual URL)
    

    # Fetch JSON data from the API
    response = requests.get(api_url)
    json_data = response.content.decode('utf-8')  # Decode the bytes to a string

    # Parse the JSON data
    data = json.loads(json_data)
    records = data['result']['records']

    # Convert to DataFrame
    df = pd.DataFrame(records)

    # Define CSV file path
    

    # Save DataFrame to CSV
    df.to_csv(csv_file_path, index=False)

    print(f"Formatted data saved as CSV, path: {csv_file_path}")


