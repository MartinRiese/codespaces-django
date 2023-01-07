# Django Playground

## Setup
### Create project
```
django-admin startproject playground .
```

### Create app
```
python manage.py startapp gpa
```

### Initialize database
```
python manage.py migrate
```

### Create Admin user
```
python manage.py createsuperuser
```

### Run server
```
python manage.py runserver
```

### gpa query
```sql
SELECT iq.student_id, CAST(SUM(iq.product) AS decimal) AS product, CAST(SUM(iq.credit) AS decimal) AS credit, CAST(SUM(iq.product) AS decimal) / CAST(SUM(iq.credit) AS decimal) AS gpa
FROM (
SELECT g.student_id AS student_id, g.id, g.course_id , CAST(c.credit AS decimal) AS credit, c.credit * g.grade AS product 
FROM gpa_grade AS g LEFT JOIN gpa_course AS c ON g.course_id = c.id
) iq
GROUP BY iq.student_id

SELECT * FROM gpa_grade gg LEFT JOIN gpa_course AS c ON gg.course_id = c.id ;
```
