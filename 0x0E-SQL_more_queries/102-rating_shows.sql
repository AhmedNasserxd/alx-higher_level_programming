-- https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows_rate.sql
-- run this to import a SQL dump
-- script that lists all shows from hbtn_0d_tvshows_rate by their rating
-- each record should display: tv_shows.title - rating sum
-- results must be sorted in descending order by the rating
-- can use only one SELECT statement
-- the database name will be passed as an argument

SELECT title, SUM(tv_show_ratings.rate) 'rating'
FROM tv_shows
LEFT JOIN tv_show_ratings ON tv_show_ratings.show_id = tv_shows.id
GROUP BY title
ORDER BY rating DESC;
