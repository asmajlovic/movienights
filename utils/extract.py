#!/usr/bin/python
import sqlite3
from random import shuffle
from sys import exit

db = sqlite3.connect('db/movienights.db')
c = db.cursor()

# Fetch the list of proposed movies for the past two weeks
query = """SELECT movie1, movie2, movie3, movie4, movie5
    FROM history
    ORDER BY date DESc
    LIMIT 2"""
res = c.execute(query).fetchall()
past_movies = set(res[0] + res[1])

# Now for the extraction
query = "SELECT title FROM movies WHERE watched IS NULL"
res = [a[0] for a in c.execute(query).fetchall()]
while True:
    shuffle(res)
    movie_list = set(res[:5])
    if not past_movies.intersection(movie_list):
        print '\n'.join(movie_list)
        exit()

