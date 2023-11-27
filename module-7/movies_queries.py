import mysql.connector

config = {
    "user": "movies_user",
    "password": "popcorn",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)

    print("\n    Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    print("-- DISPLAYING Studio RECORDS --")
    cursor = db.cursor()
    cursor.execute('SELECT * FROM movies.studio;')
    studios = cursor.fetchall()
    for studio in studios:
        print("Studio ID: {}\nStudio Name: {}\n".format(studio[0], studio[1]))

    print("-- DISPLAYING Genre RECORDS --")
    cursor = db.cursor()
    cursor.execute('SELECT * FROM movies.genre;')
    genres = cursor.fetchall()
    for genre in genres:
        print("Genre ID: {}\nGenre Name: {}\n".format(genre[0], genre[1]))

    print("-- DISPLAYING Short Film RECORDS --")
    cursor = db.cursor()
    cursor.execute('SELECT film_name, film_runtime FROM movies.film WHERE film_runtime < 120;')
    shortfilms = cursor.fetchall()
    for shortfilm in shortfilms:
        print("Film Name: {}\nRuntime: {}\n".format(shortfilm[0], shortfilm[1]))

    print("-- DISPLAYING Director RECORDS in Order --")
    cursor = db.cursor()
    cursor.execute('SELECT film_name, film_director FROM movies.film ORDER BY film_director;')
    directors = cursor.fetchall()
    for director in directors:
        print("Film Name: {}\nDirector: {}\n".format(director[0], director[1]))




finally:
    db.close()