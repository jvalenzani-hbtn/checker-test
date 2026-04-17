SELECT s.name AS student_name, c.title AS course_title
FROM enrollments AS e
INNER JOIN students AS s ON e.student_id = s.id
INNER JOIN courses AS c ON e.course_id = c.id
ORDER BY s.name ASC, c.title ASC;
