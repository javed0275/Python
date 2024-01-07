class A:
    a=1
    b=2
    
    def method1(cls):
        print(cls.a)
        print(cls.b)
  
class B(A):
    c=2
    def method2(cls):
        print(cls.a)
        print(cls.b)
        print(cls.c)
  
 #by creating an object to B ,we can access all the members of both the classes A and B
        
        
    