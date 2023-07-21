# Bundesbank Data Fetch and Store

This Python-based project fetches data about the mortgage loan financing volume from the Bundesbank API and stores it in a PostgreSQL database. The data corresponds to "Neugeschäftsvolumina Banken DE / Wohnungsbaukredite an private Haushalte insgesamt".

## Project Structure

The project is organized into several Python scripts:

- `api_handler.py`: Contains functions for making requests to the Bundesbank API.
- `db_connector.py`: Contains functions for managing the database connection and executing SQL commands.
- `main.py`: Orchestrates the process of fetching data and loading it into the database.
- `config.py`: Holds configuration data such as the API base URL and database connection parameters.

## Prerequisites

To run this project, you need:

- Python 3.8 or higher
- PostgreSQL

You can install Python from [the official website](https://www.python.org/downloads/) and PostgreSQL from [the official website](https://www.postgresql.org/download/).

You also need to install the necessary Python packages, which are listed in the `requirements.txt` file. You can install them using pip:

```bash
pip install -r requirements.txt
```

## How to Run the Scripts

Before you run the scripts, ensure your PostgreSQL database is set up and update the `config.py` file with your database connection parameters. The database password should be stored as an environment variable.

To fetch the data and load it into the database, run:

```bash
python main.py
```
## License

This project is released under the MIT License. See the [LICENSE](LICENSE) file for more details.
