# MovieFinder
This project will read a list of movies, find the first movie on the list you haven't seen, and download it.

## Program Steps
1. Check to make sure there are fewer than 10 movies in your destination folder (so that you don't have too many clogging up space).
2. Open an Excel spreadsheet containing a list of films, release years, date watched, and ratings. See the example file.
3. If you haven't watched a film yet, make sure there is nothing in the Date Watched or Rating field.
4. In the same folder as your main.py script, create a .env file with the following variables: MOVIE_LIST, DESTINATION_FOLDER, QB_CLIENT, QB_LOGIN, QB_PASSWORD. The first is the path to your Excel spreadsheet with a list of films, the second is the path to your destination folder, and the last three are your login credentials for qBitTorrent. Alternatively, you can modify the default values for these variables in the loadinfo.py file.
5. Open qBitTorrent before you run the program.
6. Run main.py from your command prompt.

## Instructions
Keep your destination folder clean. Delete movies after you watch them, and don't put other stuff in this folder. Keep your spreadsheet up to date, so that the program doesn't download a film you've already watched.

## No Piracy
This program should not be used for piracy, or downloading copyrighted/illegal things. I like to watch old silent films which are in the public domain; if you use it for something nefarious, that's on you. By using this program, you agree to not use it to break the law.
