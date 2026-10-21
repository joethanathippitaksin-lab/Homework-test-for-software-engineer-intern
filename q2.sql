SELECT
    d.departmentName                         AS Department,
    MAX(s.salary)                            AS "Top salary",
    SUM(s.salary)                            AS "Total salary",
    CAST(ROUND(AVG(s.salary), 0) AS INTEGER) AS "Average salary"
FROM STAFF s
JOIN DEPARTMENT d
    ON d.departmentId = s.departmentId
GROUP BY d.departmentId, d.departmentName
ORDER BY d.departmentId;