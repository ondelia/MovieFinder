from qbittorrent import Client
from tpblite import CATEGORIES, ORDERS

def connectToClient(qb_client, qb_login, qb_password):
    # connect to the qbittorent Web UI
    qb = Client(qb_client)

    # put the credentials (as you configured)
    qb.login(qb_login, qb_password)

    return qb

def getMagnetLink(t, filmSearch):
    # Quick search for torrents, returns a Torrents object
    torrents = t.search(filmSearch, order=ORDERS.NAME.ASC, category=CATEGORIES.VIDEO.HD_MOVIES)

    # Get the most seeded torrent based on a filter
    torrent = torrents.getBestTorrent(min_seeds=1, min_filesize='350 MiB', max_filesize='6 GiB')
    print(torrent)

    # Get the magnet link for a torrent
    magLink = torrent.magnetlink
    return(magLink)