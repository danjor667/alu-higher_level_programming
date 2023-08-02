-- selecting cities from a particular states
SELECT id, name
FROM cities
WHERE state_id = (SELECT id WHERE name = 'California')
ORDER BY id;
