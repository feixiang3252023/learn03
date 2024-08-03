import psycopg2  
"""
# 连接到 PostgreSQL  
conn = psycopg2.connect(  
    dbname='postgres',  
    user='postgres',  
    password='feixiang001',  
    host='localhost',  
    port='5432'  
)  

# 创建数据库  
conn.autocommit = True  
cur = conn.cursor()  
cur.execute("CREATE DATABASE db2;")  
cur.close()  
conn.close() 
""" 

# 连接到新创建的数据库  
conn = psycopg2.connect(  
    dbname='db2',  
    user='postgres',  
    password='feixiang001',  
    host='localhost',  
    port='5432'  
)  
cur = conn.cursor()  

''' 
# 创建学生表和成绩表  
cur.execute("""  
CREATE TABLE students (  
    id SERIAL PRIMARY KEY,  
    name VARCHAR(100) NOT NULL,  
    age INTEGER  
);  
""")  
cur.execute("""  
CREATE TABLE scores (  
    id SERIAL PRIMARY KEY,  
    student_id INTEGER REFERENCES students(id),  
    subject VARCHAR(100),  
    score INTEGER  
);  
""")  
conn.commit()  
'''
# 插入学生和成绩数据  
cur.execute("INSERT INTO students (name, age) VALUES (%s, %s) RETURNING id;", ('Alice', 20))  
student_id_1 = cur.fetchone()[0]  
cur.execute("INSERT INTO students (name, age) VALUES (%s, %s) RETURNING id;", ('Bob', 22))  
student_id_2 = cur.fetchone()[0]  
cur.execute("INSERT INTO scores (student_id, subject, score) VALUES (%s, %s, %s);", (student_id_1, 'Math', 85))  
cur.execute("INSERT INTO scores (student_id, subject, score) VALUES (%s, %s, %s);", (student_id_1, 'English', 90))  
cur.execute("INSERT INTO scores (student_id, subject, score) VALUES (%s, %s, %s);", (student_id_2, 'Math', 78))  
cur.execute("INSERT INTO scores (student_id, subject, score) VALUES (%s, %s, %s);", (student_id_2, 'English', 82))  
conn.commit()  

# 查询数据  
cur.execute("""  
SELECT s.name, s.age, sc.subject, sc.score  
FROM students s  
JOIN scores sc ON s.id = sc.student_id;  
""")  
results = cur.fetchall()  
for row in results:  
    print(f"Name: {row[0]}, Age: {row[1]}, Subject: {row[2]}, Score: {row[3]}")  

cur.close()  
conn.close()