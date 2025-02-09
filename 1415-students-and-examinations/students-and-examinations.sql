-- Write your PostgreSQL query statement below
SELECT s.student_id, s.student_name, sb.subject_name, 
    CASE 
        WHEN e.subject_name IS NULL
        THEN 0
        ELSE COUNT(sb.subject_name)
    END AS attended_exams
FROM students s
CROSS JOIN subjects sb
LEFT JOIN examinations e
ON ((s.student_id = e.student_id) AND (sb.subject_name = e.subject_name))
GROUP BY 1,2,3, e.subject_name
ORDER BY s.student_id