SELECT s.name AS student_name, c.title AS course_title
FROM registrations AS r
INNER JOIN students AS s ON r.student_id = s.id
INNER JOIN courses AS c ON r.course_id = c.id
ORDER BY s.name ASC, c.title ASC;
