-- listing all yhe cities in the database
SELECT cities.id, cities.state, state.name
FROM cities INNER JOIN states
ON cities.state_id = states.id
ORDER BY id;
