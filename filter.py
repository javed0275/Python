# A python program using filter() to filter out even numbers from a list .
#filter() function that returns even numbers from a list
#def is_even (x):
    #if x%2==0:
        #return True
    #else:
        #return False
#let us atake a list of numbers
#lst=[10,23,45,46,70,99]
#call filter() with is_even()and lst
#lst1=list(filter(is_even,lst))
#print(lst1)
          
          
#lambda function that returns even numbers from a list
lst=[10,23,45,46,70,99]
lst1=list(filter(lambda x:(x%2==0),lst))
print(lst1)
