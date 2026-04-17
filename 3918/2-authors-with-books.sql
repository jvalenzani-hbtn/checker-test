SELECT a.name AS author_name, b.title AS title
FROM authors AS a
LEFT JOIN books AS b ON a.id = b.author_id
ORDER BY a.name ASC, b.title ASC;
