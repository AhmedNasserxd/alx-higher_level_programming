-- lists all records of the table
-- Don’t list rows without a name value
-- display the score and the name (in this order)
-- listed by descending score
-- database name will be passed as an argument

SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
