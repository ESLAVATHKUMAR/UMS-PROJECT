class student:
    def addstudent(self,z):
        print(z*z)
obj=student()
obj.addstudent(10) 

#  python constructor
class unique:
    def __init__(self,li):
        self.li=li

    def countunique(self):
        k=[]
        for i in self.li:
            if i not in k:
                k.append(i)
        
        for j in k:
            count=0
            for p in self.li:
                if i==j:
                    c=c+1
            print(p)
obj=k:
obj.
                  
                  
                  
                  
#  -- in heritancre            
                  
class A():
    def f1(self):
        print('iam f1')
class B():
    def f2(self):
        print('iam f2')
class C(A,B):     
    def f3(self):
        print('iam f3')
obj=C()
obj.f3()
obj.f1()
obj.f2()



#   polymorphisem-----in this functions name is same ,always latest parameter we will get
    

class A():
    def f1 (self):
        print('iam f1')
class B(A):
    def f1(self):
        print('iam f2')
class C(B):
    def f2(self):
        print('iam 2nd f2')
obj=B()
obj.f1()


# list comprehence
# finding unique values IN SINGLE LINE,in list comprehences (1st expression-x-condition we will do)
x=[2,2,23,3,5,5,4]
k=[]
[k.append(i) for i in x if i not in k]
print(k)

 #converting string into inter with out using loops concept
x=['2','3','5','6']
k=[int(i) for i in x ]
print(k)


#  finding square in list comprehence
x=[1,2,3,4]
k=[ i*i for i in x ]
print(k)

    
# find length of more then 2 length
p=['hello','my','new','nothing']
k=[ i for i in p if len(i)>2]
print(k)


#print star pattern 
k=[print('*'*i)for i in range(1,5)]


#k=['hey','new','hayderabad'] #convert all the values in upeer case



k=['hey','new','hayderabad']
l=[i.upper()for i in k ]
print(l)

#get me the all numerical values from this string 'hello123654ew'
g='hello123654ew'
k=[i for i  in g if i.isnumeric()]
print(k)

    
# give me all the interger value only from the list ['1','5','4','22',2,5,6]
g=['1','5','4','22',2,5,6]
k=[]

    
        

# function as argument
def f2(p,q):
    print(p*q)
f2(10,20)



def f1(function):
    function (10,20)
    f1(f2)




#create sum1 function (x,y) reaction x+y
def sum1 (x,y):
    print(x*x)
    print(x+y)


# create a square function (function as a arugument) print square of that value

def square(function):
    l=function(10,20)
square(sum1)



# create myunique function return unique
# create mysum funtion take funtion of argument 

def myuniue(x):
    l=x[2,2,5,4,7,6]
    


    



