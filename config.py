import os

base_url = "https://api.statistiken.bundesbank.de/rest/data"
db_name = 'DB_NAME'
user = 'DB_USER'
password = os.getenv('DB_PASSWORD')  # Fetching sensitive data from environment variables
host = 'DB_HOST'
