import os
import pandas as pd
from dotenv import load_dotenv
from tpblite import TPB

def loadinfo():
    # Load environment
    load_dotenv()
    movie_list = os.getenv('MOVIE_LIST')
    destination = os.getenv('DESTINATION_FOLDER')
    qb_client = os.getenv('QB_CLIENT')
    qb_login = os.getenv('QB_LOGIN')
    qb_password = os.getenv('QB_PASSWORD')

    # Load download source
    t = TPB()

    # Read the Excel file
    films = pd.read_excel(movie_list, sheet_name='Films', engine='openpyxl')

    # Return all values
    return destination, qb_client, qb_login, qb_password, t, films