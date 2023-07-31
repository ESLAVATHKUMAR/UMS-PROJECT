import mysql.connector
conn=mysql.connector.connect(
host='localhost',
database='ums',
user='root',
password='Kumar@9948'
)

# ------------------ update-----------
cur=conn.cursor()
class update:
    def dptupdate(x,columnname,newvalue,oldvalue):
        cur.execute(f"update department set {columnname}='{newvalue}'where {columnname}='{oldvalue}' ")
        conn.commit()
        print('DATA ENTERED SUCESSFULL')


    def courseupdate(x,columnname,newvalue,oldvalue):
        cur.execute(f"update course set {columnname}='{newvalue}'where {columnname}='{oldvalue}' ")
        conn.commit()
        print('DATA ENTERED SUCESSFULL')

    def facultyupdate(x,columnname,newvalue,oldvalue):
        cur.execute(f"update faculty set {columnname}='{newvalue}'where {columnname}='{oldvalue}' ")
        conn.commit()
        print('DATA ENTERED SUCESSFULL')


    def studentupdate(x,columnname,newvalue,oldvalue):
        cur.execute(f"update student  set {columnname}='{newvalue}'where {columnname}='{oldvalue}' ")
        conn.commit()
        print('DATA ENTERED SUCESSFULL')



