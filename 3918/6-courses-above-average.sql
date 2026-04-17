SELECT c.title AS course_title
FROM courses AS c
INNER JOIN enrollments AS e ON c.id = e.course_id
GROUP BY c.id, c.title
HAVING COUNT(*) > (
    SELECT AVG(course_enrollments)
    FROM (
        SELECT COUNT(*) AS course_enrollments
        FROM enrollments
        GROUP BY course_id
    )
)
ORDER BY c.title ASC;
