-- https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql
-- run this to import a SQL dump
-- script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
-- each record should display: tv_genres.name, and number_shows
-- don’t display a genre that doesn’t have any shows linked
-- results must be sorted in descending order by the number of shows linked
-- can use only one SELECT statement
-- the database name will be passed as an argument

SELECT tv_genres.name AS 'genre', COUNT(tv_show_genres.genre_id) AS 'number_of_shows'
FROM tv_genres RIGHT JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;
