-- lists all the cities of California that can be found
-- states table contains only one record where name = California
-- results must be sorted in ascending order by cities.id
-- not allowed to use the JOIN keyword
-- the database name will be passed as an argument

SELECT id, name
  FROM cities
 WHERE state_id = (SELECT id FROM states WHERE name = "California") GROUP BY id ORDER BY id ASC;
