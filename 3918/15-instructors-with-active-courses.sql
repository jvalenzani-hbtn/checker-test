SELECT DISTINCT i.name AS instructor_name
FROM instructors AS i
INNER JOIN courses AS c ON i.id = c.instructor_id
WHERE c.id IN (
    SELECT r.course_id
    FROM registrations AS r
)
ORDER BY i.name ASC;
