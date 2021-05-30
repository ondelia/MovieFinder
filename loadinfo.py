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

    # Use defaults if no value specified
    if not movie_list:
        movie_list = "Movie List.xlsx"
    if not destination:
        destination = "C:\Movies"
        try:
            os.mkdir(destination)
        except:
            pass
    if not qb_client:
        qb_client = "http://127.0.0.1:8080/"
    if not qb_login:
        qb_login = "admin"
    if not qb_password:
        qb_password = "adminadmin"

    # Load download source
    t = TPB()

    # Read the Excel file
    films = pd.read_excel(movie_list, sheet_name='Films', engine='openpyxl')

    # Return all values
    return destination, qb_client, qb_login, qb_password, t, films