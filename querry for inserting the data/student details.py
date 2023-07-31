class student:
    def insert(self,sid,sname,adress,course):
        f=open('mydb.txt','a')
        f.write('\n')
        f.write(f'{sid},{sname},{adress},{course}')
        f.close()
    
obj=student()
obj.insert(1,'kumar','amangal','civil')
obj.insert(2,'kiran','amangal','eee')
obj.insert(3,'vinay','kukatpaly','b.com')

