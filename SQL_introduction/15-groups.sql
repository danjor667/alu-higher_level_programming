-- count score and group it by score
SELECT score, COUNT(score) AS number
FROM second_table
GROUP BY number
ORDER BY score
