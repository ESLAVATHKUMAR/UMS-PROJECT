import mysql.connector
conn=mysql.connector.connect(
host='localhost',
database='ums',
user='root',
password='Kumar@9948'
)


cur=conn.cursor()

class read:

    def dptread(x):
        cur.execute('select * from department')
        print(cur.fetchall())

    def courseread(x):
        cur.execute('select * from course')
        print(cur.fetchall())
    
    def facultyread(x):
        cur.execute('select * from faculty')
        print(cur.fetchall())

    def studentread(x):
        cur.execute('select * from student')
        print(cur.fetchall())
