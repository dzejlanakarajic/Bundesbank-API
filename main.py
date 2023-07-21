from api_handler import fetch_data
from db_connector import connect_to_database, insert_data_to_db
import pandas as pd
import config

# Call the fetch_data function with the desired flow_ref, key, start_period, and end_period
success = fetch_data(config.base_url, "BBK01", "SUD231", start_period="2013-01", end_period="2023-03")

if success:
    print("Data downloaded successfully.")
    # Read CSV data
    df = pd.read_csv('Your_Path_Data_Raw.csv', sep=';')

    con = connect_to_database(config.db_name, config.user, config.host, config.password)
    insert_data_to_db(con, df)
    print("Data loaded successfully")

else:
    print("Error occurred while fetching data.")
