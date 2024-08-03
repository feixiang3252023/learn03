import sqlite3  

# 连接到数据库  
conn = sqlite3.connect('db1.db')  
cursor = conn.cursor()  

# 创建学生表  
cursor.execute('''  
CREATE TABLE IF NOT EXISTS students (  
    id INTEGER PRIMARY KEY AUTOINCREMENT,  
    name TEXT NOT NULL,  
    age INTEGER NOT NULL  
);  
''')  

# 创建成绩表  
cursor.execute('''  
CREATE TABLE IF NOT EXISTS grades (  
    id INTEGER PRIMARY KEY AUTOINCREMENT,  
    student_id INTEGER NOT NULL,  
    subject TEXT NOT NULL,  
    score INTEGER NOT NULL,  
    FOREIGN KEY (student_id) REFERENCES students (id)  
);  
''')  

# 提交事务  
conn.commit()  

# 插入学生数据  
students_data = [  
    ('Alice', 20),  
    ('Bob', 22),  
    ('Charlie', 21)  
]  
cursor.executemany('INSERT INTO students (name, age) VALUES (?, ?);', students_data)  

# 插入成绩数据  
grades_data = [  
    (1, 'Math', 85),  
    (1, 'English', 90),  
    (2, 'Math', 78),  
    (3, 'English', 88)  
]  
for i in range(1000):
    cursor.executemany('INSERT INTO grades (student_id, subject, score) VALUES (?, ?, ?);', grades_data)  

# 提交事务  
conn.commit()  

# 查询学生表  
cursor.execute('SELECT * FROM students;')  
students = cursor.fetchall()  
print("Students:")  
for student in students:  
    print(student)  

# 查询成绩表  
cursor.execute('SELECT * FROM grades;')  
grades = cursor.fetchall()  
print("\nGrades:")  
for grade in grades:  
    print(grade)  

# 关闭数据库连接  
conn.close()