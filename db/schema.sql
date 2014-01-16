CREATE TABLE "history" (date numeric primary key, movie1 integer, movie2 integer, movie3 integer, movie4 integer, movie5 integer, winner int, foreign key(movie1) references movies(id), foreign key(movie2) references movies(id), foreign key(movie3) references movies(id), foreign key(movie4) references movies(id), foreign key(movie5) references movies(id));
CREATE TABLE movies(id integer PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, imdb_page TEXT, watched numeric);
CREATE TABLE users(id integer PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT, email TEXT, score integer);
