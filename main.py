import os
import pandas as pd
import time
import sys
import urllib.request as r
import torrent_crawler
import asyncio
from qbittorrent import Client
from pyYify import yify
from magnet2torrent import Magnet2Torrent, FailedToFetchException
from tpblite import TPB, CATEGORIES, ORDERS
from dotenv import load_dotenv
from os import listdir
from os.path import isfile, join

# Make asyncio work for Windows
if sys.version_info[0] == 3 and sys.version_info[1] >= 8 and sys.platform.startswith('win'):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# Load environment
load_dotenv()
movie_list = os.getenv('MOVIE_LIST')
destination = os.getenv('DESTINATION_FOLDER')

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
    print(filmTitle + " " + filmYear)
    alreadyExists = False

    # Check if the film is already in the destination folder
    for f in files:
        if filmTitle in f:
            alreadyExists = True
            break

    if alreadyExists:
        i += 1
        continue
    else:
        # Go get the selected film
        print(filmTitle)

        #t.search('public domain', category=CATEGORIES.VIDEO.MOVIES)

        movie = "The General 1926"

        # Quick search for torrents, returns a Torrents object
        torrents = t.search(movie, order=ORDERS.NAME.ASC, category=CATEGORIES.VIDEO.HD_MOVIES)

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

# Download torrent from magnet link
async def fetch_that_torrent(magLink):
    m2t = Magnet2Torrent(magLink)
    try:
        filename, torrent_data = await m2t.retrieve_torrent()
        return filename, torrent_data
    except FailedToFetchException:
        print("Failed")

filename, torrent_data = asyncio.run(fetch_that_torrent(magLink))
print("Test2")
print(filename)
print(torrent_data)

#Qbittorrent
print("Qbit Torrent")
# connect to the qbittorent Web UI
qb = Client("http://127.0.0.1:8080/")

# put the credentials (as you configured)
qb.login("admin", "adminadmin")

fullPath = os.getcwd() + '\\' + destination
qb.download_from_link(magLink, savepath=destination)