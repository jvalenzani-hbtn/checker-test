SELECT c.title AS course_title, s.name AS student_name
FROM courses AS c
LEFT JOIN enrollments AS e ON c.id = e.course_id
LEFT JOIN students AS s ON e.student_id = s.id
ORDER BY c.title ASC, s.name ASC;
