from loadinfo import loadinfo
from films import *
from torrents import *

# Load information
destination, qb_client, qb_login, qb_password, t, films = loadinfo()

# Filter to only the relevant rows
filmsUnseen = filterFilms(films)
print(filmsUnseen)

# Get the next row of filmsUnseen, check if the name of the film is contained in a filename in the destination folder.
try:
    filmSearch = getFilmName(filmsUnseen, destination)
except:
    raise RuntimeError('No film to download.')

# Get the magnet link
magLink = getMagnetLink(t, filmSearch)

# Connect to Qbittorrent
qb = connectToClient(qb_client, qb_login, qb_password)

# Download film
qb.download_from_link(magLink, savepath=destination)
print("Downloading: " + filmSearch)
