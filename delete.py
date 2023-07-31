import mysql.connector
conn=mysql.connector.connect(
host='localhost',
database='ums',
user='root',
password='Kumar@9948'
)
cur=conn.cursor()
class delete:
    def dptdelete(x,columnname,value):
        cur.execute(f"delete from department where {columnname}='{value}' ")
        conn.commit()
        print("Data entered successfully")

    def coursedelete(x,columnname,value):
        cur.execute(f"delete from course where {columnname}='{value}' ")
        conn.commit()
    print("Data entered successfully")


    def facultydelete(x,columnname,value):
        cur.execute(f"delete from faculty where {columnname}='{value}' ")
        conn.commit()
    print("Data entered successfully")


    def studentdelete(x,columnname,value):
        cur.execute(f"delete from student where {columnname}='{value}' ")
        conn.commit()
        print("Data entered successfully")


