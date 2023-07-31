import mysql.connector
conn=mysql.connector.connect(
host='localhost',
database='ums',
user='root',
password='Kumar@9948'
)


cur=conn.cursor()
class insert:
    def dptinsert(x,dptid,departmentname):
        cur.execute(f"insert into department values({dptid},'{departmentname}')")
        conn.commit()
        print("Data entered successfully")

    def courseinsert(x,courseid,coursename,coursefee,duration):
        cur.execute(f"insert into course values({courseid},'{coursename}',{coursefee},{duration} )")
        conn.commit()
        print('data enter sucessfull')

    def facultyinsert(x,facultyid,facultyname,departmentid,salary,courseid):
        cur.execute(f"insert into faculty values ({facultyid},'{facultyname}',{departmentid},{salary},{courseid} )")
        conn.commit()
        print('DATA ENTERED SUCESSFULL')
        
    def studentinsert(x,sid,sname,courseid,departmentid):
        cur.execute(f"insert into student values ({sid},'{sname}',{courseid},{departmentid} ) ")
        conn.commit()
        print('DATA ENTERED SUCESSFULL')
        


 