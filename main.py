import os
import pandas as pd
from qbittorrent import Client
from tpblite import TPB, CATEGORIES, ORDERS
from dotenv import load_dotenv
from os import listdir
from os.path import isfile, join

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

# Filter to only the relevant rows
filmsNoBlanks = films[films['Film'].notnull()]
filmsNoDate = filmsNoBlanks[filmsNoBlanks['Date Watched'].isnull()]
filmsUnseen = filmsNoDate[filmsNoDate['Rating'].isnull()]
print(filmsUnseen)

# See what's already in the destination folder
files = [f for f in listdir(destination) if isfile(join(destination, f))]
print(files)
print(len(files))

# Get the next row of filmsUnseen, check if the name of the film is contained in a filename in the destination folder.
i = 0
while(i < len(filmsUnseen)):
    # Get film title and year
    filmTitle = filmsUnseen.iloc[i,0]
    filmYear = str(int(filmsUnseen.iloc[i,1]))
    filmSearch = filmTitle + " " + filmYear
    print(filmSearch)
    alreadyExists = False

    # Check if the film is already in the destination folder
    for f in files:
        if filmTitle in f:
            alreadyExists = True
            break

    if alreadyExists:
        print(filmSearch + " already exists. Going to next film.")
        i += 1
        continue
    else:
        # Go get the selected film
        print("Attempting to download: " + filmSearch)

        # Quick search for torrents, returns a Torrents object
        torrents = t.search(filmSearch, order=ORDERS.NAME.ASC, category=CATEGORIES.VIDEO.HD_MOVIES)

        # See how many torrents were found
        print('There were {0} torrents found.'.format(len(torrents)))

        # Iterate through list of torrents and print info for Torrent object
        for torrent in torrents:
            print(torrent)

        # Get the most seeded torrent based on a filter
        torrent = torrents.getBestTorrent(min_seeds=1, min_filesize='350 MiB', max_filesize='6 GiB')
        print("The best torrent is: ")
        print(torrent)

        # Get the magnet link for a torrent
        magLink = torrent.magnetlink
        print(magLink)
        break

#Qbittorrent
print("Qbit Torrent")
# connect to the qbittorent Web UI
qb = Client(qb_client)

# put the credentials (as you configured)
qb.login(qb_login, qb_password)

# Download film
qb.download_from_link(magLink, savepath=destination)