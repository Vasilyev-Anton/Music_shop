import sqlalchemy

db = 'postgresql://postgres:314159W@localhost:5432/postgres'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()

album = connection.execute("""
SELECT title, release_year FROM album
    WHERE release_year = 2018
    """).fetchall()
print('Альбомы, выпущенные в 2018г.:', album)

longest_track = connection.execute("""
SELECT title, duration1 FROM track
    ORDER BY duration1 DESC
    LIMIT 1
    """).fetchall()
print('Самый длинный трек:', longest_track)

time_track = connection.execute("""
SELECT title, duration1 FROM track
    WHERE duration1 >= 3.5
    """).fetchall()
print('Треки, длящиеся не менее 3,5минут:', time_track)

songster = connection.execute("""
SELECT title, release_year FROM songster
    WHERE release_year BETWEEN 2018 AND 2020
    """).fetchall()
print('Сборники, выпущенные с 2018г. по 2020г.:', songster)

singer_name = connection.execute("""
SELECT name_singer FROM singer
    WHERE NOT name_singer LIKE ('%% %%')
    """).fetchall()
print('Исполнители, чье имя состоит из 1 слова:', singer_name)

title_track = connection.execute("""
SELECT title FROM track
    WHERE title iLIKE '%%my%%'
    """).fetchall()
print('Треки, содержащие в названии "My"', title_track)
