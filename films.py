def filterFilms(films):
    # Filter to only the relevant rows
    filmsNoBlanks = films[films['Film'].notnull()]
    filmsNoDate = filmsNoBlanks[filmsNoBlanks['Date Watched'].isnull()]
    filmsUnseen = filmsNoDate[filmsNoDate['Rating'].isnull()]
    return(filmsUnseen)

def getFilmName(filmsUnseen, files):
    # Get the next row of filmsUnseen, check if the name of the film is contained in a filename in the destination folder.
    i = 0
    while (i < len(filmsUnseen)):
        # Get film title and year
        filmTitle = filmsUnseen.iloc[i, 0]
        filmYear = str(int(filmsUnseen.iloc[i, 1]))
        filmSearch = filmTitle + " " + filmYear
        print(filmSearch)
        alreadyExists = False

        # Check if the film is already in the destination folder
        for f in files:
            if filmTitle in f:
                alreadyExists = True
                break

        # If the film is already there, get the next film on the list
        if alreadyExists:
            print(filmSearch + " already exists. Going to next film.")
            i += 1
            continue
        else:
            return filmSearch