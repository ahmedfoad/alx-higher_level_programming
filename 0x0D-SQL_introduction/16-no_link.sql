-- Lists all records from the `second_table` table with a name value in my MySQL server, ordered by descending score.
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
