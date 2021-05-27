from loadinfo import loadinfo
from films import *
from torrents import *
from os import listdir
from os.path import isfile, join

# Load information
destination, qb_client, qb_login, qb_password, t, films = loadinfo()

# See what's already in the destination folder
files = [f for f in listdir(destination) if isfile(join(destination, f))]
print(files)
print(len(files))

# Filter to only the relevant rows
filmsUnseen = filterFilms(films)
print(filmsUnseen)

# Get the next row of filmsUnseen, check if the name of the film is contained in a filename in the destination folder.
filmSearch = getFilmName(filmsUnseen, files)
print("Attempting to download: " + filmSearch)

# Get the magnet link
magLink = getMagnetLink(t, filmSearch)

# Connect to Qbittorrent
qb = connectToClient(qb_client, qb_login, qb_password)

# Download film
qb.download_from_link(magLink, savepath=destination)