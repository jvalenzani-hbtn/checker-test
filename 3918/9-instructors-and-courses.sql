SELECT i.name AS instructor_name, c.title AS course_title
FROM instructors AS i
LEFT JOIN courses AS c ON i.id = c.instructor_id
ORDER BY i.name ASC, c.title ASC;
