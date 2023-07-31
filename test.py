f= open('new.txt','r')
x=f.readlines()
print(x)# read the data from our file
for i in x:
    if '\n' in i:
            print(i)





# write
f=open('new.txt','w')
f.write('randam text here ')
f.close()



# append 
f=open('new.txt','a')
f.write
f.write('randam text here ')
f.close()

# image read

f=open('ums.png','rb')
f.readlines()



k=int(input('give a number'))
if k==0:
      print('even')
else:
      print('odd')



