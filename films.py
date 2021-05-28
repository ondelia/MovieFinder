import re
from os import listdir

def filterFilms(films):
    # Filter to only the relevant rows
    filmsNoBlanks = films[films['Film'].notnull()]
    filmsNoDate = filmsNoBlanks[filmsNoBlanks['Date Watched'].isnull()]
    filmsUnseen = filmsNoDate[filmsNoDate['Rating'].isnull()]
    return(filmsUnseen)

def getFilmName(filmsUnseen, destination):
    # Get the next row of filmsUnseen, check if the name of the film is contained in a filename in the destination folder.
    i = 0
    while (i < len(filmsUnseen)):
        # Get film title and year
        filmTitle = filmsUnseen.iloc[i, 0]
        filmYear = str(int(filmsUnseen.iloc[i, 1]))
        filmSearch = filmTitle + " " + filmYear

        if len(listdir(destination)) > 9:
            raise ValueError('Too many files in destination folder. Delete some and try again.')

        # If the film is already in the destination folder, get the next film on the list
        if alreadyExists(filmTitle, destination):
            print(filmSearch + " already exists. Going to next film.")
            i += 1
        else:
            return filmSearch
    raise ValueError('No remaining films on list to download.')

def alreadyExists(filmTitle, destination):
    # See what's already in the destination folder
    files = [f for f in listdir(destination)]

    # Standardize the film titles
    filmTitleTemp = re.sub(r'[^\w\s]', '', filmTitle)
    filmTitleTemp = filmTitleTemp.lower()
    filmTitleTemp = filmTitleTemp.replace(' ', '')

    # Check if the film is already in the destination folder
    for f in files:
        f = re.sub(r'[^\w\s]', '', f)
        f = f.lower()
        f = f.replace(' ', '')

        if filmTitleTemp in f:
            return(True)

    return(False)