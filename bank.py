class Bank:
    #this is constructor
    def __init__(self):
        self.accno=32456#public variable
        self.name="Raju"#public variable
        self.balance=60000.00#public variable
        self.__loan=1500000.00 #this is pvt variable # we are making loan variable as pvt
        #this variable is not available outside the class.it is not
        #even available to other methods in the same class.
        #hence it is abstracted completely from the user of the class.
    def display_to_clerk(self):
        print(self.accno)
        print(self.name)
        print(self.balance)
        #print(self.loan)
            
print('Accessing variables through method:')

p1=Bank()
p1.display_to_clerk()

print('Accessing variables through instance:')
print(p1.accno)
print(p1.name)
print(p1.balance)


    