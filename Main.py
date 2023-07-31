from insert import insert
from update import update
from delete import delete
from read import read

obj=insert()
obj1=update()
obj2=delete()
obj3=read()


print('------- This is UMS Project-------')


#----------------ADD FUNCTION --------------------

opr=input('enter any operation : ')

if opr=='add':
    print('for inserting into department table please press 1: ')
    print('for inserting into course table please press 2 : ')
    print('for inserting into faculty table please enter 3 : ')
    print('for inserting into student table please enter 4 : ')

    tab=int(input('please enter the number to insert data in table : '))
    if tab==1 :    
        dptid=int(input('please enter departmentid:'))
        departmentname=str(input('please enter departmentname:'))
        obj.dptinsert(dptid,departmentname)

    
    if tab== 2 :
        courseid=int(input('please enter the course id : '))
        coursename=str(input('please enter the course name : '))
        coursefee=int(input('enter the course fee : '))
        duration=int(input('please enter  course duration : '))
        obj.courseinsert(courseid,coursename,coursefee,duration)
    
    if tab== 3 :
        facultyid=int(input('please enter the faculty id : '))
        facultyname=str(input(' please enter the faculty name : ' ))
        departmentid=int(input('please enter the deptid : ' ))
        salary=int(input('enter a salary : '))
        courseid=int(input('enter a course id : ' ))
        obj.facultyinsert(facultyid,facultyname,departmentid,salary,courseid)
    
    if tab== 4 : 
        sid=int(input('please enter a student id : '))
        sname=str(input('please enter a student name  : '))
        courseid=int(input('please enter courseid : '))
        departmentid=int(input('please enter a dept id : '))
        obj.studentinsert(sid,sname,courseid,departmentid)


        
    # ------------------------update function---------------------------
if opr=='update':
    print('for updating data into department table please enter 1 :')
    print('for updating data into course table please enter 2 : ')
    print('for updating data into faculty table  please enter 3 : ')
    print(' for updating data into student table  please enter 4 : ')
    tab=int(input('please enter the number to update data in table'))
    if tab==1 :    
        columnname=input('please enter the columnname:')
        oldvalue=input('please enter the old value:')
        newvalue=input('please enter the new value: ')
        obj1.dptupdate(columnname,newvalue,oldvalue)

    if tab==2 :
        columnname=input('please enter the columnname : ')
        oldvalue=input('please enter the old value : ')
        newvalue=input('please enter the new value : ')
        obj1.courseupdate(columnname,newvalue,oldvalue)

    if tab==3 :
        columnname=input('please enter the columnname : ')
        oldvalue=input('please enter the old value : ')
        newvalue=input('please enter the new value : ')
        obj1.facultyupdate(columnname,newvalue,oldvalue)

    if tab==4 :
        columnname=input('please enter the columnname : ')
        oldvalue=input('please enter the old value : ')
        newvalue=input('please enter the new value : ')
        obj1.studentupdate(columnname,newvalue,oldvalue)

1

# -----------------------------delete function---------------------------

if opr=='delete':
    print('for deleting  department value please enter 1 : ')
    print('for deleting course value please enter  2 : ')
    print('for deleting faculty value please enter 3: ' )
    print('for deleting student value please enter 4: ')
    tab=int(input('please enter the number to delete the data : '))

    if tab==1:
        columnname=input('please enter the column name : ')
        value=input('please enter the value : ')
        obj2.dptdelete(columnname,value)

    if tab==2:
        columnname=input('please enter the column name : ')
        value=input('please enter the value : ')
        obj2.coursedelete(columnname,value)

    if tab==3:
        columnname=input('please enter the column name : ')
        value=input('please enter the value : ')
        obj2.facultydelete(columnname,value)

    if tab==4:
        columnname=input('please enter the column name : ')
        value=input('please enter the value : ')
        obj2.studentdelete(columnname,value)


# --------------------------------------read---------------------------
if opr=='read':
    print('please  enter the press 1 : ')
    print('please  enter the press 2 : ')
    print('please  enter the press 3 : ')
    print('please  enter the press 4 : ')



    tab=int(input('please enter the number to read the data : '))
    if tab==1:
        obj3.dptread()

    if tab==2:
        obj3.courseread()
    
    if tab==3:
        obj3.facultyread()

    if tab==4:
        obj3.studentread()
    












