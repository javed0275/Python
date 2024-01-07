class Myclass:
    #this is constrcutor
    def __init__(self):
        self.__y=3   #this is a pvt variable
        
        #now it is not possible to access the variable from with in the class or out of the class
m=Myclass()
#print(m,y)
print(m._Myclass__y)  #display pvt varible y
        
        
    