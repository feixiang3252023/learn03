import pymysql  

# 连接到 MySQL  
config = {  
    'host': 'localhost',  
    'user': 'root',  # 替换为你的 MySQL 用户名  
    'password': 'Feixiang_001',  # 替换为你的 MySQL 密码  
}  

try:  
    # 连接到 MySQL  
    conn = pymysql.connect(**config)  
    cursor = conn.cursor()  

    # 创建数据库 db1  
    cursor.execute("CREATE DATABASE IF NOT EXISTS db1;")  
    cursor.execute("USE db1;")  

    # 创建学生表  
    cursor.execute("""  
    CREATE TABLE IF NOT EXISTS students (  
        id INT AUTO_INCREMENT PRIMARY KEY,  
        name VARCHAR(100) NOT NULL,  
        age INT  
    );  
    """)  

    # 创建成绩表  
    cursor.execute("""  
    CREATE TABLE IF NOT EXISTS scores (  
        id INT AUTO_INCREMENT PRIMARY KEY,  
        student_id INT,  
        subject VARCHAR(100),  
        score INT,  
        FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE  
    );  
    """)  

    # 插入学生数据  
    cursor.execute("INSERT INTO students (name, age) VALUES (%s, %s);", ('Alice', 20))  
    cursor.execute("INSERT INTO students (name, age) VALUES (%s, %s);", ('Bob', 22))  

    # 插入成绩数据  
    cursor.execute("INSERT INTO scores (student_id, subject, score) VALUES (%s, %s, %s);", (1, 'Math', 85))  
    cursor.execute("INSERT INTO scores (student_id, subject, score) VALUES (%s, %s, %s);", (1, 'English', 90))  
    cursor.execute("INSERT INTO scores (student_id, subject, score) VALUES (%s, %s, %s);", (2, 'Math', 78))  
    cursor.execute("INSERT INTO scores (student_id, subject, score) VALUES (%s, %s, %s);", (2, 'English', 82))  

    conn.commit()  # 提交事务  

    # 查询数据  
    cursor.execute("""  
    SELECT s.name, s.age, sc.subject, sc.score  
    FROM students s  
    JOIN scores sc ON s.id = sc.student_id;  
    """)  
    
    results = cursor.fetchall()  
    for row in results:  
        print(f"Name: {row[0]}, Age: {row[1]}, Subject: {row[2]}, Score: {row[3]}")  

except Exception as e:  
    print(f"An error occurred: {e}")  
finally:  
    cursor.close()  
    conn.close()