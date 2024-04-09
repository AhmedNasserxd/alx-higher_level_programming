-- https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql
-- run this to import a SQL dump
-- script that uses the hbtn_0d_tvshows database to lists all genres not linked to Dexter
-- tv_shows table contains only one record where title = Dexter
-- each record should display: tv_genres.name
-- results must be sorted in ascending order by the genre name
-- can use max two SELECT statements
-- the database name will be passed as an argument

SELECT name
FROM tv_genres
WHERE name NOT IN
(SELECT name
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
LEFT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter')
GROUP BY name
ORDER BY name ASC;
