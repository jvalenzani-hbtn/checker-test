SELECT s.name AS student_name
FROM students AS s
WHERE s.id IN (
    SELECT e.student_id
    FROM enrollments AS e
)
ORDER BY s.name ASC;
