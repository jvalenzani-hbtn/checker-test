SELECT c.title AS course_title
FROM courses AS c
INNER JOIN assignments AS a ON c.id = a.course_id
GROUP BY c.id, c.title
HAVING COUNT(*) > (
    SELECT AVG(course_assignments)
    FROM (
        SELECT COUNT(*) AS course_assignments
        FROM assignments
        GROUP BY course_id
    )
)
ORDER BY c.title ASC;
