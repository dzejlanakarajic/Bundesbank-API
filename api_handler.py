import os
import requests
import csv
import io

def construct_endpoint(base_url, flow_ref, key, start_period, end_period):
    endpoint = f"{base_url}/{flow_ref}/{key}?startPeriod={start_period}&endPeriod={end_period}&detail=dataonly"
    return endpoint


def make_api_request(url, folder, filename):
    headers = {'accept': 'text/csv'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        folder_path = os.path.join(os.getcwd(), folder)
        os.makedirs(folder_path, exist_ok=True)
        file_path = os.path.join(folder_path, filename)

        new_data = csv.reader(io.StringIO(response.text))
        header = next(new_data)

        mode = 'a' if os.path.exists(file_path) else 'w'
        with open(file_path, mode, newline='') as file:
            writer = csv.writer(file)
            if mode == 'w':
                writer.writerow(header)
            writer.writerows(new_data)
        return True
    else:
        return False


def fetch_data(base_url, flow_ref, key, start_period, end_period, folder):
    filename = f"{flow_ref}_{key}_data_raw.csv"
    endpoint = construct_endpoint(base_url, flow_ref, key, start_period, end_period)
    success = make_api_request(endpoint, folder, filename)
    return success
